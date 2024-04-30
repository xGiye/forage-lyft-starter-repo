from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpinderBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    def __init__(self) -> None:
       pass
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        battery = SpinderBattery(current_date,last_service_date)
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        new_car = Car(battery, engine)
        return new_car
     
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)-> Car:
        battery = SpinderBattery(current_date,last_service_date)
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        new_car = Car(battery, engine)
        return new_car
    
    
    def create_palindrome(current_date, last_service_date, warning_light_on)-> Car:
        battery = SpinderBattery(current_date,last_service_date)
        engine = SternmanEngine(warning_light_on)
        new_car = Car(battery, engine)
        return new_car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)-> Car:
        battery = NubbinBattery(current_date,last_service_date)
        engine = WilloughbyEngine(last_service_date,current_mileage,last_service_mileage)
        new_car = Car(battery, engine)
        return new_car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)->Car:
        battery = NubbinBattery(current_date,last_service_date)
        engine = CapuletEngine(last_service_date,current_mileage,last_service_mileage)
        new_car = Car(battery, engine)
        return new_car
    
         
         
         
         