import os

from controllers.BaixarCSVController import blp as BaixarCSVBlueprint
from controllers.ListarCSVsController import blp as ListarCSVsBlueprint
from controllers.SalvarCSVController import blp as SalvarCSVBlueprint
from dotenv import dotenv_values
from flask import Flask
from flask_cors import CORS
from utils.MinioUtil import MinioUtil
from waitress import serve


def create_app():
    app = Flask(__name__)

    CORS(app)

    variaveis_de_ambiente = {
        **dotenv_values(".env"),
        **os.environ,
    }

    app.config.update(variaveis_de_ambiente)

    app.register_blueprint(SalvarCSVBlueprint)
    app.register_blueprint(ListarCSVsBlueprint)
    app.register_blueprint(BaixarCSVBlueprint)

    with app.app_context():
        MinioUtil().criar_bucket()

    return app


if __name__ == "__main__":
    app = create_app()
    serve(app, host="0.0.0.0", port=80)
    # app.run(host="0.0.0.0", port=80)
