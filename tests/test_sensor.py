import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, True, self.car_park)

    def test_entry_sensor_detects_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 99)

    def test_exit_sensor_detects_vehicle(self):
        self.car_park.add_car("FAKE-001")
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.available_bays, 100)

if __name__ == "__main__":
    unittest.main()