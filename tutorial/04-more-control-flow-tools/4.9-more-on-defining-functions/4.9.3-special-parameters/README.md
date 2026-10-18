### 4.9.3. Special parameters

By default, arguments may be passed to a Python function either by position or explicitly by keyword. For readability and performance, it makes sense to restrict the way arguments can be passed so that a developer need only look at the function definition to determine if items are passed by position, by position or keyword, or by keyword.

A function definition may look like:

``` text
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

where `/` and `*` are optional. If used, these symbols indicate the kind of parameter by how the arguments may be passed to the function: positional-only, positional-or-keyword, and keyword-only. Keyword parameters are also referred to as named parameters.

#### Sections

- [4.9.3.1. Positional-or-Keyword Arguments](4.9.3.1-positional-or-keyword-arguments/README.md)
- [4.9.3.2. Positional-Only Parameters](4.9.3.2-positional-only-parameters/README.md)
- [4.9.3.3. Keyword-Only Arguments](4.9.3.3-keyword-only-arguments/README.md)
- [4.9.3.4. Function Examples](4.9.3.4-function-examples/README.md)
- [4.9.3.5. Recap](4.9.3.5-recap/README.md)
