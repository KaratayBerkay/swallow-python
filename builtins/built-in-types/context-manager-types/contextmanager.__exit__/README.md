## `contextmanager.__exit__`

```
contextmanager.__exit__(exc_type, exc_val, exc_tb)
```

Exit the runtime context and return a Boolean flag indicating if any exception
that occurred should be suppressed. If an exception occurred while executing the
body of the `with` statement, the arguments contain the exception type,
value and traceback information. Otherwise, all three arguments are `None`.

Returning a true value from this method will cause the `with` statement
to suppress the exception and continue execution with the statement immediately
following the `with` statement. Otherwise the exception continues
propagating after this method has finished executing.

If this method raises an exception while handling an earlier exception from the
`with` block, the new exception is raised, and the original exception
is stored in its [__context__](https://docs.python.org/3.15/builtins/exceptions.html#BaseException.__context__) attribute.

The exception passed in should never be reraised explicitly - instead, this
method should return a false value to indicate that the method completed
successfully and does not want to suppress the raised exception. This allows
context management code to easily detect whether or not an [__exit__()](https://docs.python.org/3.15/reference/datamodel.html#object.__exit__)
method has actually failed.

## Çözümlü kısa örnek

```python
# Normal bitişte exit(None, None, None) çağrılır.
# Gövde hata verirse exit(hata_turu, hata, traceback) çağrılır.
# Doğru dönüş hatayı bastırır; yanlış dönüş yayılmasını sürdürür.
```

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:2.13.2: Bastırma kararını görünür kıl**

#### Önce

[b:2.13](../README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Aynı ValueError üreten gövdeyi __exit__ True ve False döndüren iki yönetici ile dene. Normal gövdede True dönüşüyle karşılaştır. Hata sınıfı, değeri ve traceback argümanlarını kaydet.

#### Geçiş ölçütleri

- [ ] True gövde hatasını bastırır, False yayılmasını sürdürür.
- [ ] Normal bitişte (None,None,None) verilir; dönüşün doğruluğu normal akışı değiştirmez.
- [ ] Exit gövdedeki hatayı elle yeniden raise etmek zorunda değildir.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
