import math
import copy


class Vector(list):
    """ Vector.py
        6/24/2009 by Travis Jones
        simple list-based vector class
        Notes:
            - Inspired by http://code.activestate.com/recipes/52272/
            - Supports 2D and 3D vectors
            - Constructor takes either a tuple or a list
            - Has properties x, y and z for ease of use
            - Allows for Vector add/mul with a scalar or another Vector
    """
    def __init__(self, *vec):
        if len(vec) == 0:
            super(Vector, self).__init__([0.0, 0.0, 0.0])
        else:
            if type(vec[0]) is list:
                super(Vector, self).__init__(vec[0])
            else:
                if type(vec) is tuple:
                    super(Vector, self).__init__([i for i in vec])

    def __add__(self, other):
        if type(other) is list or type(other) is Vector:
            return Vector(map(lambda x, y: x + y, self, other))
        else:
            return Vector([self[i] + other for i in range(len(self))])

    def __sub__(self, other):
        if type(other) is list or type(other) is Vector:
            return Vector(map(lambda x, y: x - y, self, other))
        else:
            return Vector([self[i] + other for i in range(len(self))])

    def __mul__(self, other):
        if type(other) is list or type(other) is Vector:
            return Vector(map(lambda x, y: x * y, self, other))
        else:
            return Vector([self[i] * other for i in range(len(self))])

    # Properties of X, Y, Z for convenience
    def __GetX(self):
        return self[0]

    def __SetX(self, value):
        self[0] = value

    x = property(fget=__GetX, fset=__SetX, doc="what?")

    def __GetY(self):
        return self[1]

    def __SetY(self, value):
        self[1] = value

    y = property(fget=__GetY, fset=__SetY, doc="what?")

    def __GetZ(self):
        return self[2]

    def __SetZ(self, value):
        self[2] = value

    z = property(fget=__GetZ, fset=__SetZ, doc="what?")

    def out(self):
        print self

    def Normalized(self):
        if len(self) > 3 or len(self) < 2:
            raise Exception("Normalization not supported on this Vector")

        temp = copy.deepcopy(self)

        if len(self) == 2:
            length = math.sqrt(temp[0] * temp[0] + temp[1] * temp[1])
            temp[0] /= length
            temp[1] /= length
        else:
            length = math.sqrt(temp[0] * temp[0] + temp[1] * temp[1] + temp[2] * temp[2])
            temp[0] /= length
            temp[1] /= length
            temp[2] /= length

        return temp

    def Normalize(self):
        n = self.Normalized()
        for i in range(len(n)):
            self[i] = n[i]


if __name__ == "__main__":

    a = Vector()

    a = Vector([2.0, 2.0, 2.0])
    a.x = 4.0

    b = a * Vector(3, 3, 3)
    c = Vector(2.0, 2.0)
    d = Vector(9.0, 7.0)
    dist = d - c
    print dist

    dist.Normalize()
    print dist
    print c + dist
