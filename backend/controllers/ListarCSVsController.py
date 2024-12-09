from enums.CodigoHTTPEnum import CodigoHTTP
from flask import Blueprint, abort, send_file
from flask.views import MethodView
from minio.error import S3Error
from services.CSVService import CSVService

blp = Blueprint("ListarCSVsController", __name__)


class ListarCSVsController(MethodView):
    def get(self) -> tuple:
        try:
            links = CSVService().listar_links()

            return {"links": links}, CodigoHTTP.aceito.value

        except S3Error as e:
            return abort(CodigoHTTP.erro_interno.value, str(e))


listar_csvs = ListarCSVsController.as_view("listar_csvs")

blp.add_url_rule("/ListarCSVs", view_func=listar_csvs)
