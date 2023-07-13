from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(
            self, first_name=None, is_alive=True):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the string representation of the Baratheon object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the string representation of the Baratheon object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Baratheon die function"""
        super().die()


class Lannister(Character):
    def __init__(
            self, first_name=None, is_alive=True):
        """Lannister constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """Return the string representation of the Lannister object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return the string representation of the Lannister object"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """Lannister die function"""
        super().die()

    @classmethod
    def create_lannister(self, first_name, is_alive=True):
        """Class method to create a Lannister object"""
        lannister = self(first_name, is_alive)
        # Additional logic for creating a Lannister object
        return lannister
