# Python Tutorial

A folder-by-folder map of the official Python tutorial (chapters 2–16). Every numbered folder is one tutorial section; nested folders are its subsections. Each section folder contains a `README.md` with the full explanation plus runnable `.py` example files taken from the tutorial.

## Contents

### [2. Using the Python Interpreter](02-using-the-python-interpreter/README.md)
How to launch Python, run scripts, and configure the interpreter.

- [2.1. Invoking the Interpreter](02-using-the-python-interpreter/2.1-invoking-the-interpreter/README.md) — starting the interpreter and the flags it accepts.
  - [2.1.1. Argument Passing](02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.1-argument-passing/README.md) — how `python script.py arg1 arg2` reaches your program via `sys.argv`.
  - [2.1.2. Interactive Mode](02-using-the-python-interpreter/2.1-invoking-the-interpreter/2.1.2-interactive-mode/README.md) — the REPL, echo examples, and `the_world_is_flat.py`.
- [2.2. The Interpreter and Its Environment](02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/README.md) — details about the running interpreter.
  - [2.2.1. Source Code Encoding](02-using-the-python-interpreter/2.2-the-interpreter-and-its-environment/2.2.1-source-code-encoding/README.md) — declaring non-UTF-8 source files with encoding cookies (`example_01.py`–`example_03.py`).

### [3. An Informal Introduction to Python](03-an-informal-introduction-to-python/README.md)
Your first taste of the language: numbers, text, lists, and a first program.

- [3.1. Using Python as a Calculator](03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/README.md) — trying things out interactively.
  - [3.1.1. Numbers](03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.1-numbers/README.md) — integers, floats, `//`, `**`, and `math`/`random` (`tax.py`, `width.py`).
  - [3.1.2. Text](03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.2-text/README.md) — strings, slicing, escapes, `str.join`/`format` (`s.py`, `prefix.py`, `word.py`).
  - [3.1.3. Lists](03-an-informal-introduction-to-python/3.1-using-python-as-a-calculator/3.1.3-lists/README.md) — indexing, nesting, mutation (`squares.py`, `cubes.py`, `rgb.py`).
- [3.2. First Steps Towards Programming](03-an-informal-introduction-to-python/3.2-first-steps-towards-programming/README.md) — Fibonacci, loops, and your first real scripts.

### [4. More Control Flow Tools](04-more-control-flow-tools/README.md)
Branching, looping, and defining functions.

