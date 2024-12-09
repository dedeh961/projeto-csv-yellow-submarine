import logging


class ArquivoNaoCSVException(Exception):
    def __init__(self, nome_do_arquivo: str) -> None:
        super().__init__("Apenas arquivos CSV são permitidos")

        logging.error(f"Apenas arquivos CSV são permitidos: {nome_do_arquivo}")
