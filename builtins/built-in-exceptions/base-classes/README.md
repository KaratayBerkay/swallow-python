The following exceptions are used mostly as base classes for other exceptions.

- [`BaseException`](BaseException/README.md) — The base class for all built-in exceptions.
- [`Exception`](Exception/README.md) — All built-in, non-system-exiting exceptions are derived from this class.
- [`ArithmeticError`](ArithmeticError/README.md) — The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError.
- [`BufferError`](BufferError/README.md) — Raised when a buffer related operation cannot be performed.
- [`LookupError`](LookupError/README.md) — The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid: IndexError, KeyError.

<!-- learning-milestone:start -->
## Klasör milestone görevi

**Milestone: Hata ailelerini doğru sınırda yakala**

### Önce

Bu klasördeki bütün bölüm görevleri ve alt klasör milestone kontrolleri tamamlanmış olmalı. Sırayı [görev dizininden](../../../TASKS.md) kontrol et.

### Tek görev

KeyError, IndexError, ZeroDivisionError ve KeyboardInterrupt nesnelerini yalnız kontrollü raise ile ayrı ayrı yükselt. LookupError, ArithmeticError, Exception ve BaseException handlerlarının hangilerini kapsadığını tabloyla göster.

### Geçiş ölçütleri

- [ ] Kalıtım yönü doğru; BaseExceptionın çok geniş yakalama alanı açıklanmıştır.
- [ ] Args ve ek notlar taşınır; hata adı benzerliği sınıf ilişkisi yerine kullanılmaz.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [klasör milestone görevi](MILESTONE.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../concrete-exceptions/AssertionError/README.md)
<!-- learning-milestone:end -->
