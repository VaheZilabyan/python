import math

class Shape:
    def draw(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass

    def get_sizes(self):
        pass

class Circle(Shape):
    def __init__(self, r=1):
        self.__r = r

    def draw(self):
        print("Draw a circle")

    def area(self):
        return math.pow(self.__r, 2) * math.pi

    def perimeter(self):
        return 2 * self.__r * math.pi

    def get_sizes(self):
        return [self.__r]

class Triangle(Shape):
    def __init__(self, a=1, b=1, c=1):
        self.__a = a
        self.__b = b
        self.__c = c

    def draw(self):
        print("Draw a triangle")

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return math.sqrt(s * (self.__a) * (self.__b) * (self.__c))

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def get_sizes(self):
        return [self.__a, self.__b, self.__c]

class Rectangle(Shape):
    def __init__(self, height=1, width=1):
        self.__height = height
        self.__width = width

    def draw(self):
        print("Draw a rectangle")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return 2 * self.__height + 2 * self.__width

    def get_sizes(self):
        return [self.__height, self.__width]

class ShapeManager:
    def __init__(self):
        self.shapes = []

    def create_circle(self, r):
        self.shapes.append(Circle(r))

    def create_triangle(self, a, b, c):
        self.shapes.append(Triangle(a, b, c))

    def create_rectangle(self, height, width):
        self.shapes.append(Rectangle(height, width))

    def display_shapes(self):
        for shp in self.shapes:
            shp.draw()
            print("--sizes: ", shp.get_sizes())
            print("--area:  ", shp.area())
            print("--perimeter: ", shp.perimeter())
            print('\n')

shape_manager = ShapeManager()

while True:
    print("Options:")
    print("1. Create a circle")
    print("2. Create a triangle")
    print("3. Create a rectangle")
    print("4. Display shapes")
    print("5. Quit")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        try:
            r = float(input("Enter the radius of the circle: "))
            shape_manager.create_circle(r)
        except ValueError:
            print("Invalid input. Please enter a valid number for the radius.")
    elif choice == "2":
        try:
            a = float(input("Enter the length of side a: "))
            b = float(input("Enter the length of side b: "))
            c = float(input("Enter the length of side c: "))
            shape_manager.create_triangle(a, b, c)
        except ValueError:
            print("Invalid input. Please enter valid numbers for the sides.")
    elif choice == "3":
        try:
            height = float(input("Enter the height of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            shape_manager.create_rectangle(height, width)
        except ValueError:
            print("Invalid input. Please enter valid numbers for the dimensions.")
    elif choice == "4":
        shape_manager.display_shapes()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")