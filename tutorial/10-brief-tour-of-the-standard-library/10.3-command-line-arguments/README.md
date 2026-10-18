## 10.3. Command-line arguments

Common utility scripts often need to process command-line arguments. These arguments are stored in the `sys` module's *argv* attribute as a list. For instance, let's take the following `demo.py` file:

``` python
# File demo.py
import sys
print(sys.argv)
```
> Code: [demo.py](demo.py)

Here is the output from running `python demo.py one two three` at the command line:

``` python
['demo.py', 'one', 'two', 'three']
```
> Code: [example_01.py](example_01.py)

The `argparse` module provides a more sophisticated mechanism to process command-line arguments. The following script extracts one or more filenames and an optional number of lines to be displayed:

``` python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
> Code: [parser.py](parser.py)

When run at the command line with `python top.py --lines=5 alpha.txt beta.txt`, the script sets `args.lines` to `5` and `args.filenames` to `['alpha.txt', 'beta.txt']`.
