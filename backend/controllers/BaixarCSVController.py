from enums.CodigoHTTPEnum import CodigoHTTP
from flask import Blueprint, Response, abort
from flask.views import MethodView
from minio.error import S3Error
from services.CSVService import CSVService

blp = Blueprint("BaixarCSVController", __name__)


class BaixarCSVController(MethodView):
    def get(self, nome_do_arquivo: str) -> tuple:
        try:
            conteudo_do_csv = CSVService().baixar_csv(nome_do_arquivo)

            return Response(conteudo_do_csv, mimetype="text/csv")

        except S3Error as e:
            return abort(CodigoHTTP.erro_interno.value, str(e))


baixar_csv_view = BaixarCSVController.as_view("baixar_csv_view")

blp.add_url_rule("/BaixarCSV/<string:nome_do_arquivo>", view_func=baixar_csv_view)
