from abc import ABC

from tires.tires import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, tires_info):
        self.tires_info = tires_info
    
    def needs_service(self):
        for tire in self.tires_info:
            if tire >= 0.9:
                return True
        return False