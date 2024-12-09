from enums.CodigoHTTPEnum import CodigoHTTP
from flask import Blueprint, abort, jsonify, request
from flask.views import MethodView
from minio.error import S3Error
from services.CSVService import CSVService
from utils.ArquivoNaoCSVExceptionUtil import ArquivoNaoCSVException
from werkzeug.utils import secure_filename

blp = Blueprint("SalvarCSVController", __name__)


class SalvarCSVController(MethodView):
    def post(self) -> tuple:
        try:
            arquivo = request.files["filepond"]

            nome_do_arquivo = secure_filename(arquivo.filename)

            if not nome_do_arquivo.endswith(".csv"):
                raise ArquivoNaoCSVException(nome_do_arquivo)

            CSVService().salvar(arquivo)

            return (
                jsonify({"message": "Arquivo enviado com sucesso"}),
                CodigoHTTP.aceito.value,
            )

        except ArquivoNaoCSVException:
            return abort(
                CodigoHTTP.erro_interno.value, "Apenas arquivos CSV são permitidos"
            )

        except S3Error as e:
            return abort(CodigoHTTP.erro_interno.value, str(e))


salvar_csv_view = SalvarCSVController.as_view("salvar_csv_view")

blp.add_url_rule("/SalvarCSV", view_func=salvar_csv_view)
