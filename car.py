# from abc import ABC, abstractmethod
from battery.battery import Battery
from engine.engine import Engine
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine
    
    def needs_service(self) -> bool:
        if self.battery.needs_service():
            return True
        elif self.engine.engine_should_be_serviced():
            return True
        else:
            return False
            
            