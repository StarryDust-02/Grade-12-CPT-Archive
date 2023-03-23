import math
import operator as opr

cos = math.cos
sin = math.sin

class objVector(object):
    '''The most basic object of all spirite
    Includes x and y vectors and caculating methods
    '''

    def __init__(self, x, y=None):

        self.__vector = []
        try:
            if y == None:
                self.__vector = [x[0], x[1]]
            else:
                self.__vector = [x, y]
        except:
            self.__vector.append(x[0])
            self.__vector.append(x[1])
        
    def __getx(self):
        return self.__vector[0]
    def __setx(self, newvalue):
        self.__vector[0] = newvalue
    def delx(self):
        self.__vector[0] = 0
    x = property(__getx, __setx, delx, 'The property of vector on x axis')

    def __gety(self):
        return self.__vector[1]
    def __sety(self, newvalue):
        self.__vector[1] = newvalue
    def dely(self):
        self.__vector[1] = 0
    y = property(__gety, __sety, dely, 'The property of vector on y axis')

    def __setboth(self, x, y):
        self.__vector[0] = x
        self.__vector[1] = y

    #operations
    def __operationIn2V(self, other, operation) -> object:
        '''operation between self vectors and other vectors
            Args:
                other -> list or float
                operation -> opertaion module object
            Returns -> object:
                objVector object
        '''
        try:
            return objVector(operation(self.__vector[0], other[0]), operation(self.__vector[1], other[1]))

        except TypeError:
            return objVector(operation(self.__vector[0], other), operation(self.__vector[1], other))
    
    def __operationIn2VR(self, other, operation) -> object:
        '''operation between other vectors and self vectors
            Args:
                other -> list or float
                operation -> opertaion module object
            Returns -> object:
                objVector object
        '''
        try:
            return objVector(operation(other[0], self.__vector[0]), operation(other[1], self.__vector[1]))

        except TypeError:
            return objVector(operation(other, self.__vector[0]), operation(other, self.__vector[1]))

    def operationself(self, operation) -> object:
        '''operation takes on self vections
            Args:
                operation -> opertaion module object
            Returns -> object:
                objVector object
        '''
        return objVector(operation(self.__vector[0]), operation(self.__vector[1]))
    
    #quick inbuild methods: caculations
    def __str__(self):#str
        return f'[{self.__vector[0]}, {self.__vector[1]}]'
    def __getitem__(self, key) -> float:#get
        return self.__vector[key]
    def __setitem__(self, key, value):#set
        self.__vector[key] = value
    def __eq__(self, other) -> bool:#equal
        return self.__vector[0] == other[0] and self.__vector[1] == other[1]
    def __ne__(self, other) -> bool:#not equal
        return self.__vector[0] == other[0] and self.__vector[1] == other[1]       
    def __add__(self, other):#add
        return self.__operationIn2V(other, opr.add)
    def __sub__(self, other):#sub
        return self.__operationIn2V(other, opr.sub)
    def __rsub__(self, other):#reversed sub
        return self.__operationIn2VR(other, opr.sub)
    def __mul__(self, other):#mutiply
        return self.__operationIn2V(other, opr.mul)
    def __div__(self, other):#divide
        return self.__operationIn2V(other, opr.div)
    def __rdiv__(self, other):#reversed divide
        return self.__operationIn2V(other, opr.div)
    def __floordiv__(self, other):#floor divide
        return self.__operationIn2V(other, opr.floordiv)
    def __rfloordiv__(self, other):#reversed floor divide
        return self.__operationIn2V(other, opr.floordiv)
    def __truediv__(self, other):#true divide
        return self.__operationIn2V(other, opr.truediv)
    def __rtruediv__(self, other):#reversed true divide
        return self.__operationIn2V(other, opr.truediv)
    __radd__ = __add__
    __rmul__ = __mul__

    #advance vector methods
    def dot_product(self, other):#dot production
        return self.__vector[0] * other[0] + self.__vector[1] * other[1]

    def __get_norm(self):
        return math.sqrt(self.__vector[0]**2 + self.__vector[1]**2)
    def __set_norm(self, value):
        norm =self.__get_norm()
        if norm != 0:
            self.__vector[0] = self.__vector[0]*value/norm
            self.__vector[1] = self.__vector[1]*value/norm
    norm = property(__get_norm, __set_norm, 'Norm of vectors')


    def __get_angle(self, cx=0 ,cy=0):
        if self.__vector[0] == 0 and self.__vector[1] == 0:
            return 0
        x = self.__vector[0]
        y = self.__vector[1]
        a = [x - cx, y - cy]
        b = [0, -1]
        dotProduct = a[0] * b[0] + a[1] * b[1]
        d = math.sqrt(a[0] * a[0] + a[1] * a[1]) * math.sqrt(b[0] * b[0] + b[1] * b[1])
        radian = dotProduct/d
        angle = math.acos(radian) * 180 / math.pi 
        if x < cx:
            return angle
        else:
            return -1*angle
        
    def __set_angle(self, value):
        self.__vector[1] = -self.__get_norm()
        self.__vector[0] = 0
        
        value = math.radians(value)
        x = self.__vector[0] * cos(value) - self.__vector[1] * sin(value)
        y = self.__vector[0] * sin(value) + self.__vector[1] * cos(value)
        
        self.__vector[0] = -x
        self.__vector[1] = y
    angle = property(__get_angle, __set_angle, None, 'Gets or sets the magnitude of a Vector')

    def rotate(self, angle):
        radian = math.radians(angle)
        x = self.__vector[0] * cos(radian) - self.__vector[1] * sin(radian)
        y = self.__vector[0] * sin(radian) + self.__vector[1] * cos(radian)
        self.__vector = [-x, y]


    def perpendicular(self):
        return objVector(-self.__vector[1], self.__vector[0])

    def copy(self):
        return objVector(self.__vector[0], self.__vector[1])
