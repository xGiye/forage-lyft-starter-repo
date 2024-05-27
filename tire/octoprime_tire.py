from tire.tire import Tire 

class OctoprimeTire(Tire):
    def __init__(self, sensor_tire_readings) -> None:
        super().__init__()
        self.sensor_tire_reading = sensor_tire_readings
    def need_service(self):
        if sum(self.sensor_tire_reading)> 3:
            return True
        else:
            return False