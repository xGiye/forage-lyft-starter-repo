from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self,tire_sensor_reading) -> None:
        super().__init__()
        self.tire_sensor_reading = tire_sensor_reading
    
    def need_service(self):
        if any(int(reading) for reading in self.tire_sensor_reading):
            return True
        else:
            return False