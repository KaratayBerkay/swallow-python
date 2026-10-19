## `UnicodeError`

```
UnicodeError
```

Raised when a Unicode-related encoding or decoding error occurs.  It is a
subclass of [ValueError](../ValueError/README.md).

UnicodeError has attributes that describe the encoding or decoding
error.  For example, `err.object[err.start:err.end]` gives the particular
invalid input that the codec failed on.

### encoding

The name of the encoding that raised the error.

### reason

A string describing the specific codec error.

### object

The object the codec was attempting to encode or decode.

### start

The first index of invalid data in [object](../../../built-in-functions/object/README.md).

This value should not be negative as it is interpreted as an
absolute offset but this constraint is not enforced at runtime.

### end

The index after the last invalid data in [object](../../../built-in-functions/object/README.md).

This value should not be negative as it is interpreted as an
absolute offset but this constraint is not enforced at runtime.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:4.4.30: Geçersiz veri aralığını ayır**

#### Önce

[t:8.3](../../../../tutorial/08-errors-and-exceptions/8.3-handling-exceptions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

`b"A\xffB".decode("utf-8")` ve `"AİB".encode("ascii")` hatalarını ayrı yakala. Encoding, object, start, end, reason alanlarını ve `e.object[e.start:e.end]` dilimini göster.

#### Geçiş ölçütleri

- [ ] İlk hata UnicodeDecodeError ve sorunlu dilim b"\xff"; ikinci UnicodeEncodeError ve sorunlu dilim "İ".
- [ ] Start dahil, end hariçtir; encoding ve reason tanı koymak için korunur.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../UnicodeEncodeError/README.md)
<!-- learning-task:end -->
