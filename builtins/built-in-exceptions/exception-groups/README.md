The following are used when it is necessary to raise multiple unrelated
exceptions. They are part of the exception hierarchy so they can be
handled with `except` like all other exceptions. In addition,
they are recognised by `except*`, which matches
their subgroups based on the types of the contained exceptions.

- [`ExceptionGroup`](ExceptionGroup/README.md) — Both of these exception types wrap the exceptions in the sequence excs.
- [`BaseExceptionGroup`](BaseExceptionGroup/README.md) — Documented together with ExceptionGroup.
