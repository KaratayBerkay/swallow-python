class MyGroup(ExceptionGroup):
    def derive(self, excs):
        return MyGroup(self.message, excs)
e = MyGroup("eg", [ValueError(1), TypeError(2)])
e.add_note("a note")
e.__context__ = Exception("context")
e.__cause__ = Exception("cause")
try:
   raise e
except Exception as e:
   exc = e
match, rest = exc.split(ValueError)
print(repr((exc, exc.__context__, exc.__cause__, exc.__notes__)))
print(repr((match, match.__context__, match.__cause__, match.__notes__)))
print(repr((rest, rest.__context__, rest.__cause__, rest.__notes__)))
print(repr(exc.__traceback__ is match.__traceback__ is rest.__traceback__))
