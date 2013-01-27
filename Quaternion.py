import copy
import math
from Vector import Vector


class Quaternion(object):
    def __init__(self, *args):
        if len(args) == 0:
            self.scalar = 0.0
            self.vector = Vector(0.0, 0.0, 0.0)
        else:
            self.scalar = args[0]
            if args[1] is Vector:
                self.vector = copy.deepcopy(args[1])
            else:
                self.vector = Vector(args[1], args[2], args[3])

    # Properties: W, X, Y, Z
    def __GetW(self):
        return self.scalar

    def __SetW(self, value):
        self.scalar = value

    w = property(fget=__GetW, fset=__SetW, doc="what?")

    def __GetX(self):
        return self.vector.x

    def __SetX(self, value):
        self.vector.x = value

    x = property(fget=__GetX, fset=__SetX, doc="what?")

    def __GetY(self):
        return self.vector.y

    def __SetY(self, value):
        self.vector.y = value

    y = property(fget=__GetY, fset=__SetY, doc="what?")

    def __GetZ(self):
        return self.vector.z

    def __SetZ(self, value):
        self.vector.z = value

    z = property(fget=__GetZ, fset=__SetZ, doc="what?")

    def __mul__(self, other):
        if type(other) is not Quaternion:
            raise Exception("Unsupported Operation")
        else:
            result = Quaternion()
            result.w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            result.x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            result.y = self.w * other.y + self.y * other.w + self.z * other.x - self.x * other.z
            result.z = self.w * other.z + self.z * other.w + self.x * other.y - self.y * other.x
            return result

    def Length(self):
        return math.sqrt(self.w * self.w + self.x * self.x + self.y * self.y + self.z * self.z)

    def out(self):
        print "W = " + str(self.scalar) + ", Vector = " + str(self.vector)

    def Normalized(self):

        if self.Length() == 0:
            return Quaternion(1.0, 0.0, 0.0, 0.0)
        else:
            temp = copy.deepcopy(self)
            length = self.Length()
            temp.w /= length
            temp.x /= length
            temp.y /= length
            temp.z /= length

            return temp

    def Normalize(self):
        self = self.Normalized()

    def Conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

if __name__ == "__main__":
    p1 = Quaternion(0.0, 1.0, 0.0, 0.0)
    q = Quaternion(.7071, 0.0, 0.0, 0.7071)
    q.out()
    (p1 * q).out()
    p2 = q * p1 * q.Conjugate()
    p2.out()
    print str([4.0, 2.1])
