class calculator:
    """Calulator class"""
    def __init__(self, first_vector, second_vector):
        """Constructor"""
        self.first_vector = first_vector
        self.second_vector = second_vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Dotproduct with two vectors"""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors"""
        res = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Soustract two vectors"""
        res = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
