### 4.9.1. Default Argument Values

The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined to allow. For example:

``` python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```
> Code: [ask_ok.py](ask_ok.py)

This function can be called in several ways:

- giving only the mandatory argument: `ask_ok('Do you really want to quit?')`

- giving one of the optional arguments: `ask_ok('OK to overwrite the file?', 2)`

- or even giving all arguments: `ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')`

This example also introduces the `in` keyword. This tests whether or not a sequence contains a certain value.

The default values are evaluated at the point of function definition in the *defining* scope, so that

``` python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```
> Code: [f.py](f.py)

will print `5`.

**Important warning:** The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

``` python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
```
> Code: [f_2.py](f_2.py)

This will print

``` python
[1]
[1, 2]
[1, 2, 3]
```
> Code: [example_01.py](example_01.py)

If you don't want the default to be shared between subsequent calls, you can write the function like this instead:

``` python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
> Code: [f_3.py](f_3.py)

<!-- learning-task:start -->
#### Bölüm görevi

**Görev 4.9.1: Varsayılan değerin ömrünü düzelt**

**Odak:** Zorunlu/isteğe bağlı argüman, tanım anında değerlendirme ve paylaşılan değiştirilebilir varsayılan.

##### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:4.8](../../4.8-defining-functions/README.md).
- Ön bilgi: [t:3.1.3](../../../03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md).

##### Tek görev

1. README içindeki f(a, L=[]) örneğini 4 ve 9 ile art arda çağırıp liste paylaşımını göster.

2. Aynı işlevi varsayılan listesi çağrılar arasında paylaşılmayacak biçimde düzelt; ayrıca açıkça bir liste verilirse o listeye eklemeyi sürdürsün.

3. Ayrı bir örnekte seed = 4 iken def show(value=seed) tanımla, seed = 9 yapıp argümansız çağrının sonucunu açıkla. ask_ok örneğinde bir, iki ve üç argümanlı çağrıların hangi varsayılanları kullandığını not et.

##### Geçiş ölçütleri

- [ ] İlk sürümün ikinci çağrısında [4, 9] oluşuyor.
- [ ] Düzeltilmiş sürümün argümansız liste kullanan çağrıları bağımsız; verilen liste ise aynı nesne olarak değişiyor.
- [ ] show varsayılanının 4 kalması tanım zamanı ile açıklanmış.
- [ ] ask_ok zorunlu prompt ve iki varsayılan bakımından doğru eşleştirilmiş; in üyelik denetimi olarak okunmuş.

[Değerlendirme yöntemi](../../../../DEGERLENDIRME.md) · [Sıra](../../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9.2-keyword-arguments/README.md)
<!-- learning-task:end -->
