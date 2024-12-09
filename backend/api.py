import os

from controllers.SalvarCSVController import blp as SalvarCSVBlueprint
from dotenv import dotenv_values
from flask import Flask, Response, abort
from flask_cors import CORS
from minio import Minio
from minio.error import S3Error
from waitress import serve


def create_app():
    app = Flask(__name__)

    CORS(app)

    variaveis_de_ambiente = {
        **dotenv_values(".env"),
        **os.environ,
    }

    app.config.update(variaveis_de_ambiente)

    client = Minio(
        app.config["MINIO_ENDPOINT"].replace("http://", ""),
        access_key=app.config["MINIO_ACCESS_KEY"],
        secret_key=app.config["MINIO_SECRET_KEY"],
        secure=False,
    )

    nome_do_bucket = app.config["NOME_DO_BUCKET"]

    bucket = client.bucket_exists(nome_do_bucket)

    if not bucket:
        client.make_bucket(nome_do_bucket)

    app.register_blueprint(SalvarCSVBlueprint)

    @app.route("/ListaDeCSVs", methods=["GET"])
    def lista_de_csvs():
        try:
            objetos_do_minio = client.list_objects(nome_do_bucket)

            url_base = "http://localhost:5000/BaixarCSV/"

            lista_de_arquivos = [
                {"nome": obj.object_name, "url": url_base + obj.object_name}
                for obj in objetos_do_minio
                if obj.object_name.endswith(".csv")
            ]

            return {"lista_de_arquivos": lista_de_arquivos}

        except S3Error as e:
            return abort(500, str(e))

    @app.route("/BaixarCSV/<string:nome_do_arquivo>", methods=["GET"])
    def baixar_csv(nome_do_arquivo):
        try:
            objeto_do_minio = client.get_object(nome_do_bucket, nome_do_arquivo)

            conteudo_do_csv = objeto_do_minio.read()

            objeto_do_minio.close()

            objeto_do_minio.release_conn()

            return Response(conteudo_do_csv, mimetype="text/csv")

        except S3Error as e:
            return abort(500, str(e))

    return app


if __name__ == "__main__":
    app = create_app()
    serve(app, host="0.0.0.0", port=80)
    # app.run(host="0.0.0.0", port=80)
