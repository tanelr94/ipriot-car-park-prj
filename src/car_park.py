# Handles car park operations and state

class CarPark:
    def __init__(self, name, total_bays, temperature):
        # Initializing car park with basic attributes
        self.name = name
        self.total_bays = total_bays
        self.available_bays = total_bays
        self.temperature = temperature
        self.parked_cars = []  # Listing to store license plates

    @classmethod
    def from_config(cls, filename):
        # Creating car park instance from configuration file
        try:
            with open(filename, 'r') as file:
                config = {}
                for line in file:
                    key, value = line.strip().split('=')
                    config[key.strip()] = value.strip()
                return cls(
                    config['name'],
                    int(config['total_bays']),
                    float(config['temperature'])
                )
        except FileNotFoundError:
            # Creating default car park if config file not found
            return cls("Default Park", 100, 25.0)

    def add_car(self, license_plate):
        # Adding a car to the car park if space is available
        if self.available_bays > 0:
            self.parked_cars.append(license_plate)
            self.available_bays -= 1
            self._log_entry(license_plate, "entered")
            return True
        return False

    def remove_car(self, license_plate):
        # Remove a car from the car park if it exists
        if license_plate in self.parked_cars:
            self.parked_cars.remove(license_plate)
            self.available_bays += 1
            self._log_entry(license_plate, "exited")
            return True
        return False

    def _log_entry(self, license_plate, action):
        # Log car entry/exit to file
        with open('car_park_log.txt', 'a') as file:
            file.write(f"{license_plate} {action} at {self.name}\n")

    def get_status(self):
        # Return current status of the car park
        return f"{self.name}: {self.available_bays}/{self.total_bays} bays available, Temp: {self.temperature}°C"