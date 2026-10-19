## `sequence.index`

```
sequence.index(value[, start[, stop]])
```

Return the index of the first occurrence of *value* in *sequence*.

Raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) if *value* is not found in *sequence*.

The *start* or *stop* arguments allow for efficient searching
of subsections of the sequence, beginning at *start* and ending at *stop*.
This is roughly equivalent to `start + sequence[start:stop].index(value)`,
only without copying any data.

> **Caution**
>
> Not all sequence types support passing the *start* and *stop* arguments.

## Çözümlü kısa örnek

İlk eşleşmenin özgün indeksini, arama sınırını ve yokluk hatasını ayır

```python
print(repr([1,2,1].index(1)))
# Sonuç: 0
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.7.11: sequence.index davranışını ayırt et**

#### Önce

[b:2.7](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; i̇lk eşleşmenin özgün indeksini, arama sınırını ve yokluk hatasını ayır

```python
[1,2,1].index(1,1)
[1,2].index(9)
```

Aynı değeri aramayı tuple ve range üzerinde de dene. Index için başlangıç/bitiş argümanlarının bütün sequence türlerinde desteklendiğini varsayma; desteklenmeyen çağrıyı kaynak notuyla ilişkilendir.

#### Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `2`; `ValueError`.
- [ ] İlk eşleşmenin özgün indeksini, arama sınırını ve yokluk hatasını ayır

- [ ] List/tuple/range üzerindeki ortak sonuç sözleşmesi ile isteğe bağlı parametre desteği ayrı incelenmiştir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../sequence.append/README.md)
<!-- learning-task:end -->
