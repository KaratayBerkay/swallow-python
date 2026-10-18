## 5.4. Loading

If and when a module spec is found, the import machinery will use it (and the loader it contains) when loading the module. Here is an approximation of what happens during the loading portion of import:

``` python
module = None
if spec.loader is not None and hasattr(spec.loader, 'create_module'):
    # It is assumed 'exec_module' will also be defined on the loader.
    module = spec.loader.create_module(spec)
if module is None:
    module = ModuleType(spec.name)
# The import-related module attributes get set here:
_init_module_attrs(spec, module)

if spec.loader is None:
    # unsupported
    raise ImportError

sys.modules[spec.name] = module
try:
    spec.loader.exec_module(module)
except BaseException:
    try:
        del sys.modules[spec.name]
    except KeyError:
        pass
    raise
return sys.modules[spec.name]
```
> Code: [module.py](module.py)

Note the following details:

- If there is an existing module object with the given name in `sys.modules`, import will have already returned it.

- The module will exist in `sys.modules` before the loader executes the module code. This is crucial because the module code may (directly or indirectly) import itself; adding it to `sys.modules` beforehand prevents unbounded recursion in the worst case and multiple loading in the best.

- If loading fails, the failing module -- and only the failing module -- gets removed from `sys.modules`. Any module already in the `sys.modules` cache, and any module that was successfully loaded as a side-effect, must remain in the cache. This contrasts with reloading where even the failing module is left in `sys.modules`.

- After the module is created but before execution, the import machinery sets the import-related module attributes ("\_init_module_attrs" in the pseudo-code example above), as summarized in a later section.

- Module execution is the key moment of loading in which the module's namespace gets populated. Execution is entirely delegated to the loader, which gets to decide what gets populated and how.

- The module created during loading and passed to exec_module() may not be the one returned at the end of import (The importlib implementation avoids using the return value directly. Instead, it gets the module object by looking the module name up in `sys.modules`. The indirect effect of this is that an imported module may replace itself in `sys.modules`. This is implementation-specific behavior that is not guaranteed to work in other Python implementations.) .

Changed in version 3.4: The import system has taken over the boilerplate responsibilities of loaders. These were previously performed by the `importlib.abc.Loader.load_module` method.

Changed in version 3.15: The `load_module` method is no longer used.

### Sections

- [5.4.1. Loaders](5.4.1-loaders/README.md)
- [5.4.2. Submodules](5.4.2-submodules/README.md)
- [5.4.3. Module specs](5.4.3-module-specs/README.md)
- [5.4.4. \_\_path\_\_ attributes on modules](5.4.4-path-attributes-on-modules/README.md)
- [5.4.5. Module reprs](5.4.5-module-reprs/README.md)
- [5.4.6. Cached bytecode invalidation](5.4.6-cached-bytecode-invalidation/README.md)