- [4.1. `if` Statements](04-more-control-flow-tools/4.1-if-statements/README.md) — `if`/`elif`/`else` chains.
- [4.2. `for` Statements](04-more-control-flow-tools/4.2-for-statements/README.md) — iterating over sequences (`users.py`, `words.py`).
- [4.3. The `range()` Function](04-more-control-flow-tools/4.3-the-range-function/README.md) — generating number sequences for loops.
- [4.4. `break` and `continue` Statements](04-more-control-flow-tools/4.4-break-and-continue-statements/README.md) — escaping or skipping loop iterations.
- [4.5. `else` Clauses on Loops](04-more-control-flow-tools/4.5-else-clauses-on-loops/README.md) — the `for … else` / `while … else` idiom.
- [4.6. `pass` Statements](04-more-control-flow-tools/4.6-pass-statements/README.md) — placeholder bodies (`initlog.py`, `my_empty_class.py`).
- [4.7. `match` Statements](04-more-control-flow-tools/4.7-match-statements/README.md) — structural pattern matching (`http_error.py`, `init.py`).
- [4.8. Defining Functions](04-more-control-flow-tools/4.8-defining-functions/README.md) — `def`, return values, default `None` (`fib.py`, `fib2.py`).
- [4.9. More on Defining Functions](04-more-control-flow-tools/4.9-more-on-defining-functions/README.md) — everything about arguments and function design.
  - [4.9.1. Default Argument Values](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.1-default-argument-values/README.md) — defaults and the mutable-default pitfall (`ask_ok.py`).
  - [4.9.2. Keyword Arguments](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.2-keyword-arguments/README.md) — calling with names (`parrot.py`, `cheeseshop.py`).
  - [4.9.3. Special Parameters](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/README.md) — controlling how arguments are interpreted.
    - [4.9.3.1. Positional-or-Keyword Arguments](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.1-positional-or-keyword-arguments/README.md) — the default `/`-free style.
    - [4.9.3.2. Positional-Only Parameters](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.2-positional-only-parameters/README.md) — the `/` separator.
    - [4.9.3.3. Keyword-Only Arguments](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.3-keyword-only-arguments/README.md) — the `*` separator.
    - [4.9.3.4. Function Examples](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.4-function-examples/README.md) — side-by-side signature examples (`standard_arg.py`, `foo.py`).
    - [4.9.3.5. Recap](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.3-special-parameters/4.9.3.5-recap/README.md) — a quick summary table of the three kinds.
  - [4.9.4. Arbitrary Argument Lists](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.4-arbitrary-argument-lists/README.md) — `*args` and `**kwargs` (`concat.py`, `write_multiple_items.py`).
  - [4.9.5. Unpacking Argument Lists](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.5-unpacking-argument-lists/README.md) — calling with `*` and `**` (`args.py`, `parrot.py`).
  - [4.9.6. Lambda Expressions](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.6-lambda-expressions/README.md) — small anonymous functions (`make_incrementor.py`, `pairs.py`).
  - [4.9.7. Documentation Strings](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.7-documentation-strings/README.md) — docstrings and `__doc__`.
  - [4.9.8. Function Annotations](04-more-control-flow-tools/4.9-more-on-defining-functions/4.9.8-function-annotations/README.md) — type hints as metadata.
- [4.10. Intermezzo: Coding Style](04-more-control-flow-tools/4.10-intermezzo-coding-style/README.md) — PEP 8 and why readability counts.

### [5. Data Structures](05-data-structures/README.md)
Lists, tuples, sets, dicts, and how to loop over them.

- [5.1. More on Lists](05-data-structures/5.1-more-on-lists/README.md) — methods, slicing, copying (`fruits.py`).
  - [5.1.1. Using Lists as Stacks](05-data-structures/5.1-more-on-lists/5.1.1-using-lists-as-stacks/README.md) — LIFO with `append`/`pop`.
  - [5.1.2. Using Lists as Queues](05-data-structures/5.1-more-on-lists/5.1.2-using-lists-as-queues/README.md) — FIFO with `collections.deque`.
  - [5.1.3. List Comprehensions](05-data-structures/5.1-more-on-lists/5.1.3-list-comprehensions/README.md) — compact loops and filters (`squares.py`, `combs.py`, `vec.py`).
  - [5.1.4. Nested List Comprehensions](05-data-structures/5.1-more-on-lists/5.1.4-nested-list-comprehensions/README.md) — matrices and transposing (`matrix.py`, `transposed.py`).
  - [5.1.5. Unpacking in Lists and List Comprehensions](05-data-structures/5.1-more-on-lists/5.1.5-unpacking-in-lists-and-list-comprehensions/README.md) — `*`/`**` inside comprehensions.
- [5.2. The `del` Statement](05-data-structures/5.2-the-del-statement/README.md) — removing items by index or slice.
- [5.3. Tuples and Sequences](05-data-structures/5.3-tuples-and-sequences/README.md) — immutability, packing/unpacking (`t.py`, `empty.py`).
- [5.4. Sets](05-data-structures/5.4-sets/README.md) — unordered uniques and set algebra (`basket.py`, `a.py`).
- [5.5. Dictionaries](05-data-structures/5.5-dictionaries/README.md) — key/value maps (`tel.py`, `odds.py`).
- [5.6. Looping Techniques](05-data-structures/5.6-looping-techniques/README.md) — `enumerate`, `zip`, `reversed`, `.items()` (`knights.py`, `zip.py`).
- [5.7. More on Conditions](05-data-structures/5.7-more-on-conditions/README.md) — chained comparisons, `in`, `not in`, `and`/`or` short-circuiting.
- [5.8. Comparing Sequences and Other Types](05-data-structures/5.8-comparing-sequences-and-other-types/README.md) — how `<`, `==`, and mixed-type comparison work.

