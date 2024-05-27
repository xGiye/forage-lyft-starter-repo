from abc import ABC

class Tire(ABC):
    def __init__(self) -> None:
        super().__init__()
        
    def need_service(self):
        pass