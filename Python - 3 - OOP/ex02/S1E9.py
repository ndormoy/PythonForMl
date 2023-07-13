from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character class"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        if not isinstance(first_name, str):
            raise ValueError("first_name must be a string")
        elif not isinstance(is_alive, bool):
            raise ValueError("is_alive must be a boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Die funct Character"""
        self.is_alive = False


class Stark(Character):
    """Stark Class inerhite from Character"""
    def __init__(self, first_name, is_alive=True):
        """Stark constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Stark die function"""
        super().die()
