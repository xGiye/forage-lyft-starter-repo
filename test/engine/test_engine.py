import unittest
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestCapuletEngine(unittest.TestCase):
    def test_should_serviced(self):
        current_mileage = 45000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 25000
        
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.engine_should_be_serviced())
        
class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 60010
        last_service_mileage = 2
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.engine_should_be_serviced())
        
    def test_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 20000
        
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.engine_should_be_serviced())