## `print()`

```
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

Print *objects* to the text stream *file*, separated by *sep* and followed
by *end*.  *sep*, *end*, *file*, and *flush*, if present, must be given as keyword
arguments.

All non-keyword arguments are converted to strings like `str()` does and
written to the stream, separated by *sep* and followed by *end*.  Both *sep*
and *end* must be strings; they can also be `None`, which means to use the
default values.  If no *objects* are given, print() will just write
*end*.

The *file* argument must be an object with a `write(string)` method; if it
is not present or `None`, [sys.stdout](https://docs.python.org/3.15/library/sys.html#sys.stdout) will be used.  Since printed
arguments are converted to text strings, print() cannot be used with
binary mode file objects.  For these, use `file.write(...)` instead.

Output buffering is usually determined by *file*.
However, if *flush* is true, the stream is forcibly flushed.

> *Changed in version 3.3:* Added the *flush* keyword argument.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.54: print sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

İki print çağrısıyla ilk satırı `Ada|7!`, ikinci satırı `tamam` olacak biçimde üret. sep ve end kullan; None değerinin yazdırılmasıyla hiçbir nesne verilmemesini karşılaştır. file ve flush seçeneklerinin rolünü açıkla.

#### Geçiş ölçütleri

- [ ] İlk çağrı `print("Ada",7,sep="|",end="!\n")` eşdeğerindedir.
- [ ] None yazdırmak "None" üretir; argümansız çağrı yalnız end yazar; file hedefi, flush tamponu kontrol eder.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../property/README.md)
<!-- learning-task:end -->
