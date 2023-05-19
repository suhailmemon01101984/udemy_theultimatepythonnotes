#Example 3: Rectangle


'''

This code demonstrates the creation of a Rectangle class in Python. 
The Rectangle class has three methods: __init__(), area(), perimeter(), and __str__().

The __init__() method is a constructor that initializes a new Rectangle object with a width and a height. 
The width and height are assigned to instance variables using the self keyword.

The area() method calculates and returns the area of the rectangle, which is equal to width * height.

The perimeter() method calculates and returns the perimeter of the rectangle, which is equal to 2 * (width + height).

The __str__() method returns a string representation of the rectangle, which is used when the object is printed. 
This method returns a string that describes the Rectangle object, including its width and height attributes.

In the example code, a new Rectangle object r1 is created with a width of 5 and a height of 10. 
The area(), perimeter(), and __str__() methods are then called on the r1 object and the output is printed to the console.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height}"


# Create a new rectangle
r1 = Rectangle(5, 10)
print(r1.area())  # Output: 50
print(r1.perimeter())  # Output: 30
print(r1)  # Output: Rectangle with width 5 and height 10
'''

# define a class rectangle that takes in 2 parameters: width and height
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # add functions to the class that calculate the area and the perimeter
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# create an object of the class rectangle with height as 34 and width as 15
rect = Rectangle(15, 34)

# print the area and the perimeter of this rectangle
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())