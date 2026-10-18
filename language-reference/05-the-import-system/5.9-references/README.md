## 5.9. References

The import machinery has evolved considerably since Python's early days. The original [specification for packages](https://www.python.org/doc/essays/packages/) is still available to read, although some details have changed since the writing of that document.

The original specification for `sys.meta_path` was [**PEP 302**](https://peps.python.org/pep-0302/), with subsequent extension in [**PEP 420**](https://peps.python.org/pep-0420/).

[**PEP 420**](https://peps.python.org/pep-0420/) introduced namespace packages for Python 3.3. [**PEP 420**](https://peps.python.org/pep-0420/) also introduced the `find_loader()` protocol as an alternative to `find_module()`.

[**PEP 366**](https://peps.python.org/pep-0366/) describes the addition of the `__package__` attribute for explicit relative imports in main modules.

[**PEP 328**](https://peps.python.org/pep-0328/) introduced absolute and explicit relative imports and initially proposed `__name__` for semantics [**PEP 366**](https://peps.python.org/pep-0366/) would eventually specify for `__package__`.

[**PEP 338**](https://peps.python.org/pep-0338/) defines executing modules as scripts.

[**PEP 451**](https://peps.python.org/pep-0451/) adds the encapsulation of per-module import state in spec objects. It also off-loads most of the boilerplate responsibilities of loaders back onto the import machinery. These changes allow the deprecation of several APIs in the import system and also addition of new methods to finders and loaders.
