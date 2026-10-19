## `OSError`

```
OSError([arg])
OSError(errno, strerror[, filename[, winerror[, filename2]]])
```

This exception is raised when a system function returns a system-related
error, including I/O failures such as "file not found" or "disk full"
(not for illegal argument types or other incidental errors).

The second form of the constructor sets the corresponding attributes,
described below.  The attributes default to [None](https://docs.python.org/3.15/builtins/constants.html#None) if not
specified.  For backwards compatibility, if three arguments are passed,
the [args](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.args) attribute contains only a 2-tuple
of the first two constructor arguments.

The constructor often actually returns a subclass of OSError, as
described in [OS exceptions](../README.md#os-exceptions) below.  The particular subclass depends on
the final `.errno` value.  This behaviour only occurs when
constructing OSError directly or via an alias, and is not
inherited when subclassing.

### errno

A numeric error code from the C variable `errno`.

### winerror

Under Windows, this gives you the native
Windows error code.  The `.errno` attribute is then an approximate
translation, in POSIX terms, of that native error code.

Under Windows, if the *winerror* constructor argument is an integer,
the `.errno` attribute is determined from the Windows error code,
and the *errno* argument is ignored.  On other platforms, the
*winerror* argument is ignored, and the `winerror` attribute
does not exist.

### strerror

The corresponding error message, as provided by
the operating system.  It is formatted by the C
functions `perror` under POSIX, and `FormatMessage`
under Windows.

### filename, filename2

For exceptions that involve a file system path (such as [open()](../../../built-in-functions/open/README.md) or
[os.unlink()](https://docs.python.org/3.15/library/os.html#os.unlink)), `filename` is the file name passed to the function.
For functions that involve two file system paths (such as
[os.rename()](https://docs.python.org/3.15/library/os.html#os.rename)), `filename2` corresponds to the second
file name passed to the function.

> *Changed in version 3.3:* [EnvironmentError](../EnvironmentError/README.md), [IOError](../IOError/README.md), [WindowsError](../WindowsError/README.md),
> [socket.error](https://docs.python.org/3.15/library/socket.html#socket.error), [select.error](https://docs.python.org/3.15/library/select.html#select.error) and
> `mmap.error` have been merged into OSError, and the
> constructor may return a subclass.

> *Changed in version 3.4:* The `filename` attribute is now the original file name passed to
> the function, instead of the name encoded to or decoded from the
> [filesystem encoding and error handler](https://docs.python.org/3.15/glossary.html#term-filesystem-encoding-and-error-handler). Also, the *filename2*
> constructor argument and attribute was added.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.15: Sistem hatasının alanlarını koru**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`e=OSError(2,"yok","ornek.txt")` nesnesini oluştur. Tür, errno, strerror, filename ve args değerlerini kaydet. Mesajı eşleştirerek karar vermek yerine hata türü/alanlarını kullanmanın neden daha doğru olduğunu açıkla; verilmemiş filename2 ve platforma özgü winerror alanlarını genelleme.

#### Geçiş ölçütleri

- [ ] Bu kurucu FileNotFoundError alt türünü verir; errno=2, filename="ornek.txt", args=(2,"yok").
- [ ] Dosya adı mesajdan ayrı alandır; platforma özel alanlar her ortamda bulunmak zorunda değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../OverflowError/README.md)
<!-- learning-task:end -->
