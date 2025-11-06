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
