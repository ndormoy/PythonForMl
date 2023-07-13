class calculator:
    """Calculator class"""
    def __init__(self, vector):
        """Constructor"""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """add method"""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """multiply method"""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """subtract method"""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """divide method"""
        if (scalar == 0):
            raise ValueError("You cannot divide by zero")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
