import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpinderBattery

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year= current_date.year - 5)
        
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_shoud_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year -2)
        
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())

