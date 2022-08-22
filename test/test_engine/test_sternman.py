import unittest
import sys
sys.path.append('/Users/won/Desktop/Forage Projects/Lyft Back-End Engineering/forage-lyft-starter-repo-main')

from engine.sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase):
    def test_service_needed(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_service_not_needed(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()