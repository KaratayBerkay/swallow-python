### 7.2.2. Saving structured data with `json`

Strings can easily be written to and read from a file. Numbers take a bit more effort, since the `read()` method only returns strings, which will have to be passed to a function like `int()`, which takes a string like `'123'` and returns its numeric value 123. When you want to save more complex data types like nested lists and dictionaries, parsing and serializing by hand becomes complicated.

Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called [JSON (JavaScript Object Notation)](https://json.org). The standard module called `json` can take Python data hierarchies, and convert them to string representations; this process is called *serializing*. Reconstructing the data from the string representation is called *deserializing*. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

> **Note**
>
> The JSON format is commonly used by modern applications to allow for data exchange. Many programmers are already familiar with it, which makes it a good choice for interoperability.

If you have an object `x`, you can view its JSON string representation with a simple line of code:

``` python
>>> import json
>>> x = [1, 'simple', 'list']
>>> json.dumps(x)
'[1, "simple", "list"]'
```
> Code: [x.py](x.py)

Another variant of the `dumps()` function, called `dump()`, simply serializes the object to a text file. So if `f` is a text file object opened for writing, we can do this:

``` python
json.dump(x, f)
```
> Code: [example_01.py](example_01.py)

To decode the object again, if `f` is a binary file or text file object which has been opened for reading:

``` python
x = json.load(f)
```
> Code: [x_2.py](x_2.py)

> **Note**
>
> JSON files must be encoded in UTF-8, the default encoding for text files.

This simple serialization technique can handle lists and dictionaries, but serializing arbitrary class instances in JSON requires a bit of extra effort. The reference for the `json` module contains an explanation of this.

> **See also**
>
> `pickle` - the pickle module
>
> Contrary to JSON, *pickle* is a protocol which allows the serialization of arbitrarily complex Python objects. As such, it is specific to Python and cannot be used to communicate with applications written in other languages. It is also insecure by default: deserializing pickle data coming from an untrusted source can execute arbitrary code, if the data was crafted by a skilled attacker.

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 7.2.2: Yapılandırılmış veriyi dosyadan geri getir**

**Odak:** JSON serialization/deserialization, dumps/dump/load ve metin/nesne ayrımı.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:7.2.1](../7.2.1-methods-of-file-objects/README.md).
- Ön bilgi: [t:5.5](../../../05-data-structures/5.5-dictionaries/README.md).

##### Tek görev

1. data = {"name": "Ada", "scores": [2, 5], "active": True} verisini önce json.dumps ile metin olarak göster; sonra UTF-8 dosyaya json.dump ile yazıp yeni açılışta json.load ile geri al.

2. Geri gelen veriyle asıl veriyi karşılaştır; scores öğesinin yine liste olarak kullanılabildiğini göster.

3. Kaynaktaki pickle notunun dil bağımlılığı ve güven sınırını sözle açıkla.

##### Geçiş ölçütleri

- [ ] dumps sonucu metin; load sonucu yine sözlük ve içindeki scores liste.
- [ ] dump dosya nesnesiyle, dumps metin üretmek için kullanılmış.
- [ ] Geri gelen değer aslına eşit; yalnız dosyanın görünüşüne bakılarak başarı sayılmamış.
- [ ] Özel sınıf örneklerinin doğrudan aynı yöntemle desteklendiği varsayılmamış; pickle notu kod çalıştırma olasılığıyla ilişkilendirilmiş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Klasörün bütün alt görevleri bittiyse milestone kontrolüne geç.](../README.md#klasör-milestone-görevi)
<!-- learning-task:end -->
