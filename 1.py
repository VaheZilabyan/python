from abc import ABC, abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def draw(self):
        return
    @abstractmethod
    def perimeter(self):
        return
    @abstractmethod
    def area(self):
        return
    @abstractmethod
    def get_sizes():
        return

class circle(shape):
    def __init__(self, r = 1) -> None:
        super().__init__()
        self.__r = r
    def get_sizes(self):
        return self.__r
    def draw(self):
        super().draw()
        print ("Draw a circle")
        return
    def area(self):
        super().draw()
        return math.pow(self.__r, 2) * math.pi
    def perimeter(self):
        return 2 * self.__r * math.pi

class triangle(shape):
    def __init__(self, a = 1, b = 1, c = 1) -> None:
        super().__init__()
        self.__a = a
        self.__b = b
        self.__c = c
    def get_sizes(self):
        super().draw()
        my_list = [self.__a, self.__b, self.__c]
        return my_list
    def draw(self):
        super().draw()
        print("Draw a triangle")
        return
    def area(self):
        super().draw()
        s = (self.__a + self.__b + self.__c)/2
        return math.sqrt(s*(self.__a)*(self.__b)*(self.__c))
    def perimeter(self):
        return self.__a + self.__b + self.__c

class rectangle(shape):
    def __init__(self, a = 1, b = 1) -> None:
        super().__init__()
        self.__heigh = a
        self.__width = b
    def get_sizes(self):
        super().draw()
        my_list = [self.__heigh, self.__width]
        return my_list
    def draw(self):
        super().draw()
        print ("Draw a rectangle")
        return
    def area(self):
        super().draw()
        return self.__heigh * self.__width
    def perimeter(self):
        return 2*self.__heigh + 2*self.__width

shapes = []

while(1):
    text = input()
    if text == "q" or text == "quit":
        break
    words = text.split()
    if words[0] != "create":
        print("Wrong input")
        continue
    if (words[1] == "circle" and len(words) == 3):
        try:
            r = float(words[2])
        except ValueError:
            print("You did not enter a number.")
            continue
        shapes.append(circle(float(words[2])))
    elif (words[1] == "triangle" and len(words) == 5):
        try:
            a = float(words[2])
            b = float(words[3])
            c = float(words[4])
        except ValueError:
            print("You did not enter a number.")
            continue
        shapes.append(triangle(float(words[2]), float(words[3]), float(words[4])))
    elif (words[1] == "rectangle" and len(words) == 4):
        try:
            a = float(words[2])
            b = float(words[3])
        except ValueError:
            print("You did not enter a number.")
            continue
        shapes.append(rectangle(float(words[2]), float(words[3])))
    else:
        print("Wrong input")
        continue

print('\n')
for shp in shapes:
    shp.draw()
    print("--sizes: ", shp.get_sizes())
    print("--area:  ", shp.area())
    print("--perimeter: ", shp.perimeter())
    print('\n')
   