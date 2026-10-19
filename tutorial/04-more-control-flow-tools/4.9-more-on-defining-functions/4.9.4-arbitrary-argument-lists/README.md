### 4.9.4. Arbitrary Argument Lists

Finally, the least frequently used option is to specify that a function can be called with an arbitrary number of arguments. These arguments will be wrapped up in a tuple (see Tuples and Sequences). Before the variable number of arguments, zero or more normal arguments may occur.

``` python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```
> Code: [write_multiple_items.py](write_multiple_items.py)

Normally, these *variadic* arguments will be last in the list of formal parameters, because they scoop up all remaining input arguments that are passed to the function. Any formal parameters which occur after the `*args` parameter are 'keyword-only' arguments, meaning that they can only be used as keywords rather than positional arguments.

``` python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```
> Code: [concat.py](concat.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.4: Değişken sayıda parçayı birleştir**

**Odak:** `*args` ile kalan konumsalları toplama ve sonrasındaki yalnız anahtarlı parametre.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.9.3.5](../4.9.3-special-parameters/4.9.3.5-recap/README.md).

##### Tek görev

1. Bölümdeki concat örneğinden yola çıkarak join_parts(prefix, `*parts`, sep="/") yaz. prefix ile başla; ardından parts öğelerini döngüyle, aralara sep koyarak ekle.

2. Sıfır, bir ve üç ek parça ile; hem varsayılan hem özel ayraçla çağır.

3. Sonuna konumsal verilen ":" değerinin neden sep değil bir parça olduğunu göster.

##### Geçiş ölçütleri

- [ ] join_parts("root") root; join_parts("root", "a", "b") root/a/b.
- [ ] sep=":" ile root:a:b elde ediliyor.
- [ ] parts bir tuple içinde toplanıyor, prefix bu grubun dışında kalıyor.
- [ ] sep yalnız anahtarla değiştirilebiliyor; konumsal ":" parts içine gidiyor.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.5-unpacking-argument-lists/README.md)
<!-- learning-task:end -->
