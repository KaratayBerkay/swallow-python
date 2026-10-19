## 5.7. More on Conditions

The conditions used in `while` and `if` statements can contain any operators, not just comparisons.

The comparison operators `in` and `not in` are membership tests that determine whether a value is in (or not in) a container. The operators `is` and `is not` compare whether two objects are really the same object. All comparison operators have the same priority, which is lower than that of all numerical operators.

Comparisons can be chained. For example, `a < b == c` tests whether `a` is less than `b` and moreover `b` equals `c`.

Comparisons may be combined using the Boolean operators `and` and `or`, and the outcome of a comparison (or of any other Boolean expression) may be negated with `not`. These have lower priorities than comparison operators; between them, `not` has the highest priority and `or` the lowest, so that `A and not B or C` is equivalent to `(A and (not B)) or C`. As always, parentheses can be used to express the desired composition.

The Boolean operators `and` and `or` are so-called *short-circuit* operators: their arguments are evaluated from left to right, and evaluation stops as soon as the outcome is determined. For example, if `A` and `C` are true but `B` is false, `A and B and C` does not evaluate the expression `C`. When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.

It is possible to assign the result of a comparison or other Boolean expression to a variable. For example,

``` python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```
> Code: [non_null.py](non_null.py)

Note that in Python, unlike C, assignment inside expressions must be done explicitly with the walrus operator `:=`. This avoids a common class of problems encountered in C programs: typing `=` in an expression when `==` was intended.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 5.7: Koşulun hangi kısmına gerçekten ulaşıldığını göster**

**Odak:** Üyelik, kimlik/eşitlik, zincirli karşılaştırma, öncelik ve and/or kısa devresi.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:5.6](../5.6-looping-techniques/README.md).
- Ön bilgi: [t:4.1](../../04-more-control-flow-tools/4.1-if-statements/README.md).

#### Tek görev

1. a = [1], b = a, c = a[:] kur; == ile is sonuçlarını karşılaştır.

2. Sonra value = "" or "fallback" or "last" ifadesinin sonucunu; False and (1 / 0), True or (1 / 0) ifadelerinde hangi tarafın çalıştığını açıkla. x=3 ve x=7 için 0 < x < 5 dene.

3. A and not B or C ifadesini anlamı değişmeden parantezle; =, == ve bölümde adı geçen := rollerini sözle ayır.

#### Geçiş ölçütleri

- [ ] a == c doğru, a is c yanlış, a is b doğru.
- [ ] or yalnız bool değil fallback metnini döndürüyor.
- [ ] Kısa devre nedeniyle iki bölme ifadesi de değerlendirilmemiş.
- [ ] Zincir koşulu 3 için doğru, 7 için yanlış; parantezler (A and (not B)) or C.
- [ ] in üyelik, is kimlik, == değer karşılaştırması; := ile yeni bir algoritma yazılması gerekmiyor.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../5.8-comparing-sequences-and-other-types/README.md)
<!-- learning-task:end -->
