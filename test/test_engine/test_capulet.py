import unittest
import sys
sys.path.append('/Users/won/Desktop/Forage Projects/Lyft Back-End Engineering/forage-lyft-starter-repo-main')

from engine.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def test_service_needed(self):
        last_service_mileage = 0
        current_mileage = 30010
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_service_not_needed(self):
        last_service_mileage = 0
        current_mileage = 29999
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()