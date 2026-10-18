### 3.1.2. Text

Python can manipulate text (represented by type `str`, so-called "strings") as well as numbers. This includes characters "`!`", words "`rabbit`", names "`Paris`", sentences "`Got your back.`", etc. "`Yay! :)`". They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`) with the same result (Unlike other languages, special characters such as `\n` have the same meaning with both single (`'...'`) and double (`"..."`) quotes. The only difference between the two is that within single quotes you don't need to escape `"` (but you have to escape `\'`) and vice versa.) .

``` python
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> "Paris rabbit got your back :)! Yay!"  # double quotes
'Paris rabbit got your back :)! Yay!'
>>> '1975'  # digits and numerals enclosed in quotes are also strings
'1975'
```
> Code: [example_01.py](example_01.py)

To quote a quote, we need to "escape" it, by preceding it with `\`. Alternatively, we can use the other type of quotation marks:

``` python
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```
> Code: [example_02.py](example_02.py)

In the Python shell, the string definition and output string can look different. The `print()` function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:

``` python
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), special characters are included in the string
'First line.\nSecond line.'
>>> print(s)  # with print(), special characters are interpreted, so \n produces new line
First line.
Second line.
```
> Code: [s.py](s.py)

If you don't want characters prefaced by `\` to be interpreted as special characters, you can use *raw strings* by adding an `r` before the first quote:

``` python
>>> print('C:\this\name')  # here \t means tab, \n means newline
C:      his
ame
>>> print(r'C:\this\name')  # note the r before the quote
C:\this\name
```
> Code: [example_03.py](example_03.py)

There is one subtle aspect to raw strings: a raw string may not end in an odd number of `\` characters; see the FAQ entry for more information and workarounds.

String literals can span multiple lines. One way is using triple-quotes: `"""..."""` or `'''...'''`. End-of-line characters are automatically included in the string, but it's possible to prevent this by adding a `\` at the end of the line. In the following example, the initial newline is not included:

``` python
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

>>>
```
> Code: [example_04.py](example_04.py)

Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`:

``` python
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```
> Code: [example_05.py](example_05.py)

Two or more *string literals* (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.

``` python
>>> 'Py' 'thon'
'Python'
```
> Code: [example_06.py](example_06.py)

This feature is particularly useful when you want to break long strings:

``` python
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```
> Code: [text.py](text.py)

This only works with two literals though, not with variables or expressions:

``` python
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
           ^^^^^^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
               ^^^^^
SyntaxError: invalid syntax
```
> Code: [prefix.py](prefix.py)

If you want to concatenate variables or a variable and a literal, use `+`:

``` python
>>> prefix + 'thon'
'Python'
```
> Code: [example_07.py](example_07.py)

Strings can be *indexed* (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:

``` python
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```
> Code: [word.py](word.py)

Indices may also be negative numbers, to start counting from the right:

``` python
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```
> Code: [example_08.py](example_08.py)

Note that since -0 is the same as 0, negative indices start from -1.

In addition to indexing, *slicing* is also supported. While indexing is used to obtain individual characters, *slicing* allows you to obtain a substring:

``` python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```
> Code: [example_09.py](example_09.py)

Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.

``` python
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```
> Code: [example_10.py](example_10.py)

Note how the start is always included, and the end always excluded. This makes sure that `s[:i] + s[i:]` is always equal to `s`:

``` python
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```
> Code: [example_11.py](example_11.py)

One way to remember how slices work is to think of the indices as pointing *between* characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of *n* characters has index *n*, for example:

``` python
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```
> Code: [example_12.py](example_12.py)

The first row of numbers gives the position of the indices 0...6 in the string; the second row gives the corresponding negative indices. The slice from *i* to *j* consists of all characters between the edges labeled *i* and *j*, respectively.

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of `word[1:3]` is 2.

Attempting to use an index that is too large will result in an error:

``` python
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
> Code: [example_13.py](example_13.py)

However, out of range slice indexes are handled gracefully when used for slicing:

``` python
>>> word[4:42]
'on'
>>> word[42:]
''
```
> Code: [example_14.py](example_14.py)

Python strings cannot be changed --- they are immutable. Therefore, assigning to an indexed position in the string results in an error:

``` python
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
> Code: [example_15.py](example_15.py)

If you need a different string, you should create a new one:

``` python
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```
> Code: [example_16.py](example_16.py)

The built-in function `len()` returns the length of a string:

``` python
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```
> Code: [s_2.py](s_2.py)

> **See also**
>
> Text Sequence Type --- str
>
> :   Strings are examples of *sequence types*, and support the common operations supported by such types.
>
> String Methods
>
> :   Strings support a large number of methods for basic transformations and searching.
>
> f-strings
>
> :   String literals that have embedded expressions.
>
> Format string syntax
>
> :   Information about string formatting with `str.format()`.
>
> printf-style String Formatting
>
> :   The old formatting operations invoked when strings are the left operand of the `%` operator are described in more detail here.
