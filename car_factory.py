from car import Car
from engine.engine import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.tires import Tires
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory():
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_info):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_info)
        calliope = Car(engine, battery, tires)
        return calliope
    
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_info):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires(tires_info)
        glissade = Car(engine, battery, tires)
        return glissade
    
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_on, tires_info):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_info)
        palindrome = Car(engine, battery, tires)
        return palindrome
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_info):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_info)
        rorschach = Car(engine, battery, tires)
        return rorschach
    
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tires_info):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tires_info)
        thovex = Car(engine, battery, tires)
        return thovex