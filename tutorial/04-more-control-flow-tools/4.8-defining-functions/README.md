## 4.8. Defining Functions

We can create a function that writes the Fibonacci series to an arbitrary boundary:

``` python
>>> def fib(n):    # write Fibonacci series less than n
...     """Print a Fibonacci series less than n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```
> Code: [fib.py](fib.py)

The keyword `def` introduces a function *definition*. It must be followed by the function name and the parenthesized list of formal parameters. The statements that form the body of the function start at the next line, and must be indented.

The first statement of the function body can optionally be a string literal; this string literal is the function's documentation string, or *docstring*. (More about docstrings can be found in the section Documentation Strings.) There are tools which use docstrings to automatically produce online or printed documentation, or to let the user interactively browse through code; it's good practice to include docstrings in code that you write, so make a habit of it.

The *execution* of a function introduces a new symbol table used for the local variables of the function. More precisely, all variable assignments in a function store the value in the local symbol table; whereas variable references first look in the local symbol table, then in the local symbol tables of enclosing functions, then in the global symbol table, and finally in the table of built-in names. Thus, global variables and variables of enclosing functions cannot be directly assigned a value within a function (unless, for global variables, named in a `global` statement, or, for variables of enclosing functions, named in a `nonlocal` statement), although they may be referenced.

The actual parameters (arguments) to a function call are introduced in the local symbol table of the called function when it is called; thus, arguments are passed using *call by value* (where the *value* is always an object *reference*, not the value of the object). (Actually, *call by object reference* would be a better description, since if a mutable object is passed, the caller will see any changes the callee makes to it (items inserted into a list).) When a function calls another function, or calls itself recursively, a new local symbol table is created for that call.

A function definition associates the function name with the function object in the current symbol table. The interpreter recognizes the object pointed to by that name as a user-defined function. Other names can also point to that same function object and can also be used to access the function:

``` python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```
> Code: [f.py](f.py)

Coming from other languages, you might object that `fib` is not a function but a procedure since it doesn't return a value. In fact, even functions without a `return` statement do return a value, albeit a rather boring one. This value is called `None` (it's a built-in name). Writing the value `None` is normally suppressed by the interpreter if it would be the only value written. You can see it if you really want to using `print()`:

``` python
>>> fib(0)
>>> print(fib(0))
None
```
> Code: [example_01.py](example_01.py)

It is simple to write a function that returns a list of the numbers of the Fibonacci series, instead of printing it:

``` python
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```
> Code: [fib2.py](fib2.py)

This example, as usual, demonstrates some new Python features:

- The `return` statement returns with a value from a function. `return` without an expression argument returns `None`. Falling off the end of a function also returns `None`.

- The statement `result.append(a)` calls a *method* of the list object `result`. A method is a function that 'belongs' to an object and is named `obj.methodname`, where `obj` is some object (this may be an expression), and `methodname` is the name of a method that is defined by the object's type. Different types define different methods. Methods of different types may have the same name without causing ambiguity. (It is possible to define your own object types and methods, using *classes*, see Classes) The method `append()` shown in the example is defined for list objects; it adds a new element at the end of the list. In this example it is equivalent to `result = result + [a]`, but more efficient.

<!-- learning-task:start -->
### Bölüm görevi

**Görev 4.8: Yazdırılan sonuçla dönen sonucu ayır**

**Odak:** def/çağrı, parametre, yerel adlar, return/None, fonksiyon alias ve listeye append.

#### Önce

- Bu bölümün [anlatımını ve içindeki örnekleri](README.md) tamamla.
- Ön bilgi: [t:3.2](../../03-an-informal-introduction-to-python/3.2-first-steps-towards-programming/README.md).
- Ön bilgi: [t:4.6](../4.6-pass-statements/README.md).

#### Tek görev

1. limit altındaki çift sayıları liste olarak döndüren even_numbers(limit) yaz; 0 ile başlatıp while içinde 2 ekleyebilirsin.

2. Kısa bir docstring ekle. f = even_numbers ile ikinci bir ad ver. 0, 1 ve 7 için sonuçları al.

3. Ardından yalnızca aynı sayıları yazdıran, return kullanmayan bir sürüm yaz ve print ile dönüşünü göster.

4. Dışarıda limit = 100 varken fonksiyon parametresinin neden onu değiştirmediğini açıkla.

#### Geçiş ölçütleri

- [ ] Sonuçlar [], [0], [0, 2, 4, 6]; sınır dışarıda kalıyor.
- [ ] f aynı fonksiyonu çağırıyor; f ile çağrının sonucu birbirinden ayrılmış.
- [ ] Yazdıran sürümün dönüşü None; return ifadesiz kullanıldığında da aynı.
- [ ] Parametre ve gövde içindeki atamalar yerel; fonksiyonun gövdesi tanımda değil çağrıda yürütülüyor.
- [ ] Her çağrıda sonuç listesinin yeniden oluştuğu ve append ile biriktiği açıklanmış.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md) · [Sıra](../../../TASKS.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../4.9-more-on-defining-functions/4.9.1-default-argument-values/README.md)
<!-- learning-task:end -->
