from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character class"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Character constructor"""
        pass

    def die(self):
        """Die funct Character"""
        pass


class Stark(Character):
    """Stark Class inerhite from Character"""
    def __init__(self, name, is_alive=True):
        """Stark constructor"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Die funct Stark"""
        self.is_alive = False
