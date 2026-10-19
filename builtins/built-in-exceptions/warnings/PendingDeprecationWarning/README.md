## `PendingDeprecationWarning`

```
PendingDeprecationWarning
```

Base class for warnings about features which are obsolete and
expected to be deprecated in the future, but are not deprecated
at the moment.

This class is rarely used as emitting a warning about a possible
upcoming deprecation is unusual, and [DeprecationWarning](../DeprecationWarning/README.md)
is preferred for already active deprecations.

Ignored by the default warning filters. Enabling the `Python
Development Mode <devmode>` shows this warning.

The deprecation policy is described in [PEP 387](https://peps.python.org/pep-387/).
