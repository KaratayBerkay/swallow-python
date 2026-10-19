The C API documentation uses the following levels to describe the thread
safety guarantees of each function. The levels are listed from least to
most safe.

### Incompatible

A function or operation that cannot be made safe for concurrent use even
with external synchronization. Incompatible code typically accesses
global state in an unsynchronized way and must only be called from a single
thread throughout the program's lifetime.

Example: a function that modifies process-wide state such as signal handlers
or environment variables, where concurrent calls from any threads, even with
external locking, can conflict with the runtime or other libraries.

### Compatible

A function or operation that is safe to call from multiple threads
*provided* the caller supplies appropriate external synchronization, for
example by holding a [lock](https://docs.python.org/3.15/glossary.html#term-lock) for the duration of each call. Without
such synchronization, concurrent calls may produce [race conditions](https://docs.python.org/3.15/glossary.html#term-race-condition) or [data races](https://docs.python.org/3.15/glossary.html#term-data-race).

Example: a function that reads from or writes to an object whose internal
state is not protected by a lock. Callers must ensure that no two threads
access the same object at the same time.

### Safe on distinct objects

A function or operation that is safe to call from multiple threads without
external synchronization, as long as each thread operates on a **different**
object. Two threads may call the function at the same time, but they must
not pass the same object (or objects that share underlying state) as
arguments.

Example: a function that modifies fields of a struct using non-atomic
writes. Two threads can each call the function on their own struct
instance safely, but concurrent calls on the *same* instance require
external synchronization.

### Safe on shared objects

A function or operation that is safe for concurrent use on the **same**
object. The implementation uses internal synchronization (such as
[per-object locks](https://docs.python.org/3.15/glossary.html#term-per-object-lock) or
[critical sections](https://docs.python.org/3.15/c-api/synchronization.html#python-critical-section-api)) to protect shared
mutable state, so callers do not need to supply their own locking.

Example: [PyList_GetItemRef()](https://docs.python.org/3.15/c-api/list.html#c.PyList_GetItemRef) can be called from multiple threads on the
same [PyListObject](https://docs.python.org/3.15/c-api/list.html#c.PyListObject) - it uses internal synchronization to serialize
access.

### Atomic

A function or operation that appears [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation) with
respect to other threads - it executes instantaneously from the perspective
of other threads. This is the strongest form of thread safety.

Example: [PyMutex_IsLocked()](https://docs.python.org/3.15/c-api/synchronization.html#c.PyMutex_IsLocked) performs an atomic read of the mutex
state and can be called from any thread at any time.
