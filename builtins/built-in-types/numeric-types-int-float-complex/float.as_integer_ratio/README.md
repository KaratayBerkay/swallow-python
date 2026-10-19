## `float.as_integer_ratio`

```
float.as_integer_ratio()
```

Return a pair of integers whose ratio is exactly equal to the
original float. The ratio is in lowest terms and has a positive denominator.  Raises
[OverflowError](https://docs.python.org/3.15/builtins/exceptions.html#OverflowError) on infinities and a [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) on
NaNs.
