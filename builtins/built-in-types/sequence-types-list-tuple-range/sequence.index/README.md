## `sequence.index`

```
sequence.index(value[, start[, stop]])
```

Return the index of the first occurrence of *value* in *sequence*.

Raises [ValueError](https://docs.python.org/3.15/builtins/exceptions.html#ValueError) if *value* is not found in *sequence*.

The *start* or *stop* arguments allow for efficient searching
of subsections of the sequence, beginning at *start* and ending at *stop*.
This is roughly equivalent to `start + sequence[start:stop].index(value)`,
only without copying any data.

> **Caution**
>
> Not all sequence types support passing the *start* and *stop* arguments.
