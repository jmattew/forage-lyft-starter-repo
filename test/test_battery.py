import unittest
from datetime import datetime

from battery.SpindlerBattery import SpindlerBattery
from battery.NubbinBattery import NubbinBattery

class TestSpindler(unittest.TestCase)
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        spBattery = SpindlerBattery(self,today,last_service_date)
        self.assertTrue(spBattery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spBattery = SpindlerBattery(self,today,last_service_date)
        self.assertFalse(spBattery.needs_service())
    
class TestNubbin(unittest.TestCase)
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nbBattery = NubbinBattery(last_service_date)
        self.assertTrue(nbBattery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        nbBattery = NubbinBattery(last_service_date)
        self.assertFalse(nbBattery.needs_service())
