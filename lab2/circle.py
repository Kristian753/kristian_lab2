class Circle:
    def __init__(self, x, y, radius):
        # kollar om radius är ett tal
        if type(radius) not in [int, float]: 
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.x = x
        self.y = y
        self.radius = radius

    @property # read only property
    def area(self):
    # räkna area med pi
        return 3.14 * self.radius * self.radius

    @property # read only property
    def perimeter(self):
    # räknar cirkelns omkrets
        return 2 * 3.14 * self.radius 

    def translate(self, dx, dy):# flyttar cirkeln
    # kollar om dx och dy är nummer
        if type(dx) not in [int, float] or type(dy) not in [int, float]:
            raise TypeError("dx and dy must be numbers")
        self.x += dx
        self.y += dy 

    def is_unit_circle(self):
    # kollar om cirkeln är en enhetscirkel
     return self.radius == 1 and self.x == 0 and self.y == 0

    def __eq__(self, other):# kollar om två cirklar är lika
        if not isinstance(other, Circle): return False
        return self.radius == other.radius
    
    def __gt__(self,other):# kollar om en cirkel är större än en annan
        if not isinstance(other, Circle): return False
        return self.radius > other
    
    def __lt__(self,other):# kollar om en cirkel är mindre än en annan
        if not isinstance(other, Circle): return False
        return self.radius < other.radius
    
    def __le__(self,other):# kollar om en cirkel är mindre än eller lika med en annan
        if not isinstance(other, Circle): return False
        return self.radius <= other.radius
    
    def __ge__(self,other):# kollar om en cirkel är större än eller lika med en annan
        if not isinstance(other, Circle): return False
        return self.radius >= other.radius
    
    def __repr__(self):  
        return f"Circle({self.x}, {self.y}, {self.radius})"
    
    def __str__(self): 
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"
