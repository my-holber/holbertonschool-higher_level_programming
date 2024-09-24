#!/usr/bin/python3
"""
    Class file for Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class inherits from BaseGeometry. """
    def __init__(self, width, height):
        """
            Initialization of Rectangle.
            Arguments:
                width (int): Width of the rectangle.
                height (int): Height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """ Returns the area of the rectangle. """
        return self.__width * self.__height

    def __str__(self):
        """ Returns the string representation of the rectangle. """
        return f"[Rectangle] {self.__width}/{self.__height}"


# Example usage
r = Rectangle(3, 5)

print(r)         # Output: [Rectangle] 3/5
print(r.area())  # Output: 15
