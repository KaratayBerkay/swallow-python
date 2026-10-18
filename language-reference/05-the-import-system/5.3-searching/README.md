## 5.3. Searching

To begin the search, Python needs the fully qualified name of the module (or package, but for the purposes of this discussion, the difference is immaterial) being imported. This name may come from various arguments to the `import` statement, or from the parameters to the `importlib.import_module()` or `__import__()` functions.

This name will be used in various phases of the import search, and it may be the dotted path to a submodule, e.g. `foo.bar.baz`. In this case, Python first tries to import `foo`, then `foo.bar`, and finally `foo.bar.baz`. If any of the intermediate imports fail, a `ModuleNotFoundError` is raised.

### Sections

- [5.3.1. The module cache](5.3.1-the-module-cache/README.md)
- [5.3.2. Finders and loaders](5.3.2-finders-and-loaders/README.md)
- [5.3.3. Import hooks](5.3.3-import-hooks/README.md)
- [5.3.4. The meta path](5.3.4-the-meta-path/README.md)
