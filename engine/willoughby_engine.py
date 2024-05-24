# from abc import ABC

# from car import Car

from engine.engine import Engine


class WilloughbyEngine(Engine) :
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
