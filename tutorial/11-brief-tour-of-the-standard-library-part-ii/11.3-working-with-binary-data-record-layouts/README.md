## 11.3. Working with binary data record layouts

The `struct` module provides `pack()` and `unpack()` functions for working with variable length binary record formats. The following example shows how to loop through header information in a ZIP file without using the `zipfile` module. Pack codes `"H"` and `"I"` represent two and four byte unsigned numbers respectively. The `"<"` indicates that they are standard size and in little-endian byte order:

``` python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```
> Code: [start.py](start.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 11.3: Binary kayıttaki sınırları hesapla**

**Odak:** struct alan boyutu/sırası, little-endian ve dilim üzerinden kayıt okuma.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:11.2](../11.2-templating/README.md).
- Ön bilgi: [t:7.2.1](../../07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md).

#### Tek görev

1. Bölümdeki <IIIHH düzeninde struct.unpack sonucunun (1, 4, 9, 3, 2) olduğunu kabul ederek bir kayıt okuma izi çıkar.

2. Bu tuple içindeki değerleri crc32, comp_size, uncomp_size, filenamesize, extra_size alanlarına eşleştir.

3. Alan bloğu başlangıcını 14 kabul ederek örnekteki start akışında alan bloğu, dosya adı, ek alan ve sonraki kayda ilerleme sınırlarını hesapla.

4. Gerçek ZIP dosyası veya bölümde örneklenmeyen pack çağrısı yazman gerekmiyor.

#### Geçiş ölçütleri

- [ ] Alan bloğu 16 bayt; üç I dörder, iki H ikişer bayt.
- [ ] Geri açılan beş değer verilen sırada ve aynı.
- [ ] Alan bloğu [14:30], ad [30:33], ek alan [33:35], veri 4 bayt sonrası sonraki başlangıç 39.
- [ ] < little-endian; kayıt sınırları dosyanın rastgele yerinden tahmin edilmemiş.
- [ ] Gerçek ZIP yapısını sıfırdan bilmek veya zipfile API ayrıntıları gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../11.4-multi-threading/README.md)
<!-- learning-task:end -->
