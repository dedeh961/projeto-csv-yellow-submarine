from flask import current_app
from minio import Minio


class MinioUtil:
    def __init__(self):
        self.nome_do_bucket = current_app.config["NOME_DO_BUCKET"]
        self.acess_key = current_app.config["MINIO_ACCESS_KEY"]
        self.secret_key = current_app.config["MINIO_SECRET_KEY"]
        self.endpoint = current_app.config["MINIO_ENDPOINT"].replace("http://", "")

    def criar_bucket(self) -> None:
        minio = self.criar_conexao()

        if not minio.bucket_exists(self.nome_do_bucket):
            minio.make_bucket(self.nome_do_bucket)

    def criar_conexao(self) -> Minio:
        return Minio(
            endpoint=self.endpoint,
            access_key=self.acess_key,
            secret_key=self.secret_key,
            secure=False,
        )