### [6. Modules](06-modules/README.md)
Splitting code across files and packaging it up.

- [6.1. More on Modules](06-modules/6.1-more-on-modules/README.md) — `import`, `from … import`, `import as` (`fibo.py`, `fib.py`).
  - [6.1.1. Executing Modules as Scripts](06-modules/6.1-more-on-modules/6.1.1-executing-modules-as-scripts/README.md) — the `__name__ == "__main__"` guard.
  - [6.1.2. The Module Search Path](06-modules/6.1-more-on-modules/6.1.2-the-module-search-path/README.md) — where Python looks for modules (`sys.path`).
  - [6.1.3. "Compiled" Python Files](06-modules/6.1-more-on-modules/6.1.3-compiled-python-files/README.md) — `__pycache__` and `.pyc` files.
- [6.2. Standard Modules](06-modules/6.2-standard-modules/README.md) — `sys` and friends shipped with Python.
- [6.3. The `dir()` Function](06-modules/6.3-the-dir-function/README.md) — introspecting modules and objects.
- [6.4. Packages](06-modules/6.4-packages/README.md) — hierarchical packages with `__init__.py` (see the `sound/` example tree).
  - [6.4.1. Importing \* From a Package](06-modules/6.4-packages/6.4.1-importing-from-a-package/README.md) — `__all__`, namespace packages, and its own `sound/` fixture.
  - [6.4.2. Intra-package References](06-modules/6.4-packages/6.4.2-intra-package-references/README.md) — relative imports inside a package (another `sound/` fixture).

### [7. Input and Output](07-input-and-output/README.md)
Showing data to users and reading data back.

- [7.1. Fancier Output Formatting](07-input-and-output/7.1-fancier-output-formatting/README.md) — ways to format output.
  - [7.1.1. Formatted String Literals](07-input-and-output/7.1-fancier-output-formatting/7.1.1-formatted-string-literals/README.md) — f-strings.
  - [7.1.2. The `str.format()` Method](07-input-and-output/7.1-fancier-output-formatting/7.1.2-the-string-format-method/README.md) — `"{0} of {1}".format(...)` and format specs.
  - [7.1.3. Manual String Formatting](07-input-and-output/7.1-fancier-output-formatting/7.1.3-manual-string-formatting/README.md) — `str.zfill`/manual padding.
  - [7.1.4. Old String Formatting](07-input-and-output/7.1-fancier-output-formatting/7.1.4-old-string-formatting/README.md) — the `%` operator.
- [7.2. Reading and Writing Files](07-input-and-output/7.2-reading-and-writing-files/README.md) — `open()`, modes, and context managers.
  - [7.2.1. Methods of File Objects](07-input-and-output/7.2-reading-and-writing-files/7.2.1-methods-of-file-objects/README.md) — `read`, `readline`, `write`, `seek`.
  - [7.2.2. Saving Structured Data with `json`](07-input-and-output/7.2-reading-and-writing-files/7.2.2-saving-structured-data-with-json/README.md) — `json.dumps`/`json.load` for serialization.

### [8. Errors and Exceptions](08-errors-and-exceptions/README.md)
What goes wrong, why, and how to handle it.

