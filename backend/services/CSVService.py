from flask import current_app
from utils.CriarConexaoMinioUtil import criar_conexao_minio


class CSVService:
    def __init__(self):
        self.nome_do_bucket = current_app.config["NOME_DO_BUCKET"]

    def salvar(self, arquivo: object) -> None:
        minio = criar_conexao_minio()

        minio.put_object(
            self.nome_do_bucket,
            arquivo.filename,
            arquivo,
            length=-1,
            part_size=10 * 1024 * 1024,
        )

    def listar_links(self) -> list:
        minio = criar_conexao_minio()

        objetos_do_minio = minio.list_objects(self.nome_do_bucket)

        url_base = "http://localhost:5000/BaixarCSV/"

        return [
            {"nome": obj.object_name, "url": url_base + obj.object_name}
            for obj in objetos_do_minio
            if obj.object_name.endswith(".csv")
        ]

    def baixar_csv(self, nome_do_arquivo: str) -> bytes:
        minio = criar_conexao_minio()

        objeto_do_minio = minio.get_object(self.nome_do_bucket, nome_do_arquivo)

        conteudo_do_csv = objeto_do_minio.read()

        objeto_do_minio.close()

        objeto_do_minio.release_conn()

        return conteudo_do_csv
