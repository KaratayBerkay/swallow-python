# Görev b:2.14.3: genericalias.__parameters__ davranışını ayırt et

## Önce

[b:2.14](../README.md) ve bu sayfanın açıklama/örnekleri.

## Tek görev

Aşağıdaki denemeleri ayrı ayrı incele. Sonuç veya hata türünü önce çıkar, sonra doğrula; henüz bağlanmamış benzersiz type variablelar listelenir

```python
from typing import TypeVar
T=TypeVar("T")
dict[T,T].__parameters__ == (T,)
list[int].__parameters__ == ()
```

## Geçiş ölçütleri

- [ ] Sonuçlar sırayla: `True`; `True`.
- [ ] Henüz bağlanmamış benzersiz type variablelar listelenir

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)
