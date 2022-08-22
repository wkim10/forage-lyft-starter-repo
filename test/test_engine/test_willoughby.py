import unittest
import sys
sys.path.append('/Users/won/Desktop/Forage Projects/Lyft Back-End Engineering/forage-lyft-starter-repo-main')

from engine.willoughby_engine import WilloughbyEngine

class TestWilloughby(unittest.TestCase):
    def test_service_needed(self):
        last_service_mileage = 0
        current_mileage = 60010
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_service_not_needed(self):
        last_service_mileage = 0
        current_mileage = 59999
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()