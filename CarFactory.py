from abc import ABC, abstractmethod

from car import Car

 
class CarFactory(ABC,Car)
  def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    self.current_date = current_date
    super().__init__(last_service_date)
    self.current_mileage = current_mileage
    self.last_service_mileage = last_service_mileage
    
  def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    self.current_date = current_date
    super().__init__(last_service_date)
    self.current_mileage = current_mileage
    self.last_service_mileage = last_service_mileage
  
  def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
    self.current_date = current_date
    super().__init__(last_service_date)
    self.warning_light_on = warning_light_on
    
  def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    self.current_date = current_date
    super().__init__(last_service_date)
    self.current_mileage = current_mileage
    self.last_service_mileage = last_service_mileage
  
  def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
    self.current_date = current_date
    super().__init__(last_service_date)
    self.current_mileage = current_mileage
    self.last_service_mileage = last_service_mileage
