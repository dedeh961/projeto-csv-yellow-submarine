import os

from controllers.BaixarCSVController import blp as BaixarCSVBlueprint
from controllers.ListarCSVsController import blp as ListarCSVsBlueprint
from controllers.SalvarCSVController import blp as SalvarCSVBlueprint
from dotenv import dotenv_values
from flask import Flask
from flask_cors import CORS
from minio import Minio
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
    app.register_blueprint(ListarCSVsBlueprint)
    app.register_blueprint(BaixarCSVBlueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    serve(app, host="0.0.0.0", port=80)
    # app.run(host="0.0.0.0", port=80)
