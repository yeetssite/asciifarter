# fartlib reference
This document outlines all the functions, objects and classes included in `fartlib`.
Innaccurate information? Make an [issue on GitHub](https://github.com/yeetshttps/asciiFarter/issues).

---

## `getfart`
`getfart` is the main module used by `fartlib`. It includes functions and classes to receive art files over the internet such as `random_art` or `newest_art`.

### `.random_art()`
```python3
class getfart.random_art()
```
Gets a randomly selected ascii art. If the selected art won't fit in your terminal, it will reroll for another art that will.

#### Attributes
###### `random_art.name`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The filename of the randomly selected art.

###### `random_art.File`
[`urllib.request.Request()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) - The art as a file-like object.

###### `random_art.text`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The text of the randomly selected art, equalvilant to "`random_art.File.read().decode('utf-8')`".

#### Methods
###### `random_art.poop()`
```python3
def random_art.poop(line_delay=0.000001)
```
Prints the art in AsciiFarter style, replaceable using [`stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) and [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep).

###### Arguments:
`line_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. Responsible for the scrolling effect output by AsciiFarter.


---

### `.newest_art()`
```python3
class getfart.newest_art()
```
Get the newest art, pulled from the `<newestAscii>` element in [`status.xml`](https://yeetshttps.github.io/asciiFarter/status.xml).

#### Attributes
###### `newest_art.name`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The filename of the selected art.

###### `newest_art.File`
[`urllib.request.Request()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) - The art as a file-like object.

###### `newest_art.text`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The text of the selected art, equalvilant to "`newest_art.File.read().decode('utf-8')`".

#### Methods
###### `newest_art.poop()`
```python3
def newest_art.poop(line_delay=0.000001)
```
Prints the art in AsciiFarter style, replaceable using [`stdout`](https://docs.python.org/3/library/sys.html#sys.stdout) and [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep).

###### Arguments:
`line_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. Responsible for the scrolling effect output by AsciiFarter.


---

### `.find_art()`
```python3
class getfart.find_art(art=None)
```

Finds an `art` by name. The name of the `art` must be passed as a [`str()`](https://docs.python.org/3/library/stdtypes.html#textseq). If a string isn't passed, the exception `getfart.find_art.SearchError` will be raised.

#### Arguments:
`art`: [`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The art's name to search for. Raises `getfart.find_art.SearchError` if no name or an invalid type(not a [`str()`](https://docs.python.org/3/library/stdtypes.html#textseq)) is provided.

#### Attributes
###### `find_art.search`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The string passed to `art` converted to lowercase for better and more reliable results

###### `find_art.found`
[`bool()`](https://docs.python.org/3/library/functions.html#bool) - Whether or not the `art` to look for has been successfully found.  

Set to `True` if found, or `False` if otherwise.

###### `find_art.name`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The name of the found `art`. Similar to [`random_art.name`](#random_artname) or [`newest_art.name`](#newest_artname).

###### `find_art.File`
[`urllib.request.Request()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.Request) - The found `art` as a file-like object.

###### `find_art.text`
[`str()`](https://docs.python.org/3/library/stdtypes.html#textseq) - The found `art`'s text contents as a string. Equalvilant to `find_art.File.read.decode('utf-8')`.

#### Methods
###### `find_art.poop()`
```python3
def find_art.poop(line_delay=0.0001, char_delay=0.001)
```

Prints the `art` in AsciiFarter style. Not required to print the `art`, as you can just print `find_art.text` directly.

###### Arguments
`line_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. A part of the animated output given by AsciiFarter.

`char_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. Another part of AsciiFarter's animated output. Currently only available for `find_art.poop()` and `list_art()`.


---

### `list_art`
```python3
class list_art(line_delay=0.001, char_delay=0.01)
```

Prints a list of all the ascii arts available to select from.

#### Arguments
`line_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between lines printed. A part of AsciiFarter's animated output.

`char_delay`: [`float()`](https://docs.python.org/3/library/stdtypes.html#typesnumeric) - The delay, in seconds, in between characters printed. Another part of AsciiFarter's animated output.


