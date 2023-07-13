from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract Character class"""
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
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

