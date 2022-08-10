from tire.tire import Tire
from utils import add_years_to_date
from array import *


class Carrigan(Tire):
    def __init__(self, arr):
        self.arr = arr

    def needs_service(self,arr):
        for i in arr
          if i >= 0.9:
            return True
        return False
