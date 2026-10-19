## 8.6. User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). Exceptions should typically be derived from the `Exception` class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

Most exceptions are defined with names that end in "Error", similar to the naming of the standard exceptions.

Many standard modules define their own exceptions to report errors that may occur in functions they define.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 8.6: Alan hatasını doğru exception ailesine yerleştir**

**Odak:** Exception alt sınıfı, anlamlı Error adı ve basit özel hata.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:8.4](../8.4-raising-exceptions/README.md).
- Ön bilgi: [t:8.3](../8.3-handling-exceptions/README.md).

#### Tek görev

1. Bir görev sayacında negatif değer için NegativeCountError adlı özel hata gerektiğini düşün.

2. Yeni sınıf yazmak yerine tasarım notunda adını, hangi sınıftan türeyeceğini, hangi hatalarda kullanılacağını ve except NegativeCountError ile except Exception handlerlarının kapsam ilişkisini yaz.

3. Sınıf yazım sözdizimi bu kısa bölümde örneklenmediği için uygulama beklenmiyor.

#### Geçiş ölçütleri

- [ ] Negatif görev sayısı alan hatasıyla ilişkilendirilmiş; taban Exception.
- [ ] Error son eki ve sade hata tasarımı gerekçeli.
- [ ] Özel handler yalnız ilgili aileyi, Exception daha genel aileyi yakalıyor; handler sırası doğru.
- [ ] Dosya bulunamaması gibi ilgisiz bir hatanın bu isimle yeniden etiketlenmemesi açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../8.7-defining-clean-up-actions/README.md)
<!-- learning-task:end -->
