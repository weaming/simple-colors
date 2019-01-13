# Simple Colors

Colorful output in terminal.

## Installation

```sh
pip install simple-colors
```

## Usage

```python
from simple_colors import *

print(green('hello'))
print(green('hello', 'bold'))
print(green('hello', 'underlined'))
```

## Inlucded colors

* black
* red
* green
* yellow
* blue
* magenta
* cyan

## Included styles:

* bold
* bright
* dim
* italic
* underlined
* blink
* reverse

## CLI Usage

```
$ simple-colors -h
usage: simple-colors [-h]
                     [-s {bright,bold,dim,italic,underlined,blink,reverse}]
                     {black,red,green,yellow,blue,magenta,cyan} text

positional arguments:
  {black,red,green,yellow,blue,magenta,cyan}
  text                  text of file path

optional arguments:
  -h, --help            show this help message and exit
  -s {bright,bold,dim,italic,underlined,blink,reverse}, --style {bright,bold,dim,italic,underlined,blink,reverse}
```
