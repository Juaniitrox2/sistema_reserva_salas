"""Define las excepciones que usan los demás modulos"""

class InvalidDateValue(Exception):
    """Error raiseado cuando un valor de la fecha está fuera de sus limites"""
    def __init__(self, message: str) -> None:
        self.message = message
