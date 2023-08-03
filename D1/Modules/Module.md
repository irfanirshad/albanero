# Modules

Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module; definitions from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).


### More on modules

When you import a module like this
```from fibo import *```

This imports all names except those beginning with an underscore(__). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

**Interesting line above. Explore?** 


Note that in general the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code. However, it is okay to use it to save typing in interactive sessions.

If the module name is followed by as, then the name following as is bound directly to the imported module.
```
import fibo as fib. 
fib.fib(500)
```

### Exceuting modules as scripts

```
python fibo.py <arguments>
```

is the same as 

```
if __name__=='__main__':
    import sys
    fib(int(sys.argv[1]))
```


### The module Search Path

WHen a module named "spam" is imported, the interpreter searches for it in the order:
    - Built-in module for that name
    - If not found, any files named "spam.py" in list of directories given by variable "sys.path"


### COmpiled Python files

.pyc files exist in the __pycache__ directory ... 


### dir()

dir() -> lists the names you have defined 
dir(sys) -> ALl the names a module defines.  Returns a sorted lists of strings..



### Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. For example, the module name A.B designates a submodule named B in a package named A.

For example: 

```sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

The __init__.py files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path. In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.


Say you wish to use echo.py inside of effects inside present in sound root folder.

3 ways to do this..

1.
```
import sound.effects.echo
# to use echofilter() , here you will have to reference with its full name...
sounds.effect.echo.echofiler(input, output, delay=0.7, atten=4)
```

2. 
```
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
```


3.
```
from sounds.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

### Importing * from a package

Using __all__ in __init__.py file.

```
__all__ = ["echo", "sorround", "reverse"]
```


### Intra-packaging references

#### Absolute imports

Should be used in main module of an application should always use absolute imports

```
from sound.effects import echo
```


Relative imports
```
from . import echo
from ..filters import equalizer
```
