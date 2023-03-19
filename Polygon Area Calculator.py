class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.height = height
        return height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal 
    
    def get_picture(self):
        picture = ('*' * self.width + '\n') * self.height
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            return picture
        
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)
    
    def __str__(self):
        return f'Square(side={self.width})'