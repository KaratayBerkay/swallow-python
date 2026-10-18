## 10.4. Error output redirection and program termination

The `sys` module also has attributes for *stdin*, *stdout*, and *stderr*. The latter is useful for emitting warnings and error messages to make them visible even when *stdout* has been redirected:

``` python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```
> Code: [example_01.py](example_01.py)

The most direct way to terminate a script is to use `sys.exit()`.
