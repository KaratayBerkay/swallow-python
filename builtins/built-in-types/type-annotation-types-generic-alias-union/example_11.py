class M(type):
    def __or__(self, other):
        return "Hello"
class C(metaclass=M):
    pass
print(repr(C | int))
print(repr(int | C))
