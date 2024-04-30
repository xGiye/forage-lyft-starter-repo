# from abc import ABC, abstractmethod
from battery import Battery
from engine import Engine

class Car:
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine
    
    def needs_service(self) -> bool:
        if(self.battery.needs_service or self.engine.needs_service):
            return True
        else:
            return False
            