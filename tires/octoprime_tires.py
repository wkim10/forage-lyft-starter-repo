from abc import ABC

from tires.tires import Tires

class OctoprimeTires(Tires, ABC):
    def __init__(self, tires_info):
        self.tires_info = tires_info
    
    def needs_service(self):
        return sum(self.tires_info) >= 3