from flask import current_app
from utils.MinioUtil import MinioUtil


class CSVService:
    def __init__(self):
        self.nome_do_bucket = current_app.config["NOME_DO_BUCKET"]
        self.minio = MinioUtil().criar_conexao()
        self.url_base_baixar_csv = "http://localhost:5000/BaixarCSV/"

    def salvar(self, arquivo: object) -> None:
        self.minio.put_object(
            bucket_name=self.nome_do_bucket,
            object_name=arquivo.filename,
            data=arquivo,
            length=-1,
            part_size=10 * 1024 * 1024,
        )

    def listar_links(self) -> list:
        objetos_do_minio = self.minio.list_objects(self.nome_do_bucket)

        return [
            {
                "id": i + 1,
                "nome": obj.object_name,
                "url": self.url_base_baixar_csv + obj.object_name,
            }
            for i, obj in enumerate(objetos_do_minio)
            if obj.object_name.endswith(".csv")
        ]

    def baixar_csv(self, nome_do_arquivo: str) -> bytes:
        objeto_do_minio = self.minio.get_object(self.nome_do_bucket, nome_do_arquivo)

        conteudo_do_csv = objeto_do_minio.read()

        MinioUtil().fechar_conexao(objeto_do_minio)

        return conteudo_do_csv
