## 10.5. String pattern matching

The `re` module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions:

``` python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```
> Code: [re_example.py](re_example.py)

When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:

``` python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```
> Code: [example_01.py](example_01.py)

<!-- learning-task:start -->
### Bölüm görevi

**Görev 10.5: Örnekteki kalıpla eşleşeni ve değişeni bul**

**Odak:** Verilen re.findall/re.sub kalıplarını kullanma ve basit replace seçimi.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:10.4](../10.4-error-output-redirection-and-program-termination/README.md).

#### Tek görev

1. README içindeki iki regex kalıbını aynen kullan. findall girdisini "fast foot and fastest hand" yap; sub girdisini "one the the hat" yap.

2. Çalıştırmadan önce bulunan sözcükleri ve değişen metni çıkar.

3. Sonra "tea for too" metnindeki yalnız too sözcüğünü two yapmak için bölümdeki daha basit yöntemi uygula.

4. Yeni regex kalıbı tasarlaman gerekmiyor.

#### Geçiş ölçütleri

- [ ] findall sırasıyla fast, foot, fastest buluyor.
- [ ] Tekrar silme sonucu one the hat.
- [ ] Basit değişim tea for two; str.replace yeterli olduğu gerekçelendirilmiş.
- [ ] findall sonuç listesi ile sub yeni metin dönüşü ayrılmış; regex motorunun işlenmemiş ayrıntıları istenmemiş.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../10.6-mathematics/README.md)
<!-- learning-task:end -->
