# 5. The import system

Python code in one module gains access to the code in another module by the process of importing it. The `import` statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as `importlib.import_module()` and built-in `__import__()` can also be used to invoke the import machinery.

The `import` statement combines two operations; it searches for the named module, then it binds the results of that search to a name in the local scope. The search operation of the `import` statement is defined as a call to the `__import__()` function, with the appropriate arguments. The return value of `__import__()` is used to perform the name binding operation of the `import` statement. See the `import` statement for the exact details of that name binding operation.

A direct call to `__import__()` performs only the module search and, if found, the module creation operation. While certain side-effects may occur, such as the importing of parent packages, and the updating of various caches (including `sys.modules`), only the `import` statement performs a name binding operation.

When an `import` statement is executed, the standard builtin `__import__()` function is called. Other mechanisms for invoking the import system (such as `importlib.import_module()`) may choose to bypass `__import__()` and use their own solutions to implement import semantics.

When a module is first imported, Python searches for the module and if found, it creates a module object (See `types.ModuleType`.), initializing it. If the named module cannot be found, a `ModuleNotFoundError` is raised. Python implements various strategies to search for the named module when the import machinery is invoked. These strategies can be modified and extended by using various hooks described in the sections below.

Changed in version 3.3: The import system has been updated to fully implement the second phase of [**PEP 302**](https://peps.python.org/pep-0302/). There is no longer any implicit import machinery - the full import system is exposed through `sys.meta_path`. In addition, native namespace package support has been implemented (see [**PEP 420**](https://peps.python.org/pep-0420/)).

## Sections

- [5.1. `importlib`](5.1-importlib/README.md)
- [5.2. Packages](5.2-packages/README.md)
- [5.3. Searching](5.3-searching/README.md)
- [5.4. Loading](5.4-loading/README.md)
- [5.5. The Path Based Finder](5.5-the-path-based-finder/README.md)
- [5.6. Replacing the standard import system](5.6-replacing-the-standard-import-system/README.md)
- [5.7. Package Relative Imports](5.7-package-relative-imports/README.md)
- [5.8. Special considerations for \_\_main\_\_](5.8-special-considerations-for-main/README.md)
- [5.9. References](5.9-references/README.md)
