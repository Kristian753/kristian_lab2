class rectangel:
    def __init__(self,x,y,width, height):
        # Kontrollerar att width är ett nummer
        if type(width) not in [int, float]: 
            raise TypeError("Width must be a number.")
        # Kontrollerar att height är ett nummer
        if type(height) not in [int, float]: 
            raise TypeError("Height must be a number.")
        # Kontrollerar att width är positivt
        if width <= 0:
            raise ValueError("Width must be positive.")
        # Kontrollerar att height är positivt
        if height <= 0:
            raise ValueError("Height must be positive.")
        self.width = width 
        self.y = y
        self.x = x
        self.height = height

    @property # read only property
    def area(self):
        # Beräknar rektangelns area
        return self.width * self.height
    
    @property # read only property
    def perimeter(self):
        # Beräknar rektangelns omkrets
        return 2 * (self.width + self.height)
    

    def translate(self, dx, dy):
        # Kontrollerar att dx och dy är nummer
        if type(dx) not in [int, float] or type(dy) not in [int, float]:
            raise TypeError("dx and dy must be numbers")
        # Flyttar rektangelns x-position
        self.x += dx
        # Flyttar rektangelns y-position
        self.y += dy

    def __eq__(self, other):
        # Jämför om två rektanglar har samma mått
        if not isinstance(other, rectangel): return False
        return self.width == other.width and self.height == other.height