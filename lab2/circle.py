class Circle:
    def __init__(self, x, y, radius):
        # kollar om radius är ett tal
        if Type(radius) not in [int, float]: 
            raise TypeError("Radius must be a number.")
        self.x = x
        self.y = y
        self.radius = radius

@property
def area(self):
    return 3.14 * self.radius * self.radius