- [8.1. Syntax Errors](08-errors-and-exceptions/8.1-syntax-errors/README.md) — parse-time mistakes.
- [8.2. Exceptions](08-errors-and-exceptions/8.2-exceptions/README.md) — runtime errors and their types.
- [8.3. Handling Exceptions](08-errors-and-exceptions/8.3-handling-exceptions/README.md) — `try`/`except`/`else`/`finally`.
- [8.4. Raising Exceptions](08-errors-and-exceptions/8.4-raising-exceptions/README.md) — `raise` and re-raising.
- [8.5. Exception Chaining](08-errors-and-exceptions/8.5-exception-chaining/README.md) — `raise … from …` and implicit chaining.
- [8.6. User-defined Exceptions](08-errors-and-exceptions/8.6-user-defined-exceptions/README.md) — subclassing `Exception`.
- [8.7. Defining Clean-up Actions](08-errors-and-exceptions/8.7-defining-clean-up-actions/README.md) — `finally`.
- [8.8. Predefined Clean-up Actions](08-errors-and-exceptions/8.8-predefined-clean-up-actions/README.md) — `with` as automatic cleanup.
- [8.9. Raising and Handling Multiple Unrelated Exceptions](08-errors-and-exceptions/8.9-raising-and-handling-multiple-unrelated-exceptions/README.md) — `except (A, B)` and multiple `except` blocks.
- [8.10. Enriching Exceptions with Notes](08-errors-and-exceptions/8.10-enriching-exceptions-with-notes/README.md) — `add_note()` for extra context.

### [9. Classes](09-classes/README.md)
Objects, namespaces, inheritance, iterators, and generators.

- [9.1. A Word About Names and Objects](09-classes/9.1-a-word-about-names-and-objects/README.md) — names as bindings to objects.
- [9.2. Python Scopes and Namespaces](09-classes/9.2-python-scopes-and-namespaces/README.md) — LEGB rule, `global` and `nonlocal`.
  - [9.2.1. Scopes and Namespaces Example](09-classes/9.2-python-scopes-and-namespaces/9.2.1-scopes-and-namespaces-example/README.md) — a worked demonstration.
- [9.3. A First Look at Classes](09-classes/9.3-a-first-look-at-classes/README.md) — introducing `class`.
  - [9.3.1. Class Definition Syntax](09-classes/9.3-a-first-look-at-classes/9.3.1-class-definition-syntax/README.md) — the `class` statement.
  - [9.3.2. Class Objects](09-classes/9.3-a-first-look-at-classes/9.3.2-class-objects/README.md) — attributes and methods on the class itself.
  - [9.3.3. Instance Objects](09-classes/9.3-a-first-look-at-classes/9.3.3-instance-objects/README.md) — per-object state.
  - [9.3.4. Method Objects](09-classes/9.3-a-first-look-at-classes/9.3.4-method-objects/README.md) — why `self` is passed automatically.
  - [9.3.5. Class and Instance Variables](09-classes/9.3-a-first-look-at-classes/9.3.5-class-and-instance-variables/README.md) — shared vs. per-instance data.
- [9.4. Random Remarks](09-classes/9.4-random-remarks/README.md) — small design notes and idioms.
- [9.5. Inheritance](09-classes/9.5-inheritance/README.md) — derived classes (`modname/` shows module-qualified names).
  - [9.5.1. Multiple Inheritance](09-classes/9.5-inheritance/9.5.1-multiple-inheritance/README.md) — MRO and diamond shapes.
- [9.6. Private Variables](09-classes/9.6-private-variables/README.md) — name mangling and `_leading_underscore`.
- [9.7. Odds and Ends](09-classes/9.7-odds-and-ends/README.md) — dataclass-like helpers, `__slots__` notes.
- [9.8. Iterators](09-classes/9.8-iterators/README.md) — `__iter__` / `__next__`.
- [9.9. Generators](09-classes/9.9-generators/README.md) — `yield` and lazy sequences.
- [9.10. Generator Expressions](09-classes/9.10-generator-expressions/README.md) — generator comprehension syntax.

### [10. Brief Tour of the Standard Library](10-brief-tour-of-the-standard-library/README.md)
A showcase of batteries that come with Python.

