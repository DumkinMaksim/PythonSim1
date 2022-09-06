# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


print('input coordinats')
x1=float(input('enter Xa-> '))
y1=float(input('enter Ya-> '))
x2=float(input('enter Xb-> '))
y2=float(input('enter Yb-> '))
# первый вариант
print('Расстояние между 2 точками в 2д пространстве = '+str(round(((x2-x1)**2+(y2-y1)**2)**0.5,4)))

# второй вариант
sqrt = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(sqrt)