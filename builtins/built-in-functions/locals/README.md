## `locals()`

```
locals()
```

Return a mapping object representing the current local symbol table, with
variable names as the keys, and their currently bound references as the
values.

At module scope, as well as when using [exec()](../exec/README.md) or [eval()](../eval/README.md) with
a single namespace, this function returns the same namespace as
[globals()](../globals/README.md).

At class scope, it returns the namespace that will be passed to the
metaclass constructor.

When using `exec()` or `eval()` with separate local and global
arguments, it returns the local namespace passed in to the function call.

In all of the above cases, each call to `locals()` in a given frame of
execution will return the *same* mapping object. Changes made through
the mapping object returned from `locals()` will be visible as assigned,
reassigned, or deleted local variables, and assigning, reassigning, or
deleting local variables will immediately affect the contents of the
returned mapping object.

In an [optimized scope](https://docs.python.org/3.15/glossary.html#term-optimized-scope) (including functions, generators, and
coroutines), each call to `locals()` instead returns a fresh dictionary
containing the current bindings of the function's local variables and any
nonlocal cell references. In this case, name binding changes made via the
returned dict are *not* written back to the corresponding local variables
or nonlocal cell references, and assigning, reassigning, or deleting local
variables and nonlocal cell references does *not* affect the contents
of previously returned dictionaries.

Calling `locals()` as part of a comprehension in a function, generator, or
coroutine is equivalent to calling it in the containing scope, except that
the comprehension's initialised iteration variables will be included. In
other scopes, it behaves as if the comprehension were running as a nested
function.

Calling `locals()` as part of a generator expression is equivalent to
calling it in a nested generator function.

> *Changed in version 3.12:* The behaviour of `locals()` in a comprehension has been updated as
> described in [PEP 709](https://peps.python.org/pep-709/).

> *Changed in version 3.13:* As part of [PEP 667](https://peps.python.org/pep-667/), the semantics of mutating the mapping objects
> returned from this function are now defined. The behavior in
> [optimized scopes](https://docs.python.org/3.15/glossary.html#term-optimized-scope) is now as described above.
> Aside from being defined, the behaviour in other scopes remains
> unchanged from previous versions.

<!-- learning-task:start -->
### Bölüm görevi

**Görev b:3.43: locals sözleşmesini uygula**

#### Önce

[t:4.8](../../../tutorial/04-more-control-flow-tools/4.8-defining-functions/README.md) ve bu sayfanın açıklama/örnekleri.

Sürüm: Python 3.13 veya üzeri. Daha eski yorumlayıcıda yalnız bu sürüme bağlı kısmı gerekçeli yazılı iz ile çözebilirsin; çalıştırma kanıtını bekleyen olarak kaydet.

#### Tek görev

Python 3.13+ için bir fonksiyonda `x=1; a=locals(); a["x"]=9; b=locals()` satırlarını izle. x, a["x"], b["x"] ve `a is b` değerlerini raporla. Modül düzeyindeki locals davranışıyla karşılaştır.

#### Geçiş ölçütleri

- [ ] Fonksiyonda değerler 1, 9, 1, False olur; a değişikliği x adını yeniden bağlamaz.
- [ ] Modül düzeyinde locals global namespace ile aynıdır.

[Değerlendirme yöntemi](../../../DEGERLENDIRME.md)

Ayrı dosya: [bölüm görevi](TASK.md).

**Sonraki adım:** [Görev geçiş ölçütlerini sağladıktan sonra sıradaki anlatımı oku.](../map/README.md)
<!-- learning-task:end -->
