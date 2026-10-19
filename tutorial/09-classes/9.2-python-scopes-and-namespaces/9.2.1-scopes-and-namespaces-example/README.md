### 9.2.1. Scopes and Namespaces Example

This is an example demonstrating how to reference the different scopes and namespaces, and how `global` and `nonlocal` affect variable binding:

``` python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```
> Code: [scope_test.py](scope_test.py)

The output of the example code is:

``` text
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

Note how the *local* assignment (which is default) didn't change *scope_test*\'s binding of *spam*. The `nonlocal` assignment changed *scope_test*\'s binding of *spam*, and the `global` assignment changed the module-level binding.

You can also see that there was no previous binding for *spam* before the `global` assignment.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 9.2.1: Kapsam izini tek değişiklikle yeniden çıkar**

**Odak:** Yerel/nonlocal/global atamaların aynı örnekte ayrıştırılması.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:9.2](../README.md).

##### Tek görev

1. README içindeki scope_test örneğinin kopyasında başlangıçtaki spam = "test spam" satırını "start" yap; do_nonlocal içindeki nonlocal bildirimini kaldır.

2. Dört çıktı satırını çalıştırmadan önce çıkar, sonra doğrula.

3. İkinci denemede yalnız bildirimi geri koy ve hangi satırların neden değiştiğini açıkla.

##### Geçiş ölçütleri

- [ ] Bildirim yokken ilk üç dış gözlem start, son modül gözlemi global spam.
- [ ] nonlocal geri geldiğinde ikinci ve üçüncü gözlem nonlocal spam oluyor.
- [ ] Değişim print konumuyla değil atamanın hedef namespace alanıyla açıklanmış.
- [ ] Global atama daha önce modül düzeyinde spam bulunmasa da modül bağını oluşturuyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