- [10.1. Operating System Interface](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/README.md) — `os`, `shutil`, `pathlib` (contains a sample `server/`, `build/`, `installdir/` layout used by the examples).
- [10.2. File Wildcards](10-brief-tour-of-the-standard-library/10.2-file-wildcards/README.md) — `glob` and `fnmatch`.
- [10.3. Command-line Arguments](10-brief-tour-of-the-standard-library/10.3-command-line-arguments/README.md) — `argparse` and `sys.argv`.
- [10.4. Error Output Redirection and Program Termination](10-brief-tour-of-the-standard-library/10.4-error-output-redirection-and-program-termination/README.md) — `sys.stderr` and `sys.exit`.
- [10.5. String Pattern Matching](10-brief-tour-of-the-standard-library/10.5-string-pattern-matching/README.md) — `re` regular expressions.
- [10.6. Mathematics](10-brief-tour-of-the-standard-library/10.6-mathematics/README.md) — `math`, `random`, `statistics`.
- [10.7. Internet Access](10-brief-tour-of-the-standard-library/10.7-internet-access/README.md) — `urllib.request`, `requests`-style access, `smtplib`.
- [10.8. Dates and Times](10-brief-tour-of-the-standard-library/10.8-dates-and-times/README.md) — `datetime`, `time`, `calendar`.
- [10.9. Data Compression](10-brief-tour-of-the-standard-library/10.9-data-compression/README.md) — `zlib`, `gzip`, `bz2`, `lzma`, `zipfile`, `tarfile`.
- [10.10. Performance Measurement](10-brief-tour-of-the-standard-library/10.10-performance-measurement/README.md) — `timeit`, `profile`, `cProfile`.
- [10.11. Quality Control](10-brief-tour-of-the-standard-library/10.11-quality-control/README.md) — `doctest` and `unittest`.
- [10.12. Batteries Included](10-brief-tour-of-the-standard-library/10.12-batteries-included/README.md) — a summary of what ships in the standard library.

### [11. Brief Tour of the Standard Library — Part II](11-brief-tour-of-the-standard-library-part-ii/README.md)
Advanced standard-library modules.

- [11.1. Output Formatting](11-brief-tour-of-the-standard-library-part-ii/11.1-output-formatting/README.md) — `textwrap`, `pprint`.
- [11.2. Templating](11-brief-tour-of-the-standard-library-part-ii/11.2-templating/README.md) — the `string.Template` module.
- [11.3. Working with Binary Data Record Layouts](11-brief-tour-of-the-standard-library-part-ii/11.3-working-with-binary-data-record-layouts/README.md) — the `struct` module.
- [11.4. Multi-Threading](11-brief-tour-of-the-standard-library-part-ii/11.4-multi-threading/README.md) — `queue`, `threading`, the GIL.
- [11.5. Logging](11-brief-tour-of-the-standard-library-part-ii/11.5-logging/README.md) — the `logging` package.
- [11.6. Weak References](11-brief-tour-of-the-standard-library-part-ii/11.6-weak-references/README.md) — `weakref` and garbage collection.
- [11.7. Tools for Working with Lists](11-brief-tour-of-the-standard-library-part-ii/11.7-tools-for-working-with-lists/README.md) — `array`, `collections`, `heapq`, `bisect`.
- [11.8. Decimal Floating-Point Arithmetic](11-brief-tour-of-the-standard-library-part-ii/11.8-decimal-floating-point-arithmetic/README.md) — the `decimal` module.

### [12. Virtual Environments and Packages](12-virtual-environments-and-packages/README.md)
Isolating project dependencies.

- [12.1. Introduction](12-virtual-environments-and-packages/12.1-introduction/README.md) — why environments exist.
- [12.2. Creating Virtual Environments](12-virtual-environments-and-packages/12.2-creating-virtual-environments/README.md) — `python -m venv` (this repo uses `uv`, see `pyproject.toml` and `.venv`).
- [12.3. Managing Packages with pip](12-virtual-environments-and-packages/12.3-managing-packages-with-pip/README.md) — `pip install`, `requirements.txt`.

### [13. What Now?](13-what-now/README.md)
Where to go after finishing the tutorial (no subsections).

### [14. Interactive Input Editing and History Substitution](14-interactive-input-editing-and-history-substitution/README.md)
Making the REPL nicer to use.

