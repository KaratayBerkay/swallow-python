## `str.islower`

```
str.islower()
```

Return `True` if all cased characters [^1] in the string are lowercase and
there is at least one cased character, `False` otherwise.

[^1]: Cased characters are those with general category property being one of "Lu" (Letter, uppercase), "Ll" (Letter, lowercase), or "Lt" (Letter, titlecase).

## Çözümlü kısa örnek

En az bir büyük/küçük harf özelliği olan karakter gerekir

```python
print(repr("ada".islower()))
# Sonuç: True
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.9.20: str.islower davranışını ayırt et**

#### Önce

[b:2.9](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; en az bir büyük/küçük harf özelliği olan karakter gerekir

```python
"ada 12!".islower()
"Ada".islower()
"123".islower()
```

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `False`; `False`.
- [ ] En az bir büyük/küçük harf özelliği olan karakter gerekir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../str.isnumeric/README.md)
<!-- learning-task:end -->
