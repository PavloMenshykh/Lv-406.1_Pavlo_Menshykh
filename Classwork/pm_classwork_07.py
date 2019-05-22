#Створити батьківський клас Figure з методами init: ініціалізується колір, 
#                                                                                         get_color: повертає колір фігури,
#                                                                                          info: надає інформацію про фігуру та колір,  
#від якого наслідуються такі класи як Rectangle, Square, які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.


class Figure:
    def __init__(self, color, ftype):
        self.get_color ="Figure color is %s" % color
        self.info = "Figure is a %s, color is %s" % (ftype, color)
    
    def get_color(self, color):
        self.get_color = color

    def info(self, color, ftype):
        self.info = color, ftype

class Rectangle(Figure):
    def __init__(self, color, a, b):
        Figure.__init__(self, color, "rectangle")
        self.square = "Figure area is %s" % str(a*b)

class Square(Figure):
    def __init__(self, color, a):
        Figure.__init__(self, color, "square")
        self.square = "Figure area is %s" % str(a**2)
    

fig2 = Square("red", 3)
fig3 = Rectangle("red", 3, 5)
print(fig3.square)
print(fig2.square)
print(fig2.get_color)
print(fig2.info)