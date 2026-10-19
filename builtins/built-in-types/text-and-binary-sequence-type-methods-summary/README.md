The following table summarizes the text and binary sequence methods by category.

Bu tablo bir başvuru haritasıdır. Her satırda işlem ailesi, str yöntemi ve varsa bytes/bytearray karşılığı bulunur. "Yok", o satırdaki metin yönteminin tabloda binary karşılığı bulunmadığını belirtir. Yöntem adını görmek, argümanlarını ve davranışını öğrenmiş olmak anlamına gelmez; uygulama ayrıntıları sonraki anlatımlardadır.

| Category | [str](../text-sequence-type-str/str/README.md) methods | [bytes](../binary-sequence-types-bytes-bytearray-memoryview/bytes/README.md) and [bytearray](../binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md) methods |
| --- | --- | --- |
| Formatting | [str.format()](../text-sequence-type-str/str.format/README.md) | Yok |
| Formatting | [str.format_map()](../text-sequence-type-str/str.format_map/README.md) | Yok |
| Formatting | [f-strings](https://docs.python.org/3.15/reference/lexical_analysis.html#f-strings) | Yok |
| Formatting | [printf-style String Formatting](https://docs.python.org/3.15/builtins/stdtypes.html#old-string-formatting) | [printf-style Bytes Formatting](https://docs.python.org/3.15/builtins/stdtypes.html#bytes-formatting) |
| Searching and Replacing | [str.find()](../text-sequence-type-str/str.find/README.md) | [bytes.find()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.find/README.md) |
| Searching and Replacing | [str.rfind()](../text-sequence-type-str/str.rfind/README.md) | [bytes.rfind()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rfind/README.md) |
| Searching and Replacing | [str.index()](../text-sequence-type-str/str.index/README.md) | [bytes.index()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.index/README.md) |
| Searching and Replacing | [str.rindex()](../text-sequence-type-str/str.rindex/README.md) | [bytes.rindex()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rindex/README.md) |
| Searching and Replacing | [str.startswith()](../text-sequence-type-str/str.startswith/README.md) | [bytes.startswith()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.startswith/README.md) |
| Searching and Replacing | [str.endswith()](../text-sequence-type-str/str.endswith/README.md) | [bytes.endswith()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.endswith/README.md) |
| Searching and Replacing | [str.count()](../text-sequence-type-str/str.count/README.md) | [bytes.count()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.count/README.md) |
| Searching and Replacing | [str.replace()](../text-sequence-type-str/str.replace/README.md) | [bytes.replace()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.replace/README.md) |
| Splitting and Joining | [str.split()](../text-sequence-type-str/str.split/README.md) | [bytes.split()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.split/README.md) |
| Splitting and Joining | [str.rsplit()](../text-sequence-type-str/str.rsplit/README.md) | [bytes.rsplit()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rsplit/README.md) |
| Splitting and Joining | [str.splitlines()](../text-sequence-type-str/str.splitlines/README.md) | [bytes.splitlines()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.splitlines/README.md) |
| Splitting and Joining | [str.partition()](../text-sequence-type-str/str.partition/README.md) | [bytes.partition()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.partition/README.md) |
| Splitting and Joining | [str.rpartition()](../text-sequence-type-str/str.rpartition/README.md) | [bytes.rpartition()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rpartition/README.md) |
| Splitting and Joining | [str.join()](../text-sequence-type-str/str.join/README.md) | [bytes.join()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.join/README.md) |
| String Classification | [str.isalpha()](../text-sequence-type-str/str.isalpha/README.md) | [bytes.isalpha()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.isalpha/README.md) |
| String Classification | [str.isdecimal()](../text-sequence-type-str/str.isdecimal/README.md) | Yok |
| String Classification | [str.isdigit()](../text-sequence-type-str/str.isdigit/README.md) | [bytes.isdigit()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.isdigit/README.md) |
| String Classification | [str.isnumeric()](../text-sequence-type-str/str.isnumeric/README.md) | Yok |
| String Classification | [str.isalnum()](../text-sequence-type-str/str.isalnum/README.md) | [bytes.isalnum()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.isalnum/README.md) |
| String Classification | [str.isidentifier()](../text-sequence-type-str/str.isidentifier/README.md) | Yok |
| String Classification | [str.islower()](../text-sequence-type-str/str.islower/README.md) | [bytes.islower()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.islower/README.md) |
| String Classification | [str.isupper()](../text-sequence-type-str/str.isupper/README.md) | [bytes.isupper()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.isupper/README.md) |
| String Classification | [str.istitle()](../text-sequence-type-str/str.istitle/README.md) | [bytes.istitle()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.istitle/README.md) |
| String Classification | [str.isspace()](../text-sequence-type-str/str.isspace/README.md) | [bytes.isspace()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.isspace/README.md) |
| String Classification | [str.isprintable()](../text-sequence-type-str/str.isprintable/README.md) | Yok |
| Case Manipulation | [str.lower()](../text-sequence-type-str/str.lower/README.md) | [bytes.lower()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.lower/README.md) |
| Case Manipulation | [str.upper()](../text-sequence-type-str/str.upper/README.md) | [bytes.upper()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.upper/README.md) |
| Case Manipulation | [str.casefold()](../text-sequence-type-str/str.casefold/README.md) | Yok |
| Case Manipulation | [str.capitalize()](../text-sequence-type-str/str.capitalize/README.md) | [bytes.capitalize()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.capitalize/README.md) |
| Case Manipulation | [str.title()](../text-sequence-type-str/str.title/README.md) | [bytes.title()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.title/README.md) |
| Case Manipulation | [str.swapcase()](../text-sequence-type-str/str.swapcase/README.md) | [bytes.swapcase()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.swapcase/README.md) |
| Padding and Stripping | [str.ljust()](../text-sequence-type-str/str.ljust/README.md) | [bytes.ljust()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.ljust/README.md) |
| Padding and Stripping | [str.rjust()](../text-sequence-type-str/str.rjust/README.md) | [bytes.rjust()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rjust/README.md) |
| Padding and Stripping | [str.center()](../text-sequence-type-str/str.center/README.md) | [bytes.center()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.center/README.md) |
| Padding and Stripping | [str.expandtabs()](../text-sequence-type-str/str.expandtabs/README.md) | [bytes.expandtabs()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.expandtabs/README.md) |
| Padding and Stripping | [str.strip()](../text-sequence-type-str/str.strip/README.md) | [bytes.strip()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.strip/README.md) |
| Padding and Stripping | [str.lstrip()](../text-sequence-type-str/str.lstrip/README.md) | [bytes.lstrip()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.lstrip/README.md) |
| Padding and Stripping | [str.rstrip()](../text-sequence-type-str/str.rstrip/README.md) | [bytes.rstrip()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.rstrip/README.md) |
| Padding and Stripping | [str.removeprefix()](../text-sequence-type-str/str.removeprefix/README.md) | [bytes.removeprefix()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.removeprefix/README.md) |
| Padding and Stripping | [str.removesuffix()](../text-sequence-type-str/str.removesuffix/README.md) | [bytes.removesuffix()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.removesuffix/README.md) |
| Translation and Encoding | [str.translate()](../text-sequence-type-str/str.translate/README.md) | [bytes.translate()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.translate/README.md) |
| Translation and Encoding | [str.maketrans()](../text-sequence-type-str/str.maketrans/README.md) | [bytes.maketrans()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.maketrans/README.md) |
| Translation and Encoding | [str.encode()](../text-sequence-type-str/str.encode/README.md) | Yok |
| Translation and Encoding | Yok | [bytes.decode()](../binary-sequence-types-bytes-bytearray-memoryview/bytes.decode/README.md) |

## Tabloyu okuma örneği

Searching and Replacing grubunda `str.find()` metin sütununda, `bytes.find()` binary sütununda bulunur. Bu adımda yalnız bu eşleşmeyi okuyabiliriz; hangi argümanın hangi sonucu verdiğini ilgili yöntem anlatımından öğreniriz.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.8: Yöntem ailesini veri türünden seç**

#### Önce

[b:2](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Tabloyu bir başvuru haritası olarak kullan. Üç seçim yap: Splitting and Joining grubundan iki veri türünde de karşılığı olan bir yöntem çifti; Padding and Stripping grubundan başka bir çift; String Classification grubundan yalnız str sütununda bulunan bir yöntem.

Her seçim için grup adını ve ilgili sütunlardaki yöntem adlarını yaz. Olmayan bir karşılığı diğer türe taşıma. Bu adımda kod, argüman veya çıktı üretmek gerekmiyor; yöntemlerin çalışma sözleşmeleri sonraki anlatımlarda sınanacak.

#### Geçiş ölçütleri

- [ ] İlk iki seçim doğru gruptan alınmış; str ve binary karşılıkları doğru sütunlardan eşleştirilmiş.
- [ ] Üçüncü yöntemin binary karşılığı tabloda yok; adından hareketle böyle bir API uydurulmamış.
- [ ] Bir yöntemin tabloda adının bulunmasıyla onu uygulamayı öğrenmiş olmak ayrılmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../text-sequence-type-str/README.md)
<!-- learning-task:end -->
