from tire.tire import Tire
from utils import add_years_to_date
from array import *


class Octoprime(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self,arr):
        sum = 0
        for i in arr:
          sum += i
        if sum >= 3:
          return True
        return False
