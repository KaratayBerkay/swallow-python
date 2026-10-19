## `eval()`

```
eval(source, /, globals=None, locals=None)
```

- **source** ([str](../str/README.md) | [code object](https://docs.python.org/3.15/reference/datamodel.html#code-objects)) – A Python expression.

- **globals** ([dict](../dict/README.md) | [frozendict](../frozendict/README.md) | `None`) – The global namespace (default: `None`).

- **locals** ([mapping](https://docs.python.org/3.15/glossary.html#term-mapping) | `None`) – The local namespace (default: `None`).

- **returns** – The result of the evaluated expression.

- **raises** – Syntax errors are reported as exceptions.

> **Warning**
>
> This function executes arbitrary code. Calling it with
> untrusted user-supplied input will lead to security vulnerabilities.

The *source* argument is parsed and evaluated as a Python expression
(technically speaking, an [expression list](https://docs.python.org/3.15/reference/expressions.html#exprlists))
using the *globals* and *locals* mappings as global and local namespace.
If the *globals* dictionary is present and does not contain a value for the
key `__builtins__`, a
reference to the dictionary of the built-in module [builtins](https://docs.python.org/3.15/library/builtins.html#module-builtins) is
inserted under that key before *source* is parsed.
Overriding `__builtins__` can be used to restrict or change the available
names, but this is **not** a security mechanism: the executed code can
still access all builtins.
If the *locals* mapping is omitted it defaults to the
*globals* dictionary.  If both mappings are omitted, the source is
executed with the *globals* and *locals* in the environment where
eval() is called.  Note, *eval()* will only have access to the
[nested scopes](https://docs.python.org/3.15/glossary.html#term-nested-scope) (non-locals) in the enclosing
environment if they are already referenced in the scope that is calling
eval() (e.g. via a `nonlocal` statement).

Example:

``` python
>>> x = 1
>>> eval('x+1')
2
```
> Code: [example_01.py](example_01.py)

``` python
>>> eval("1, 2")
(1, 2)
```
> Code: [example_02.py](example_02.py)

This function can also be used to execute arbitrary code objects (such as
those created by [compile()](../compile/README.md)).  In this case, pass a code object instead
of a string.  If the code object has been compiled with `'exec'` as the
*mode* argument, eval()'s return value will be `None`.

Hints: dynamic execution of statements is supported by the [exec()](../exec/README.md)
function.  The [globals()](../globals/README.md) and [locals()](../locals/README.md) functions
return the current global and local dictionary, respectively, which may be
useful to pass around for use by eval() or [exec()](../exec/README.md).

If the given source is a string, then leading and trailing spaces and tabs
are stripped.

See [ast.literal_eval()](https://docs.python.org/3.15/library/ast.html#ast.literal_eval) for a function to evaluate strings
with expressions containing only literals.

Raises an [auditing event](https://docs.python.org/3.15/library/sys.html#auditing) `exec` with the code object
as the argument. Code compilation events may also be raised.

> *Changed in version 3.13:* The *globals* and *locals* arguments can now be passed as keywords.

> *Changed in version 3.13:* The semantics of the default *locals* namespace have been adjusted as
> described for the [locals()](../locals/README.md) builtin.

> *Changed in version 3.15:* *globals* can now be a [frozendict](../frozendict/README.md).

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.22: eval sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

#### Tek görev

Yalnız sabit `"x + y"` ifadesini globals={"x":2,"y":3}, locals={"x":8} ile değerlendir. Atama içeren `"x = 4"` metnini ayrıca dene. İsim arama önceliği ve ifade kısıtını açıkla.

#### Geçiş ölçütleri

- [ ] Sonuç 11 olur; x localstan, y globalstan bulunur.
- [ ] Atama SyntaxError verir; eval kullanıcı girdisi çalıştırmak için kullanılmamıştır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../exec/README.md)
<!-- learning-task:end -->
