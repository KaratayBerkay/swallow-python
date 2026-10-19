## `repr()`

```
repr(object, /)
```

Return a string containing a printable representation of an object.  For many
types, this function makes an attempt to return a string that would yield an
object with the same value when passed to [eval()](../eval/README.md); otherwise, the
representation is a string enclosed in angle brackets that contains the name
of the type of the object together with additional information often
including the name and address of the object.  A class can control what this
function returns for its instances
by defining a [__repr__()](https://docs.python.org/3.15/reference/datamodel.html#object.__repr__) method.
If [sys.displayhook()](https://docs.python.org/3.15/library/sys.html#sys.displayhook) is not accessible, this function will raise
[RuntimeError](https://docs.python.org/3.15/builtins/exceptions.html#RuntimeError).

This class has a custom representation that can be evaluated:

``` python
class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person({self.name!r}, {self.age!r})"
```
