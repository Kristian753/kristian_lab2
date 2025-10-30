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
    # räkna area med pi
    return 3.14 * self.radius * self.radius

@property
def perimeter(self):
    # räknar cirkelns omkrets
    return 2 * 3.14 * self.radius 

def translate(self, dx, dy):
    # kollar om dx och dy är nummer
    if type(dx) not in [int, float] or type(dy) not in [int, float]:
        raise TypeError("dx and dy must be numbers")
    self.x += dx
    self.y += dy 

def is_unit_circle(self):
    # kollar om cirkeln är en enhetscirkel
    return self.radius == 1 and self.x == 0 and self.y == 0
 

