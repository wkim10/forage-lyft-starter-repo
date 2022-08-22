import unittest
import sys
sys.path.append('/Users/won/Desktop/Forage Projects/Lyft Back-End Engineering/forage-lyft-starter-repo-main')

from battery.nubbin_battery import NubbinBattery

from datetime import date

class TestNubbin(unittest.TestCase):
    def test_service_needed(self):
        last_service_date = date.fromisoformat("2017-08-22")
        current_date = date.fromisoformat("2022-08-22")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_service_not_needed(self):
        last_service_date = date.fromisoformat("2019-08-22")
        current_date = date.fromisoformat("2022-08-22")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()