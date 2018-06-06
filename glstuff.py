from OpenGL.GL import *
from OpenGL.GLU import *

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def touchingRect(self, coords: Vector3, size: Vector3):
        if (coords.x - size.x) == self.x or (coords.y - size.y) == self.y or (coords.z - size.z) == self.z or (coords.x + size.x) == self.x or (coords.y + size.y) == self.y or (coords.z + size.z) == self.z:
            return True
        return False

class ColorCube:
    def __init__(self, size, colors, coords: Vector3):
        self.vertices = 
