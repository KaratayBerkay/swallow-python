The [len()](../../built-in-functions/len/README.md) function is lock-free and [atomic](https://docs.python.org/3.15/glossary.html#term-atomic-operation).

> Concatenation and comparisons use the buffer protocol, which prevents
> resizing but does not hold the per-object lock. These operations may
> observe intermediate states from concurrent modifications:
>
> ``` python
> ba + other    # may observe concurrent writes
> ba == other   # may observe concurrent writes
> ba < other    # may observe concurrent writes
> ```
>
> All other operations from here on hold the per-object lock.
>
> Reading a single element or slice is safe to call from multiple threads:
>
> ``` python
> ba[i]        # bytearray.__getitem__
> ba[i:j]      # slice
> ```
>
> The following operations are safe to call from multiple threads and will
> not corrupt the bytearray:
>
> ``` python
> ba[i] = x         # write single byte
> ba[i:j] = values  # write slice
> ba.append(x)      # append single byte
> ba.extend(other)  # extend with iterable
> ba.insert(i, x)   # insert single byte
> ba.pop()          # remove and return last byte
> ba.pop(i)         # remove and return byte at index
> ba.remove(x)      # remove first occurrence
> ba.reverse()      # reverse in place
> ba.clear()        # remove all bytes
> ```
>
> Slice assignment locks both objects when *values* is a [bytearray](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md):
>
> ``` python
> ba[i:j] = other_bytearray  # both locked
> ```
>
> The following operations return new objects and hold the per-object lock
> for the duration:
>
> ``` python
> ba.copy()     # returns a shallow copy
> ba * n        # repeat into new bytearray
> ```
>
> The membership test holds the lock for its duration:
>
> ``` python
> x in ba       # bytearray.__contains__
> ```
>
> All other bytearray methods (such as [find()](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray.find/README.md),
> [replace()](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray.replace/README.md), [split()](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray.split/README.md),
> [decode()](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray.decode/README.md), etc.) hold the per-object lock for their
> duration.
>
> Operations that involve multiple accesses, as well as iteration, are never
> atomic:
>
> ``` python
> # NOT atomic: check-then-act
> if x in ba:
>     ba.remove(x)
>
> # NOT thread-safe: iteration while modifying
> for byte in ba:
>     process(byte)  # another thread may modify ba
> ```
>
> To safely iterate over a bytearray that may be modified by another
> thread, iterate over a copy:
>
> ``` python
> # Make a copy to iterate safely
> for byte in ba.copy():
>     process(byte)
> ```
>
> Consider external synchronization when sharing [bytearray](../../built-in-types/binary-sequence-types-bytes-bytearray-memoryview/bytearray/README.md) instances
> across threads.  See [Python support for free threading](https://docs.python.org/3.15/howto/free-threading-python.html#freethreading-python-howto) for more information.
