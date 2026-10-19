## `memoryview`

```
memoryview(object)
```

Create a memoryview that references *object*.  *object* must
support the buffer protocol.  Built-in objects that support the buffer
protocol include [bytes](../bytes/README.md) and [bytearray](../bytearray/README.md).

A memoryview has the notion of an *element*, which is the
atomic memory unit handled by the originating *object*.  For many simple
types such as [bytes](../bytes/README.md) and [bytearray](../bytearray/README.md), an element is a single
byte, but other types such as [array.array](https://docs.python.org/3.15/library/array.html#array.array) may have bigger elements.

memoryviews are [generic](https://docs.python.org/3.15/library/typing.html#generics) over the type of their
underlying data.

`len(view)` is equal to the length of [tolist()](https://docs.python.org/3.15/builtins/stdtypes.html#memoryview.tolist), which
is the nested list representation of the view. If `view.ndim == 1`,
this is equal to the number of elements in the view.

> *Changed in version 3.12:* If `view.ndim == 0`, `len(view)` now raises [TypeError](https://docs.python.org/3.15/builtins/exceptions.html#TypeError) instead of returning 1.

The `itemsize` attribute will give you the number of
bytes in a single element.

A memoryview supports slicing and indexing to expose its data.
One-dimensional slicing will result in a subview:

``` python
>>> v = memoryview(b'abcefg')
>>> v[1]
98
>>> v[-1]
103
>>> v[1:4]
<memory at 0x7f3ddc9f4350>
>>> bytes(v[1:4])
b'bce'
```
> Code: [example_01.py](example_01.py)

If `format` is one of the native format specifiers
from the [struct](https://docs.python.org/3.15/library/struct.html#module-struct) module, indexing with an integer or a tuple of
integers is also supported and returns a single *element* with
the correct type.  One-dimensional memoryviews can be indexed
with an integer or a one-integer tuple.  Multi-dimensional memoryviews
can be indexed with tuples of exactly *ndim* integers where *ndim* is
the number of dimensions.  Zero-dimensional memoryviews can be indexed
with the empty tuple.

Here is an example with a non-byte format:

``` python
>>> import array
>>> a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
>>> m = memoryview(a)
>>> m[0]
-11111111
>>> m[-1]
44444444
>>> m[::2].tolist()
[-11111111, -33333333]
```
> Code: [example_02.py](example_02.py)

If the underlying object is writable, the memoryview supports
one-dimensional slice assignment. Resizing is not allowed:

``` python
>>> data = bytearray(b'abcefg')
>>> v = memoryview(data)
>>> v.readonly
False
>>> v[0] = ord(b'z')
>>> data
bytearray(b'zbcefg')
>>> v[1:4] = b'123'
>>> data
bytearray(b'z123fg')
>>> v[2:3] = b'spam'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: memoryview assignment: lvalue and rvalue have different structures
>>> v[2:6] = b'spam'
>>> data
bytearray(b'z1spam')
```
> Code: [example_03.py](example_03.py)

One-dimensional memoryviews of [hashable](https://docs.python.org/3.15/glossary.html#term-hashable) (read-only) types with formats
'B', 'b' or 'c' are also hashable. The hash is defined as
`hash(m) == hash(m.tobytes())`:

``` python
>>> v = memoryview(b'abcefg')
>>> hash(v) == hash(b'abcefg')
True
>>> hash(v[2:4]) == hash(b'ce')
True
>>> hash(v[::-2]) == hash(b'abcefg'[::-2])
True
```
> Code: [example_04.py](example_04.py)

> *Changed in version 3.3:* One-dimensional memoryviews can now be sliced.
> One-dimensional memoryviews with formats 'B', 'b' or 'c' are now [hashable](https://docs.python.org/3.15/glossary.html#term-hashable).

> *Changed in version 3.4:* memoryview is now registered automatically with
> [collections.abc.Sequence](https://docs.python.org/3.15/library/collections.abc.html#collections.abc.Sequence)

> *Changed in version 3.5:* memoryviews can now be indexed with a tuple of integers.

> *Changed in version 3.14:* memoryview is now a [generic type](https://docs.python.org/3.15/glossary.html#term-generic-type).

memoryview has several methods:

### __eq__(exporter)

A memoryview and a [PEP 3118](https://peps.python.org/pep-3118/) exporter are equal if their shapes are
equivalent and if all corresponding values are equal when the operands'
respective format codes are interpreted using [struct](https://docs.python.org/3.15/library/struct.html#module-struct) syntax.

For the subset of [struct](https://docs.python.org/3.15/library/struct.html#module-struct) format strings currently supported by
`tolist()`, `v` and `w` are equal if `v.tolist() == w.tolist()`:

``` python
>>> import array
>>> a = array.array('I', [1, 2, 3, 4, 5])
>>> b = array.array('d', [1.0, 2.0, 3.0, 4.0, 5.0])
>>> c = array.array('b', [5, 3, 1])
>>> x = memoryview(a)
>>> y = memoryview(b)
>>> x == a == y == b
True
>>> x.tolist() == a.tolist() == y.tolist() == b.tolist()
True
>>> z = y[::-2]
>>> z == c
True
>>> z.tolist() == c.tolist()
True
```
> Code: [example_05.py](example_05.py)

If either format string is not supported by the [struct](https://docs.python.org/3.15/library/struct.html#module-struct) module,
then the objects will always compare as unequal (even if the format
strings and buffer contents are identical):

``` python
>>> from ctypes import BigEndianStructure, c_long
>>> class BEPoint(BigEndianStructure):
...     _fields_ = [("x", c_long), ("y", c_long)]
...
>>> point = BEPoint(100, 200)
>>> a = memoryview(point)
>>> b = memoryview(point)
>>> a == point
False
>>> a == b
False
```
> Code: [example_06.py](example_06.py)

Note that, as with floating-point numbers, `v is w` does *not* imply
`v == w` for memoryview objects.

> *Changed in version 3.3:* Previous versions compared the raw memory disregarding the item format
> and the logical array structure.

### tobytes(order='C')

Return the data in the buffer as a bytestring.  This is equivalent to
calling the [bytes](../bytes/README.md) constructor on the memoryview.

``` python
>>> m = memoryview(b"abc")
>>> m.tobytes()
b'abc'
>>> bytes(m)
b'abc'
```
> Code: [example_07.py](example_07.py)

For non-contiguous arrays the result is equal to the flattened list
representation with all elements converted to bytes. `tobytes()`
supports all format strings, including those that are not in
[struct](https://docs.python.org/3.15/library/struct.html#module-struct) module syntax.

> *Added in version 3.8:* *order* can be {'C', 'F', 'A'}.  When *order* is 'C' or 'F', the data
> of the original array is converted to C or Fortran order. For contiguous
> views, 'A' returns an exact copy of the physical memory. In particular,
> in-memory Fortran order is preserved. For non-contiguous views, the
> data is converted to C first. *order=None* is the same as *order='C'*.

### hex(*,, bytes_per_sep=1), hex(sep,, bytes_per_sep=1)

Return a string object containing two hexadecimal digits for each
byte in the buffer.

``` python
>>> m = memoryview(b"abc")
>>> m.hex()
'616263'
```
> Code: [example_08.py](example_08.py)

> *Added in version 3.5.*

> *Changed in version 3.8:* Similar to [bytes.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#bytes.hex), [memoryview.hex()](https://docs.python.org/3.15/builtins/stdtypes.html#memoryview.hex) now supports
> optional *sep* and *bytes_per_sep* parameters to insert separators
> between bytes in the hex output.

### tolist()

Return the data in the buffer as a list of elements.

``` python
>>> memoryview(b'abc').tolist()
[97, 98, 99]
>>> import array
>>> a = array.array('d', [1.1, 2.2, 3.3])
>>> m = memoryview(a)
>>> m.tolist()
[1.1, 2.2, 3.3]
```
> Code: [example_09.py](example_09.py)

> *Changed in version 3.3:* `tolist()` now supports all single character native formats in
> [struct](https://docs.python.org/3.15/library/struct.html#module-struct) module syntax as well as multi-dimensional
> representations.

### toreadonly()

Return a readonly version of the memoryview object.  The original
memoryview object is unchanged.

``` python
>>> m = memoryview(bytearray(b'abc'))
>>> mm = m.toreadonly()
>>> mm.tolist()
[97, 98, 99]
>>> mm[0] = 42
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cannot modify read-only memory
>>> m[0] = 43
>>> mm.tolist()
[43, 98, 99]
```
> Code: [example_10.py](example_10.py)

> *Added in version 3.8.*

### release()

Release the underlying buffer exposed by the memoryview object.  Many
objects take special actions when a view is held on them (for example,
a [bytearray](../bytearray/README.md) would temporarily forbid resizing); therefore,
calling release() is handy to remove these restrictions (and free any
dangling resources) as soon as possible.

After this method has been called, any further operation on the view
raises a `ValueError` (except `release()` itself which can
be called multiple times):

``` python
>>> m = memoryview(b'abc')
>>> m.release()
>>> m[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operation forbidden on released memoryview object
```
> Code: [example_11.py](example_11.py)

The context management protocol can be used for a similar effect,
using the `with` statement:

``` python
>>> with memoryview(b'abc') as m:
...     m[0]
...
97
>>> m[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operation forbidden on released memoryview object
```
> Code: [example_12.py](example_12.py)

> *Added in version 3.2.*

### cast(format,, /), cast(format,, shape,, /)

Cast a memoryview to a new format or shape. *shape* defaults to
`[byte_length//new_itemsize]`, which means that the result view
will be one-dimensional. The return value is a new memoryview, but
the buffer itself is not copied. Supported casts are 1D -> C-[contiguous](https://docs.python.org/3.15/glossary.html#term-contiguous)
and C-contiguous -> 1D.

The destination format is restricted to a single element native format in
[struct](https://docs.python.org/3.15/library/struct.html#module-struct) syntax. One of the formats must be a byte format
('B', 'b' or 'c'). The byte length of the result must be the same
as the original length.
Note that all byte lengths may depend on the operating system.

Cast 1D/long to 1D/unsigned bytes:

``` python
>>> import array
>>> a = array.array('l', [1,2,3])
>>> x = memoryview(a)
>>> x.format
'l'
>>> x.itemsize
8
>>> len(x)
3
>>> x.nbytes
24
>>> y = x.cast('B')
>>> y.format
'B'
>>> y.itemsize
1
>>> len(y)
24
>>> y.nbytes
24
```
> Code: [example_13.py](example_13.py)

Cast 1D/unsigned bytes to 1D/char:

``` python
>>> b = bytearray(b'zyz')
>>> x = memoryview(b)
>>> x[0] = b'a'
Traceback (most recent call last):
  ...
TypeError: memoryview: invalid type for format 'B'
>>> y = x.cast('c')
>>> y[0] = b'a'
>>> b
bytearray(b'ayz')
```
> Code: [example_14.py](example_14.py)

Cast 1D/bytes to 3D/ints to 1D/signed char:

``` python
>>> import struct
>>> buf = struct.pack("i"*12, *list(range(12)))
>>> x = memoryview(buf)
>>> y = x.cast('i', shape=[2,2,3])
>>> y.tolist()
[[[0, 1, 2], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]
>>> y.format
'i'
>>> y.itemsize
4
>>> len(y)
2
>>> y.nbytes
48
>>> z = y.cast('b')
>>> z.format
'b'
>>> z.itemsize
1
>>> len(z)
48
>>> z.nbytes
48
>>> buf = struct.pack("L"*6, *list(range(6)))
>>> x = memoryview(buf)
>>> y = x.cast('L', shape=[2,3])
>>> len(y)
2
>>> y.nbytes
48
>>> y.tolist()
[[0, 1, 2], [3, 4, 5]]
```
> Code: [example_15.py](example_15.py)

Cast 1D/unsigned long to 2D/unsigned long:

> *Added in version 3.3.*

> *Changed in version 3.5:* The source format is no longer restricted when casting to a byte view.

### count(value,, /)

Count the number of occurrences of *value*.

> *Added in version 3.14.*

### index(value,, start=0,, stop=sys.maxsize,, /)

Return the index of the first occurrence of *value* (at or after
index *start* and before index *stop*).

Raises a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) if *value* cannot be found.

> *Added in version 3.14.*

There are also several readonly attributes available:

### obj

The underlying object of the memoryview:

``` python
>>> b  = bytearray(b'xyz')
>>> m = memoryview(b)
>>> m.obj is b
True
```
> Code: [example_16.py](example_16.py)

> *Added in version 3.3.*

### nbytes

`nbytes == product(shape) * itemsize == len(m.tobytes())`. This is
the amount of space in bytes that the array would use in a contiguous
representation. It is not necessarily equal to `len(m)`:

``` python
>>> import array
>>> a = array.array('i', [1,2,3,4,5])
>>> m = memoryview(a)
>>> len(m)
5
>>> m.nbytes
20
>>> y = m[::2]
>>> len(y)
3
>>> y.nbytes
12
>>> len(y.tobytes())
12
```
> Code: [example_17.py](example_17.py)

Multi-dimensional arrays:

``` python
>>> import struct
>>> buf = struct.pack("d"*12, *[1.5*x for x in range(12)])
>>> x = memoryview(buf)
>>> y = x.cast('d', shape=[3,4])
>>> y.tolist()
[[0.0, 1.5, 3.0, 4.5], [6.0, 7.5, 9.0, 10.5], [12.0, 13.5, 15.0, 16.5]]
>>> len(y)
3
>>> y.nbytes
96
```
> Code: [example_18.py](example_18.py)

> *Added in version 3.3.*

### readonly

A bool indicating whether the memory is read only.

### format

A string containing the format (in [struct](https://docs.python.org/3.15/library/struct.html#module-struct) module style) for each
element in the view. A memoryview can be created from exporters with
arbitrary format strings, but some methods (e.g. `tolist()`) are
restricted to native single element formats.

> *Changed in version 3.3:* format `'B'` is now handled according to the struct module syntax.
> This means that `memoryview(b'abc')[0] == b'abc'[0] == 97`.

### itemsize

The size in bytes of each element of the memoryview:

``` python
>>> import array, struct
>>> m = memoryview(array.array('H', [32000, 32001, 32002]))
>>> m.itemsize
2
>>> m[0]
32000
>>> struct.calcsize('H') == m.itemsize
True
```
> Code: [example_19.py](example_19.py)

### ndim

An integer indicating how many dimensions of a multi-dimensional array the
memory represents.

### shape

A tuple of integers the length of `ndim` giving the shape of the
memory as an N-dimensional array.

> *Changed in version 3.3:* An empty tuple instead of `None` when ndim = 0.

### strides

A tuple of integers the length of `ndim` giving the size in bytes to
access each element for each dimension of the array.

> *Changed in version 3.3:* An empty tuple instead of `None` when ndim = 0.

### suboffsets

Used internally for PIL-style arrays. The value is informational only.

### c_contiguous

A bool indicating whether the memory is C-[contiguous](https://docs.python.org/3.15/glossary.html#term-contiguous).

> *Added in version 3.3.*

### f_contiguous

A bool indicating whether the memory is Fortran [contiguous](https://docs.python.org/3.15/glossary.html#term-contiguous).

> *Added in version 3.3.*

### contiguous

A bool indicating whether the memory is [contiguous](https://docs.python.org/3.15/glossary.html#term-contiguous).

> *Added in version 3.3.*

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.10.3: Paylaşılan tamponu izle**

#### Önce

[b:2.10](../README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.14 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Aynı tampon üzerinde görünüm ve kopyanın yaşamını izle:

1. `data=bytearray(b"ABCD")`, `v=memoryview(data)`, `alt=v[1:3]` ve `salt=v.toreadonly()` kur. `alt` üzerinden bir bayt değiştir; data ve salt sonuçlarını göster.
2. Aynı boyutlu dilim atamasını, farklı boyutlu atamayı ve salt üzerinden yazmayı karşılaştır. `bytes(v)`, `tolist()` ve `hex()` sonuçlarını kaydet.
3. `v.cast("B",shape=[2,2])` ile yeni görünüm al; ndim/shape/strides/itemsize/nbytes/len ilişkisini göster. `obj` kimliğini, c_contiguous/f_contiguous ve suboffsets alanlarının veri değil görünüm metadatası oluşunu kaynakla ilişkilendir.
4. Bütün alt görünümleri bırakmadan data boyutunu değiştirmeyi dene, sonra hepsini release et. Bırakılmış görünüm erişimini, tekrar release çağrısını ve with ile bırakmayı karşılaştır. Hashable bytes görünümü ile writable bytearray görünümünün hash sınırını göster; eşitlikte ham baytların yanında format/shape yorumunun da önemini açıkla.
5. Python 3.14+ count/index için bulunan ve bulunmayan öğeyi ekle. Python 3.12+ sıfır boyutlu görünümde len sınırını yazılı açıkla.

#### Geçiş ölçütleri

- [ ] Alt görünüm aynı tamponu paylaşır; readonly görünüm başka ad üzerinden değişikliği görür, yazma denemesi TypeError verir.
- [ ] Farklı boyutlu görünüm ataması ValueError; dış bytearray yeniden boyutlandırılması canlı export varken BufferError verir.
- [ ] Nbytes bayt miktarıdır, len ilk boyut uzunluğudur; dönüştürme kopyası ile cast/slice görünümü ayrılmıştır.
- [ ] Release sonrası erişim ValueError; yeniden release geçerlidir; bütün exportlar bırakıldıktan sonra yeniden boyutlandırma geçerlidir.
- [ ] 3.14 count sayı, index ilk indeks veya ValueError verir; 3.12 sıfır boyutta len TypeError verir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../bytes.count/README.md)
<!-- learning-task:end -->
