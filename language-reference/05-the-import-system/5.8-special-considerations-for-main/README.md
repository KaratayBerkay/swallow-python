## 5.8. Special considerations for \_\_main\_\_

The `__main__` module is a special case relative to Python's import system. As noted elsewhere, the `__main__` module is directly initialized at interpreter startup, much like `sys` and `builtins`. However, unlike those two, it doesn't strictly qualify as a built-in module. This is because the manner in which `__main__` is initialized depends on the flags and other options with which the interpreter is invoked.

### Sections

- [5.8.1. \_\_main\_\_.\_\_spec\_\_](5.8.1-main-spec/README.md)
