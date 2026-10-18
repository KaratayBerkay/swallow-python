## 10.1. Operating system interface

The `os` module provides dozens of functions for interacting with the operating system:

``` python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python315'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```
> Code: [os_example.py](os_example.py)

Be sure to use the `import os` style instead of `from os import *`. This will keep `os.open()` from shadowing the built-in `open()` function which operates much differently.

The built-in `dir()` and `help()` functions are useful as interactive aids for working with large modules like `os`:

``` python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```
> Code: [os_2.py](os_2.py)

For daily file and directory management tasks, the `shutil` module provides a higher-level interface that is easier to use:

``` python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```
> Code: [shutil_example.py](shutil_example.py)