- [14.1. Tab Completion and History Editing](14-interactive-input-editing-and-history-substitution/14.1-tab-completion-and-history-editing/README.md) — readline support in the interpreter.
- [14.2. Alternatives to the Interactive Interpreter](14-interactive-input-editing-and-history-substitution/14.2-alternatives-to-the-interactive-interpreter/README.md) — IPython, bpython, and other front ends.

### [15. Floating-Point Arithmetic: Issues and Limitations](15-floating-point-arithmetic-issues-and-limitations/README.md)
Why `0.1 + 0.2 != 0.3`.

- [15.1. Representation Error](15-floating-point-arithmetic-issues-and-limitations/15.1-representation-error/README.md) — binary fractions and `Decimal`/`Fraction` workarounds.

### [16. Appendix](16-appendix/README.md)
Reference material for the interactive interpreter.

- [16.1. Interactive Mode](16-appendix/16.1-interactive-mode/README.md) — interactive etiquette and behavior.
  - [16.1.1. Error Handling](16-appendix/16.1-interactive-mode/16.1.1-error-handling/README.md) — what the REPL prints on failure.
  - [16.1.2. Executable Python Scripts](16-appendix/16.1-interactive-mode/16.1.2-executable-python-scripts/README.md) — shebang lines (`#!/usr/bin/env python3`).
  - [16.1.3. The Interactive Startup File](16-appendix/16.1-interactive-mode/16.1.3-the-interactive-startup-file/README.md) — `PYTHONSTARTUP`.
  - [16.1.4. The Customization Modules](16-appendix/16.1-interactive-mode/16.1.4-the-customization-modules/README.md) — `readline` and `rlcompleter` config.

## Non-documentation folders

These directories hold example fixtures referenced by the sections above; they have no `README.md` of their own:

- `06-modules/6.4-packages/` sample package trees used to explain imports (no READMEs of their own):
  - [`6.4.1-importing-from-a-package/sound/`](06-modules/6.4-packages/6.4.1-importing-from-a-package/sound/) with [`effects/`](06-modules/6.4-packages/6.4.1-importing-from-a-package/sound/effects/), [`filters/`](06-modules/6.4-packages/6.4.1-importing-from-a-package/sound/filters/), [`formats/`](06-modules/6.4-packages/6.4.1-importing-from-a-package/sound/formats/) — package tree for the `import *` rules.
  - [`6.4.2-intra-package-references/sound/`](06-modules/6.4-packages/6.4.2-intra-package-references/sound/) with [`effects/`](06-modules/6.4-packages/6.4.2-intra-package-references/sound/effects/), [`filters/`](06-modules/6.4-packages/6.4.2-intra-package-references/sound/filters/), [`formats/`](06-modules/6.4-packages/6.4.2-intra-package-references/sound/formats/) — second copy of the tree for relative-import examples.
  - [`sound/`](06-modules/6.4-packages/sound/) with [`effects/`](06-modules/6.4-packages/sound/effects/), [`filters/`](06-modules/6.4-packages/sound/filters/), [`formats/`](06-modules/6.4-packages/sound/formats/) — base package layout introduced in 6.4.
- [`09-classes/9.5-inheritance/modname/`](09-classes/9.5-inheritance/modname/) — tiny module used to show fully qualified names.
- `10-brief-tour-of-the-standard-library/10.1-operating-system-interface/` fake directory layout for the `os`/`shutil` examples:
  - [`build/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/build/) with [`executables/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/build/executables/) — fake build output.
  - [`installdir/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/installdir/) — fake install target directory.
  - [`server/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/server/) with [`accesslogs/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/server/accesslogs/) and [`accesslogs/today/`](10-brief-tour-of-the-standard-library/10.1-operating-system-interface/server/accesslogs/today/) — fake log tree for traversal examples.
- `15-floating-point-arithmetic-issues-and-limitations/__pycache__/` — generated bytecode, safe to ignore or delete.
