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
