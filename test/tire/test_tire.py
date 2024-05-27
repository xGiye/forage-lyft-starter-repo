import unittest
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCariiganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        sensor_reading =[1,0.8,0.7,0.6]
        
        car_tires = CarriganTire(sensor_reading)
        self.assertTrue(car_tires.need_service())
    
    def test_should_not_be_serviced(self):
        sensor_reading =[0.3,0.8,0.7,0.6]
        
        car_tires = CarriganTire(sensor_reading)
        self.assertFalse(car_tires.need_service())  
        
class TestOctoprimeTires(unittest.TestCase):
    def test_should_be_tested(self):
        senor_reading = [1,0.9,0.9,1]
        car_tires = OctoprimeTire(senor_reading)
        
        self.assertTrue(car_tires.need_service())
        
    def test_should_not_be_tested(self):
        senor_reading = [1,0.4,0.4,0.5]
        car_tires = OctoprimeTire(senor_reading)
        
        self.assertFalse(car_tires.need_service())