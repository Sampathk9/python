#!/usr/bin/env python3
import logging
from abc import ABC, abstractmethod

# --------------------------------------------------------
# LOGGING SETUP
# --------------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------------
# 1. ABSTRACTION + POLYMORPHISM + ENCAPSULATION
# --------------------------------------------------------
class Device(ABC):
    """Abstract base class for all devices."""

    def __init__(self, name):
        self._name = name     # protected
        self.__status = False # private
        logging.debug(f"Device created: {self._name}")

    def turn_on(self):
        self.__status = True
        logging.info(f"{self._name}: Turned ON")

    def turn_off(self):
        self.__status = False
        logging.info(f"{self._name}: Turned OFF")

    def get_status(self):
        return self.__status

    @abstractmethod
    def operate(self):
        pass


class Light(Device):
    def operate(self):
        logging.debug(f"Operating Light: {self._name}")
        if self.get_status():
            return f"{self._name} light is shining."
        return f"{self._name} light is off."


class Thermostat(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature
        logging.debug(f"Thermostat created: {self._name}, Temp={self.temperature}")

    def operate(self):
        logging.debug(f"Operating Thermostat: {self._name}")
        if self.get_status():
            return f"{self._name} thermostat set to {self.temperature}°C."
        return f"{self._name} thermostat is off."


class SecurityCamera(Device):
    def operate(self):
        logging.debug(f"Operating SecurityCamera: {self._name}")
        if self.get_status():
            return f"{self._name} camera is recording..."
        return f"{self._name} camera is idle."


# --------------------------------------------------------
# 6. AGGREGATION & 7. COMPOSITION
# --------------------------------------------------------
class Room:
    def __init__(self, name):
        self.name = name
        self.devices = []
        logging.debug(f"Room created: {self.name}")

    def add_device(self, device):
        self.devices.append(device)
        logging.info(f"{device._name} added to room: {self.name}")

    def operate_all(self):
        logging.debug(f"Operating all devices in room: {self.name}")
        return [device.operate() for device in self.devices]


# --------------------------------------------------------
# 5. ASSOCIATION
# --------------------------------------------------------
class Owner:
    def __init__(self, name):
        self.name = name
        logging.debug(f"Owner created: {self.name}")


class Home:
    def __init__(self, owner):
        self.owner = owner
        self.rooms = []
        logging.debug(f"Home initialized for owner: {self.owner.name}")

    def add_room(self, room):
        self.rooms.append(room)
        logging.info(f"Room added to home: {room.name}")

    def system_status(self):
        logging.debug("Generating system status report...")
        status_report = []
        # logging.debug(f"Home rooms: {[ (r.name, len(r.devices)) for r in self.rooms ]}")
        logging.debug(f"Home rooms: {[ (r.name, [d._name for d in r.devices]) for r in self.rooms ]}")
        for room in self.rooms:
            status_report.append(f"Room: {room.name}")
            for device in room.devices:
                status_report.append("  - " + device.operate())
        return status_report


# --------------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------------
if __name__ == "__main__":

    logging.info("Smart Home System Starting...")

    # Association
    owner = Owner("Alice")
    home = Home(owner)

    # Rooms (Aggregation)
    living_room = Room("Living Room")
    bedroom = Room("Bedroom")

    # Devices (Composition)
    light = Light("Ceiling")
    thermostat = Thermostat("Main")
    camera = SecurityCamera("Front Door")

    # Activate some devices
    light.turn_on()
    camera.turn_on()

    # Add devices to rooms
    living_room.add_device(light)
    living_room.add_device(camera)
    bedroom.add_device(thermostat)

    # Add rooms to home
    home.add_room(living_room)
    home.add_room(bedroom)

    # Display system status
    logging.info("System Status:")
    for line in home.system_status():
        print(line)
