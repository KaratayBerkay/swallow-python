from .init import f, y
# Using eval to stop PyLance since this environment is python 3.15

f(eval("*x for x in y"))
f(eval("(*x for x in y)"))
