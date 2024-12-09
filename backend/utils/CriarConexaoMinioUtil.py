from flask import current_app
from minio import Minio


def criar_conexao_minio() -> Minio:
    return Minio(
        current_app.config["MINIO_ENDPOINT"].replace("http://", ""),
        access_key=current_app.config["MINIO_ACCESS_KEY"],
        secret_key=current_app.config["MINIO_SECRET_KEY"],
        secure=False,
    )
