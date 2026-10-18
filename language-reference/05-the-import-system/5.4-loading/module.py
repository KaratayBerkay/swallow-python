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
