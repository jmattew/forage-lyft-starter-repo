import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        cpEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(cpEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        cpEngine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(cpEngine.needs_service())
       
class TestSternman(unittest.TestCase):
   def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        stEngine = SternmanEngine(self, warning_light_is_on)
        self.assertTrue(stEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        stEngine = SternmanEngine(self, warning_light_is_on)
        self.assertFalse(car.needs_service())
        
class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        wbEngine = WilloughbyEngine(self, current_mileage, last_service_mileage)
        self.assertTrue(wbEngine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        wbEngine = WilloughbyEngine(self, current_mileage, last_service_mileage)
        self.assertFalse(wbEngine.needs_service())

