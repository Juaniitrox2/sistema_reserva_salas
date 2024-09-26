"""Define las excepciones que usan los demás modulos"""

class InvalidDateValue(Exception):
    """Error raiseado cuando un valor de la fecha está fuera de sus limites"""
    def __init__(self, message: str) -> None:
        self.message = message

class InvalidRoom(Exception):
    """Error levantado cuando se produce un error con salas en el sistema de reservas"""
    def __init__(self, message: str) -> None:
        self.message = message
