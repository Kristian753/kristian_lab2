class Circle:
    def __init__(self, x, y, radius):
        if Type(radius) not in [int, float]:
            raise TypeError("Radius must be a number.")
        self.x = x
        self.y = y
        self.radius = radius