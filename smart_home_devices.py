from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self._name} is {status}")

    def _turn_on(self):
        self.__is_on = True

    def _turn_off(self):
        self.__is_on = False

    def is_on(self):
        return self.__is_on


class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 0

    def operate(self):
        self._turn_on()
        self.__brightness = 70
        print(f"{self._name} is turned ON with brightness {self.__brightness}%")

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value

    def get_brightness(self):
        return self.__brightness


class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Low"

    def operate(self):
        self._turn_on()
        self.__speed = "Medium"
        print(f"{self._name} is turned ON with speed {self.__speed}")

    def set_speed(self, value):
        if value in ["Low", "Medium", "High"]:
            self.__speed = value

    def get_speed(self):
        return self.__speed


class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 0

    def operate(self):
        self._turn_on()
        self.__temperature = 24
        print(f"{self._name} is turned ON with temperature {self.__temperature}°C")

    def set_temperature(self, value):
        if 16 <= value <= 30:
            self.__temperature = value

    def get_temperature(self):
        return self.__temperature


light = SmartLight("Bedroom Light")
fan = SmartFan("Hall Fan")
ac = SmartAC("Office AC")

devices = [light, fan, ac]

for device in devices:
    device.operate()
    device.show_status()

try:
    light.__brightness = 50
except AttributeError as e:
    print("Access Error:", e)

try:
    fan.__speed = "High"
except AttributeError as e:
    print("Access Error:", e)

try:
    ac.__temperature = 20
except AttributeError as e:
    print("Access Error:", e)

light.set_brightness(90)
fan.set_speed("High")
ac.set_temperature(22)

print("Updated Brightness:", light.get_brightness())
print("Updated Speed:", fan.get_speed())
print("Updated Temperature:", ac.get_temperature())
