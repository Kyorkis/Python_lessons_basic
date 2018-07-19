# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#import math 
#class Treyg():
#    def __init__(self,A,B,C):
#        self.A = A
#        self.B = B
#        self.C = C
        
#    def sidelen(x, y):
#        return math.sqrt((x[0]-y[0])**2 +(x[1]-y[1])**2)
        
#        self.AB = sidelen(self.A , self.B)
#        self.BC = sidelen(self.B , self.C)
#        self.AC = sidelen(self.C , self.A)

#treugolnik1 = Treyg((3, 2), (6, 7), (0, 12))
#print (treugolnik1.sidelen())

#import math

#class Triangle:
#    def __init__(self, A, B, C):
        # Функция вычисляет длину стороны согласно координатам точек
#        def sideLen(dot1, dot2):
#            return math.sqrt((dot1[0] - dot2[0]) ** 2
#                             + (dot1[1] - dot2[1]) ** 2)
 
#        self.A = A
#        self.B = B
#        self.C = C
        # На основании соседних координат вычисляем длину стороны AB
#        self.AB = sideLen(self.A, self.B)
#        self.BC = sideLen(self.B, self.C)
#        self.CA = sideLen(self.C, self.A)
 
    # Вычисление площади треугольника по формуле Герона
#    def areaTriangle(self):
#        semi_perimeter = self.perimeterTriangle() / 2
 
#        return math.sqrt(semi_perimeter
#                         * (semi_perimeter - self.AB)
#                         * (semi_perimeter - self.BC)
#                         * (semi_perimeter - self.CA))
 
    # вычисляем периметр треугольника
#    def perimeterTriangle(self):
#        return self.AB + self.BC + self.CA
 
    # Вычисляем высоту треугольника
#    def heightTriangle(self):
#        return self.areaTriangle() / (self.AB / 2)
 
 
#treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))
 
#print(treugolnik1.areaTriangle())
#print(treugolnik1.heightTriangle())
#print(treugolnik1.perimeterTriangle())
    
        

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
import math
class Trapeze:
    def __init__(self, A, B, C, D):
        
        def sideLen(dot1, dot2):
            return math.sqrt((dot1[0] - dot2[0]) ** 2
                             + (dot1[1] - dot2[1]) ** 2)
 
        def areaTriangle(len1, len2, len3):
            semi_perimeter = (len1 + len2 + len3) / 2
 
            return math.sqrt(semi_perimeter
                             * (semi_perimeter - len1)
                             * (semi_perimeter - len2)
                             * (semi_perimeter - len3))
 
        self.A = A
        self.B = B
        self.C = C
        self.D = D
 
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CD = sideLen(self.C, self.D)
        self.DA = sideLen(self.D, self.A)
        self.diagonal_AC = sideLen(self.C, self.A)
        self.diagonal_BD = sideLen(self.B, self.D)
        self.perimeter = self.AB + self.BC + self.CD + self.DA
 
       
        self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) \
                    + areaTriangle(self.diagonal_BD, self.BC, self.CD)
 
    def isTrapezeEqu(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False
x = Trapeze((1,5), (55,10), (54,76), (43,78))
print(x.isTrapezeEqu())