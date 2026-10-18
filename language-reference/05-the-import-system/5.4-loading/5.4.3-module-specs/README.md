### 5.4.3. Module specs

The import machinery uses a variety of information about each module during import, especially before loading. Most of the information is common to all modules. The purpose of a module's spec is to encapsulate this import-related information on a per-module basis.

Using a spec during import allows state to be transferred between import system components, e.g. between the finder that creates the module spec and the loader that executes it. Most importantly, it allows the import machinery to perform the boilerplate operations of loading, whereas without a module spec the loader had that responsibility.

The module's spec is exposed as `module.__spec__`. Setting `__spec__` appropriately applies equally to modules initialized during interpreter startup. The one exception is `__main__`, where `__spec__` is set to None in some cases.

See `ModuleSpec` for details on the contents of the module spec.

Added in version 3.4.
