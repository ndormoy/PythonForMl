from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character class"""
    def __init__(self, name, is_alive=True):
        """Character constructor"""
        if not isinstance(name, str):
            raise ValueError("first_name must be a string")
        elif not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean")
        self.name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Die funct Character"""
        self.is_alive = False


class Stark(Character):
    """Stark Class inerhite from Character"""
    def __init__(self, name, is_alive=True):
        """Stark constructor"""
        super().__init__(name, is_alive)

    def die(self):
        """Stark die function"""
        super().die()
