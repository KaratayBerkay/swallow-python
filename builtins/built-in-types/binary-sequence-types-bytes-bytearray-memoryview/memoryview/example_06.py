from ctypes import BigEndianStructure, c_long
class BEPoint(BigEndianStructure):
    _fields_ = [("x", c_long), ("y", c_long)]
point = BEPoint(100, 200)
a = memoryview(point)
b = memoryview(point)
print(repr(a == point))
print(repr(a == b))
