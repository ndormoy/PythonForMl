class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar) -> None:
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        if (scalar == 0):
            raise ValueError("You cannot divide by zero")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
