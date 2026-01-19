#!/usr/bin/env python3
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.DEBUG)
# --------------------------------------------------------
# 1. ABSTRACTION + 4. POLYMORPHISM (method overriding)
# --------------------------------------------------------
class Device(ABC):
    """Abstract base class for all devices."""

    def __init__(self, name):
        self._name = name     # Encapsulated (protected)
        self.__status = False # Encapsulated (private)

    def turn_on(self):
        self.__status = True

    def turn_off(self):
        self.__status = False

    def get_status(self):
        return self.__status

    @abstractmethod
    def operate(self):
        """Each device must implement its own behavior."""
        pass


class Light(Device):
    def operate(self):
        if self.get_status():
            return f"{self._name} light is shining."
        return f"{self._name} light is off."


class Thermostat(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self.temperature = temperature

    def operate(self):
        if self.get_status():
            return f"{self._name} thermostat set to {self.temperature}°C."
        return f"{self._name} thermostat is off."


class SecurityCamera(Device):
    def operate(self):
        if self.get_status():
            return f"{self._name} camera is recording..."
        return f"{self._name} camera is idle."


# --------------------------------------------------------
# 6. AGGREGATION (Home has Rooms, but Rooms can exist alone)
# --------------------------------------------------------
class Room:
    """Room contains devices — COMPOSITION: If room is deleted, devices go too."""

    def __init__(self, name):
        self.name = name
        self.devices = []  # Composition: devices belong *only* to this room

    def add_device(self, device):
        self.devices.append(device)

    def operate_all(self):
        return [device.operate() for device in self.devices]


# --------------------------------------------------------
# 5. ASSOCIATION (Home associated with Owner, not owning them)
# --------------------------------------------------------
class Owner:
    def __init__(self, name):
        self.name = name


class Home:
    def __init__(self, owner):
        self.owner = owner  # Association: both can exist independently
        self.rooms = []     # Aggregation

    def add_room(self, room):
        self.rooms.append(room)

    def system_status(self):
        status_report = []
        for room in self.rooms:
            status_report.append(f"Room: {room.name}")
            for device in room.devices:
                status_report.append("  - " + device.operate())
        return status_report


# --------------------------------------------------------
# FULL SYSTEM DEMONSTRATION
# --------------------------------------------------------
if __name__ == "__main__":

    # Association: Home <-> Owner
    owner = Owner("Alice")
    home = Home(owner)

    # Rooms (can exist without Home) → Aggregation
    living_room = Room("Living Room")
    bedroom = Room("Bedroom")

    # Devices (exist only inside a room) → Composition
    light = Light("Ceiling")
    thermostat = Thermostat("Main")
    camera = SecurityCamera("Front Door")

    # Turn on some devices
    light.turn_on()
    camera.turn_on()

    # Add devices to rooms
    living_room.add_device(light)
    living_room.add_device(camera)
    bedroom.add_device(thermostat)

    # Add rooms to home
    home.add_room(living_room)
    home.add_room(bedroom)

    # Show system status
    for line in home.system_status():
        print(line)
