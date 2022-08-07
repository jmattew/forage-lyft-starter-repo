from abc import ABC, abstractmethod

from Serviceable import Serviceable

class Car(ABC, Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

class Engine(ABC):        
    @abstractmethod
    def needs_service(self):
        pass

class Battery(ABC): 
    @abstractmethod
    def needs_service(self):
        pass
