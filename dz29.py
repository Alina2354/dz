import math

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("только вектора")

    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("только вектора")

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            raise TypeError("только число")

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __eq__(self, other):

        if isinstance(other, Vector3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

if __name__ == '__main__':
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)


    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")

    