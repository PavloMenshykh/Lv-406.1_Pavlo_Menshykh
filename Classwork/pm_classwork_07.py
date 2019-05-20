#Створити батьківський клас Figure з методами init: ініціалізується колір, get_color: повертає колір фігури, info: надає інформацію про фігуру та колір,  
#від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.

class Figure:
    def __init__(self, get_color, type):
        self.color = get_color
        i = 1 if type == rect else 2
        self.sides = i

    def inputs(self):
        self.sides = [float(input("Enter side"+str(i)+" :\n"))]

class Rectangle(Figure):
    def __init__(self):
        pass

class Square(Figure):
    def __init__(self):
        pass

"""
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side“ + str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)  #super().__init__(3) 

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The square of the triangle is %0.2f' %area)

>>> t = Triangle()

>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4

>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0

>>> t.findArea()
The square of the triangle is 6.00
"""