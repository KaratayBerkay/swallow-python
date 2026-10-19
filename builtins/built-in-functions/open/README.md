## `open()`

```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

Open *file* and return a corresponding [file object](https://docs.python.org/3.15/glossary.html#term-file-object).  If the file
cannot be opened, an [OSError](https://docs.python.org/3.15/builtins/exceptions.html#OSError) is raised. See
[Reading and writing files](https://docs.python.org/3.15/tutorial/inputoutput.html#tut-files) for more examples of how to use this function.

*file* is a [path-like object](https://docs.python.org/3.15/glossary.html#term-path-like-object) giving the pathname (absolute or
relative to the current working directory) of the file to be opened or an
integer file descriptor of the file to be wrapped.  (If a file descriptor is
given, it is closed when the returned I/O object is closed unless *closefd*
is set to `False`.)

*mode* is an optional string that specifies the mode in which the file is
opened.  It defaults to `'r'` which means open for reading in text mode.
Other common values are `'w'` for writing (truncating the file if it
already exists), `'x'` for exclusive creation, and `'a'` for appending
(which on *some* Unix systems, means that *all* writes append to the end of
the file regardless of the current seek position).  In text mode, if
*encoding* is not specified, UTF-8 is used by default; if
[Python UTF-8 Mode](https://docs.python.org/3.15/library/os.html#utf8-mode) is disabled,
[locale.getencoding()](https://docs.python.org/3.15/library/locale.html#locale.getencoding) is called to get the current locale encoding.
(For reading and writing raw bytes use binary mode and leave
*encoding* unspecified.)  The available modes are:

| Character | Meaning |
| --- | --- |
| `'r'` | open for reading (default) |
| `'w'` | open for writing, truncating the file first |
| `'x'` | open for exclusive creation, failing if the file already exists |
| `'a'` | open for writing, appending to the end of file if it exists |
| `'b'` | binary mode |
| `'t'` | text mode (default) |
| `'+'` | open for updating (reading and writing) |

The default mode is `'r'` (open for reading text, a synonym of `'rt'`).
Modes `'w+'` and `'w+b'` open and truncate the file.  Modes `'r+'`
and `'r+b'` open the file with no truncation.

As mentioned in the [Overview](https://docs.python.org/3.15/library/io.html#io-overview), Python distinguishes between binary
and text I/O.  Files opened in binary mode (including `'b'` in the *mode*
argument) return contents as [bytes](../bytes/README.md) objects without any decoding.  In
text mode (the default, or when `'t'` is included in the *mode* argument),
the contents of the file are returned as [str](../str/README.md), the bytes having been
first decoded using the default encoding or using the specified
*encoding* if given.

> **Note**
>
> Python doesn't depend on the underlying operating system's notion of text
> files; all the processing is done by Python itself, and is therefore
> platform-independent.

*buffering* is an optional integer used to set the buffering policy.  Pass 0
to switch buffering off (only allowed in binary mode), 1 to select line
buffering (only usable when writing in text mode), and an integer > 1 to indicate the size
in bytes of a fixed-size chunk buffer. Note that specifying a buffer size this
way applies for binary buffered I/O, but `TextIOWrapper` (i.e., files opened
with `mode='r+'`) would have another buffering. To disable buffering in
`TextIOWrapper`, consider using the `write_through` flag for
`io.TextIOWrapper.reconfigure()`. When no *buffering* argument is
given, the default buffering policy works as follows:

- Binary files are buffered in fixed-size chunks; the size of the buffer
  is `max(min(blocksize, 8 MiB), DEFAULT_BUFFER_SIZE)`
  when the device block size is available.
  On most systems, the buffer will typically be 128 kilobytes long.

- "Interactive" text files (files for which [isatty()](https://docs.python.org/3.15/library/io.html#io.IOBase.isatty)
  returns `True`) use line buffering.  Other text files use the policy
  described above for binary files.

*encoding* is the name of the encoding used to decode or encode the file.
This should only be used in text mode.  The default encoding is UTF-8;
if [Python UTF-8 Mode](https://docs.python.org/3.15/library/os.html#utf8-mode) is disabled, the default is
platform-dependent (whatever [locale.getencoding()](https://docs.python.org/3.15/library/locale.html#locale.getencoding) returns).
Any [text encoding](https://docs.python.org/3.15/glossary.html#term-text-encoding) supported by Python can be used, and
`encoding="locale"` specifies the current locale encoding explicitly.
See the [codecs](https://docs.python.org/3.15/library/codecs.html#module-codecs) module for the list of supported encodings.

*errors* is an optional string that specifies how encoding and decoding
errors are to be handled—this cannot be used in binary mode.
A variety of standard error handlers are available,
though any error handling name that has been registered with
[codecs.register_error()](https://docs.python.org/3.15/library/codecs.html#codecs.register_error) is also valid.  The standard names
can be found in [Error Handlers](https://docs.python.org/3.15/library/codecs.html#error-handlers).

*newline* determines how to parse newline characters from the stream.
It can be `None`, `''`, `'\n'`, `'\r'`, and
`'\r\n'`.  It works as follows:

- When reading input from the stream, if *newline* is `None`, universal
  newlines mode is enabled.  Lines in the input can end in `'\n'`,
  `'\r'`, or `'\r\n'`, and these are translated into `'\n'` before
  being returned to the caller.  If it is `''`, universal newlines mode is
  enabled, but line endings are returned to the caller untranslated.  If it
  has any of the other legal values, input lines are only terminated by the
  given string, and the line ending is returned to the caller untranslated.

- When writing output to the stream, if *newline* is `None`, any `'\n'`
  characters written are translated to the system default line separator,
  [os.linesep](https://docs.python.org/3.15/library/os.html#os.linesep).  If *newline* is `''` or `'\n'`, no translation
  takes place.  If *newline* is any of the other legal values, any `'\n'`
  characters written are translated to the given string.

If *closefd* is `False` and a file descriptor rather than a filename was
given, the underlying file descriptor will be kept open when the file is
closed.  If a filename is given *closefd* must be `True` (the default);
otherwise, an error will be raised.

A custom opener can be used by passing a callable as *opener*. The underlying
file descriptor for the file object is then obtained by calling *opener* with
(*file*, *flags*). *opener* must return an open file descriptor (passing
`os.open` as *opener* results in functionality similar to passing
`None`).

The newly created file is [non-inheritable](https://docs.python.org/3.15/library/os.html#fd-inheritance).

The following example uses the [dir_fd](https://docs.python.org/3.15/library/os.html#dir-fd) parameter of the
[os.open()](https://docs.python.org/3.15/library/os.html#os.open) function to open a file relative to a given directory:

``` python
>>> import os
>>> dir_fd = os.open('somedir', os.O_RDONLY)
>>> def opener(path, flags):
...     return os.open(path, flags, dir_fd=dir_fd)
...
>>> with open('spamspam.txt', 'w', opener=opener) as f:
...     print('This will be written to somedir/spamspam.txt', file=f)
...
>>> os.close(dir_fd)  # don't leak a file descriptor
```
> Code: [example_01.py](example_01.py)

The type of [file object](https://docs.python.org/3.15/glossary.html#term-file-object) returned by the open() function
depends on the mode.  When open() is used to open a file in a text
mode (`'w'`, `'r'`, `'wt'`, `'rt'`, etc.), it returns a subclass of
[io.TextIOBase](https://docs.python.org/3.15/library/io.html#io.TextIOBase) (specifically [io.TextIOWrapper](https://docs.python.org/3.15/library/io.html#io.TextIOWrapper)).  When used
to open a file in a binary mode with buffering, the returned class is a
subclass of [io.BufferedIOBase](https://docs.python.org/3.15/library/io.html#io.BufferedIOBase).  The exact class varies: in read
binary mode, it returns an [io.BufferedReader](https://docs.python.org/3.15/library/io.html#io.BufferedReader); in write binary and
append binary modes, it returns an [io.BufferedWriter](https://docs.python.org/3.15/library/io.html#io.BufferedWriter), and in
read/write mode, it returns an [io.BufferedRandom](https://docs.python.org/3.15/library/io.html#io.BufferedRandom).  When buffering is
disabled, the raw stream, a subclass of [io.RawIOBase](https://docs.python.org/3.15/library/io.html#io.RawIOBase),
[io.FileIO](https://docs.python.org/3.15/library/io.html#io.FileIO), is returned.

See also the file handling modules, such as [fileinput](https://docs.python.org/3.15/library/fileinput.html#module-fileinput), [io](https://docs.python.org/3.15/library/io.html#module-io)
(where open() is declared), [os](https://docs.python.org/3.15/library/os.html#module-os), [os.path](https://docs.python.org/3.15/library/os.path.html#module-os.path), [tempfile](https://docs.python.org/3.15/library/tempfile.html#module-tempfile),
and [shutil](https://docs.python.org/3.15/library/shutil.html#module-shutil).

Raises an auditing event `open` with arguments `path`, `mode`, `flags`.

The `mode` and `flags` arguments may have been modified or inferred from
the original call.

> *Changed in version 3.3:*
>
> - The *opener* parameter was added.
>
> - The `'x'` mode was added.
>
> - [IOError](https://docs.python.org/3.15/builtins/exceptions.html#IOError) used to be raised, it is now an alias of [OSError](https://docs.python.org/3.15/builtins/exceptions.html#OSError).
>
> - [FileExistsError](https://docs.python.org/3.15/builtins/exceptions.html#FileExistsError) is now raised if the file opened in exclusive
>   creation mode (`'x'`) already exists.

> *Changed in version 3.4:*
>
> - The file is now non-inheritable.

> *Changed in version 3.5:*
>
> - If the system call is interrupted and the signal handler does not raise an
>   exception, the function now retries the system call instead of raising an
>   [InterruptedError](https://docs.python.org/3.15/builtins/exceptions.html#InterruptedError) exception (see [PEP 475](https://peps.python.org/pep-475/) for the rationale).
>
> - The `'namereplace'` error handler was added.

> *Changed in version 3.6:*
>
> - Support added to accept objects implementing [os.PathLike](https://docs.python.org/3.15/library/os.html#os.PathLike).
>
> - On Windows, opening a console buffer may return a subclass of
>   [io.RawIOBase](https://docs.python.org/3.15/library/io.html#io.RawIOBase) other than [io.FileIO](https://docs.python.org/3.15/library/io.html#io.FileIO).

> *Changed in version 3.11:* The `'U'` mode has been removed.

> *Changed in version 3.15:* UTF-8 is now the default encoding, instead of the
> platform-dependent locale encoding ([PEP 686](https://peps.python.org/pep-686/)).
