## 12.2. Creating Virtual Environments

The module used to create and manage virtual environments is called `venv`. `venv` will install the Python version from which the command was run (as reported by the `--version` option). For instance, executing the command with `python3.12` will install version 3.12.

To create a virtual environment, decide upon a directory where you want to place it, and run the `venv` module as a script with the directory path:

``` python
python -m venv tutorial-env
```
> Code: [example_01.py](example_01.py)

This will create the `tutorial-env` directory if it doesn't exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is `.venv`. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with `.env` environment variable definition files that some tooling supports.

Once you've created a virtual environment, you may activate it.

On Windows, run:

``` python
tutorial-env\Scripts\activate
```
> Code: [example_02.py](example_02.py)

On Unix or MacOS, run:

``` python
source tutorial-env/bin/activate
```
> Code: [example_03.py](example_03.py)

(This script is written for the bash shell. If you use the **csh** or **fish** shells, there are alternate `activate.csh` and `activate.fish` scripts you should use instead.)

Activating the virtual environment will change your shell's prompt to show what virtual environment you're using, and modify the environment so that running `python` will get you that particular version and installation of Python. For example:

``` console
$ source ~/envs/tutorial-env/bin/activate
(tutorial-env) $ python
Python 3.5.1 (default, May  6 2016, 10:59:36)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python35.zip', ...,
'~/envs/tutorial-env/lib/python3.5/site-packages']
>>>
```

Note that the activated virtual environment does not alter the `PYTHONPATH` variable in any way. This may lead to unexpected results if the path includes references to code which is incompatible with the Python version the virtual environment is using. The best practice is to `unset PYTHONPATH` in bash or the equivalent for the shell you are using.

To deactivate a virtual environment, type:

``` python
deactivate
```
> Code: [example_04.py](example_04.py)

into the terminal.
