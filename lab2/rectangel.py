class rectangel:
    def __init__(self,x,y,width, height):
        if type(width) not in [int, float]: 
            raise TypeError("Width must be a number.")
        if type(height) not in [int, float]: 
            raise TypeError("Height must be a number.")
        if width <= 0:
            raise ValueError("Width must be positive.")
        if height <= 0:
            raise ValueError("Height must be positive.")
        self.width = width 
        self.y = y
        self.x = x
        self.height = height

    @property # read only property
    def area(self):
        return self.width * self.height
    
    @property # read only property
    def perimeter(self):
        return 2 * (self.width + self.height)
    

    def translate(self, dx, dy):
        if type(dx) not in [int, float] or type(dy) not in [int, float]:
            raise TypeError("dx and dy must be numbers")
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        if not isinstance(other, rectangel): return False
        return self.width == other.width and self.height == other.height
    
    def __gt__(self,other):
        if not isinstance(other, rectangel): return False
        return self.width * self.height > other.width * other.height
    
    def __lt__(self,other):
        if not isinstance(other, rectangel): return False
        return self.width * self.height < other.width * other.height
    
    def __le__(self,other):
        if not isinstance(other, rectangel): return False
        return self.width * self.height <= other.width * other.height
    
    def __ge__(self,other):
        if not isinstance(other, rectangel): return False
        return self.width * self.height >= other.width * other.height
    
    def __repr__(self):
        return f"rectangel({self.x}, {self.y}, {self.width}, {self.height})"
    
    def __str__(self):
        return f"rectangel with top-left corner at ({self.x}, {self.y}), width {self.width} and height {self.height}"
    
    def is_square(self):
        return self.width == self.height