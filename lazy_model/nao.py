class NotAnObject:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "NAO"


NAO = NotAnObject()
