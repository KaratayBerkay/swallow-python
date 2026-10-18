## 5.7. Package Relative Imports

Relative imports use leading dots. A single leading dot indicates a relative import, starting with the current package. Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after the first. For example, given the following package layout:

``` python
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```
> Code: [example_01.py](example_01.py)

In either `subpackage1/moduleX.py` or `subpackage1/__init__.py`, the following are valid relative imports:

``` python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```
> Code: [spam.py](spam.py)

Absolute imports may use either the `import <>` or `from <> import <>` syntax, but relative imports may only use the second form; the reason for this is that:

``` python
import XXX.YYY.ZZZ
```
> Code: [xxx.py](xxx.py)

should expose `XXX.YYY.ZZZ` as a usable expression, but .moduleY is not a valid expression.
