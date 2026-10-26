import math


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __rmul__(self, k):
        return self * k

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def normalized(self):
        length = abs(self)
        if length == 0:
            raise ValueError("нулевой вектор нельзя нормализовать")
        return Vector(self.x / length, self.y / length, self.z / length)

    def angle(self, other):
        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("угол с нулевым вектором не определён")
        cos = self.dot(other) / (abs(self) * abs(other))
        cos = max(-1.0, min(1.0, cos))  # защита от погрешности float
        return math.acos(cos)

    def is_orthogonal(self, other):
        return abs(self.dot(other)) < 1e-9

    def is_collinear(self, other):
        c = self.cross(other)
        return abs(c.x) < 1e-9 and abs(c.y) < 1e-9 and abs(c.z) < 1e-9


def triangle_area(a, b, c):
    ab = b - a
    ac = c - a
    return 0.5 * abs(ab.cross(ac))


def volume(a, b, c):
    return abs(a.dot(b.cross(c)))
