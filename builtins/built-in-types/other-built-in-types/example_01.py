class C:
    def method(self):
        pass
c = C()
c.method.whoami = 'my name is method'  # can't set on the method
c.method.__func__.whoami = 'my name is method'
print(repr(c.method.whoami))
