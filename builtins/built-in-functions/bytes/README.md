## `bytes()`

```
bytes(source=b'')
bytes(source, encoding, errors='strict')
```

Return a new "bytes" object which is an immutable sequence of integers in
the range `0 <= x < 256`.  bytes is an immutable version of
[bytearray](../bytearray/README.md) -- it has the same non-mutating methods and the same
indexing and slicing behavior.

Accordingly, constructor arguments are interpreted as for `bytearray()`.

Bytes objects can also be created with literals, see [String and Bytes literals](https://docs.python.org/3.15/reference/lexical_analysis.html#strings).

See also [Binary Sequence Types — bytes, bytearray, memoryview](https://docs.python.org/3.15/builtins/stdtypes.html#binaryseq), [Bytes Objects](https://docs.python.org/3.15/builtins/stdtypes.html#typebytes), and [Bytes and Bytearray Operations](https://docs.python.org/3.15/builtins/stdtypes.html#bytes-methods).

## Çözümlü kısa örnek

Bytes değişmezdir; tamsayı uzunluk, iterable ise öğe değerleri verir.

```python
print(repr(bytes([65])))
# Sonuç: b'A'
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.11: bytes davranışını ayırt et**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; bytes değişmezdir; tamsayı uzunluk, iterable ise öğe değerleri verir.

```python
bytes(2)
bytes("İ", "utf-8")
bytes([256])
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `b'\x00\x00'`; `b'\xc4\xb0'`; `ValueError`.
- [ ] Bytes değişmezdir; tamsayı uzunluk, iterable ise öğe değerleri verir.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../callable/README.md)
<!-- learning-task:end -->
