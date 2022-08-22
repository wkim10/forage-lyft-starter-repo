import unittest
import sys
sys.path.append('/Users/won/Desktop/Forage Projects/Lyft Back-End Engineering/forage-lyft-starter-repo-main')

from tires.carrigan_tires import CarriganTires

class TestCarrigan(unittest.TestCase):
    def test_service_needed(self):
        tires_info = [0.1, 0.2, 0.3, 0.9]
        tires = CarriganTires(tires_info)
        self.assertTrue(tires.needs_service())

    def test_service_not_needed(self):
        tires_info = [0.1, 0.2, 0.3, 0.4]
        tires = CarriganTires(tires_info)
        self.assertFalse(tires.needs_service())
        

if __name__ == '__main__':
    unittest.main()