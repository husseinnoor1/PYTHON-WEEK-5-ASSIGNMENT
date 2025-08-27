# Base class
class SmartDevice:
    def __init__(self, brand, model, battery_level):
        self.brand = brand
        self.model = model
        self._battery_level = battery_level  # protected attribute

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def show_battery(self):
        print(f"Battery level: {self._battery_level}%")

    def charge(self, amount):
        self._battery_level = min(100, self._battery_level + amount)
        print(f"{self.brand} {self.model} charged to {self._battery_level}%.")

# Subclass 1
class Smartphone(SmartDevice):
    def __init__(self, brand, model, battery_level, phone_number):
        super().__init__(brand, model, battery_level)
        self.__phone_number = phone_number  # private attribute

    def call(self, number):
        print(f"Calling {number} from {self.__phone_number}...")

    def show_battery(self):  # Polymorphism: override method
        print(f"Smartphone Battery: {self._battery_level}%")

# Subclass 2
class Smartwatch(SmartDevice):
    def __init__(self, brand, model, battery_level, heart_rate=70):
        super().__init__(brand, model, battery_level)
        self.heart_rate = heart_rate

    def track_heart_rate(self):
        print(f"Tracking heart rate... Current: {self.heart_rate} BPM")

    def show_battery(self):  # Polymorphism: override method
        print(f"Smartwatch Battery: {self._battery_level}%")
