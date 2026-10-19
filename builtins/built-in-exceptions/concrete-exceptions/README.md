The following exceptions are the exceptions that are usually raised.

- [`AssertionError`](AssertionError/README.md) — Raised when an assert statement fails.
- [`AttributeError`](AttributeError/README.md) — Raised when an attribute reference (see Attribute references) or assignment fails.
- [`EOFError`](EOFError/README.md) — Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
- [`FloatingPointError`](FloatingPointError/README.md) — Not currently used.
- [`GeneratorExit`](GeneratorExit/README.md) — Raised when a generator or coroutine is closed; see generator.close() and coroutine.close().
- [`ImportError`](ImportError/README.md) — Raised when the import statement has troubles trying to load a module.
- [`ModuleNotFoundError`](ModuleNotFoundError/README.md) — A subclass of ImportError which is raised by import when a module could not be located.
- [`ImportCycleError`](ImportCycleError/README.md) — A subclass of ImportError which is raised when a lazy import fails because it (directly or indirectly) tries to import itself.
- [`IndexError`](IndexError/README.md) — Raised when a sequence subscript is out of range.
- [`KeyError`](KeyError/README.md) — Raised when a mapping (dictionary) key is not found in the set of existing keys.
- [`KeyboardInterrupt`](KeyboardInterrupt/README.md) — Raised when the user hits the interrupt key (normally Control-C or Delete).
- [`MemoryError`](MemoryError/README.md) — Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects).
- [`NameError`](NameError/README.md) — Raised when a local or global name is not found.
- [`NotImplementedError`](NotImplementedError/README.md) — This exception is derived from RuntimeError.
- [`OSError`](OSError/README.md) — This exception is raised when a system function returns a system-related error, including I/O failures such as "file not found" or "disk full"…
- [`OverflowError`](OverflowError/README.md) — Raised when the result of an arithmetic operation is too large to be represented.
- [`PythonFinalizationError`](PythonFinalizationError/README.md) — This exception is derived from RuntimeError.
- [`RecursionError`](RecursionError/README.md) — This exception is derived from RuntimeError.
- [`ReferenceError`](ReferenceError/README.md) — This exception is raised when a weak reference proxy, created by the weakref.proxy() function, is used to access an attribute of the referent…
- [`RuntimeError`](RuntimeError/README.md) — Raised when an error is detected that doesn't fall in any of the other categories.
- [`StopIteration`](StopIteration/README.md) — Raised by built-in function next() and an iterator's __next__() method to signal that there are no further items produced by the iterator.
- [`StopAsyncIteration`](StopAsyncIteration/README.md) — Must be raised by __anext__() method of an asynchronous iterator object to stop the iteration.
- [`SyntaxError`](SyntaxError/README.md) — Raised when the parser encounters a syntax error.
- [`IndentationError`](IndentationError/README.md) — Base class for syntax errors related to incorrect indentation.
- [`TabError`](TabError/README.md) — Raised when indentation contains an inconsistent use of tabs and spaces.
- [`SystemError`](SystemError/README.md) — Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope.
- [`SystemExit`](SystemExit/README.md) — This exception is raised by the sys.exit() function.
- [`TypeError`](TypeError/README.md) — Raised when an operation or function is applied to an object of inappropriate type.
- [`UnboundLocalError`](UnboundLocalError/README.md) — Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
- [`UnicodeError`](UnicodeError/README.md) — Raised when a Unicode-related encoding or decoding error occurs.
- [`UnicodeEncodeError`](UnicodeEncodeError/README.md) — Raised when a Unicode-related error occurs during encoding.
- [`UnicodeDecodeError`](UnicodeDecodeError/README.md) — Raised when a Unicode-related error occurs during decoding.
- [`UnicodeTranslateError`](UnicodeTranslateError/README.md) — Raised when a Unicode-related error occurs during translating.
- [`ValueError`](ValueError/README.md) — Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described…
- [`ZeroDivisionError`](ZeroDivisionError/README.md) — Raised when the second argument of a division or modulo operation is zero.

The following exceptions are kept for compatibility with previous versions;
starting from Python 3.3, they are aliases of [OSError](OSError/README.md).

- [`EnvironmentError`](EnvironmentError/README.md)
- [`IOError`](IOError/README.md)
- [`WindowsError`](WindowsError/README.md) — Only available on Windows.

## OS exceptions

The following exceptions are subclasses of [OSError](OSError/README.md), they get raised
depending on the system error code.

- [`BlockingIOError`](BlockingIOError/README.md) — Raised when an operation would block on an object (e.g. socket) set for non-blocking operation. Corresponds to errno EAGAIN, EALREADY, EWOULDBLOCK…
- [`ChildProcessError`](ChildProcessError/README.md) — Raised when an operation on a child process failed.
- [`ConnectionError`](ConnectionError/README.md) — A base class for connection-related issues.
- [`BrokenPipeError`](BrokenPipeError/README.md) — A subclass of ConnectionError, raised when trying to write on a pipe while the other end has been closed, or trying to write on a socket which has…
- [`ConnectionAbortedError`](ConnectionAbortedError/README.md) — A subclass of ConnectionError, raised when a connection attempt is aborted by the peer.
- [`ConnectionRefusedError`](ConnectionRefusedError/README.md) — A subclass of ConnectionError, raised when a connection attempt is refused by the peer.
- [`ConnectionResetError`](ConnectionResetError/README.md) — A subclass of ConnectionError, raised when a connection is reset by the peer.
- [`FileExistsError`](FileExistsError/README.md) — Raised when trying to create a file or directory which already exists.
- [`FileNotFoundError`](FileNotFoundError/README.md) — Raised when a file or directory is requested but doesn't exist.
- [`InterruptedError`](InterruptedError/README.md) — Raised when a system call is interrupted by an incoming signal.
- [`IsADirectoryError`](IsADirectoryError/README.md) — Raised when a file operation (such as os.remove()) is requested on a directory.
- [`NotADirectoryError`](NotADirectoryError/README.md) — Raised when a directory operation (such as os.listdir()) is requested on something which is not a directory.
- [`PermissionError`](PermissionError/README.md) — Raised when trying to run an operation without the adequate access rights - for example filesystem permissions.
- [`ProcessLookupError`](ProcessLookupError/README.md) — Raised when a given process doesn't exist.
- [`TimeoutError`](TimeoutError/README.md) — Raised when a system function timed out at the system level.

> *Added in version 3.3:* All the above [OSError](OSError/README.md) subclasses were added.

> **See also**
>
> [PEP 3151](https://peps.python.org/pep-3151/) - Reworking the OS and IO exception hierarchy
