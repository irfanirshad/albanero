## Excerpt taken from a Dictionary vs Enums War


@nikolaychechulin3494
1 year ago
Do not parametrize functions with strings! Use enums
54

@ebn7722
1 year ago
care to elaborate? :)
1

@Rawing77
1 year ago
There are certainly reasons to use enums, but magic strings are pretty normal in python. The stdlib uses them all the time, and often they're just more convenient than an enum. Imagine writing `open(FileOpenMode.WRITE)` instead of `open('w')`, or `int.to_bytes(ByteOrder.LITTLE)` instead of `int.to_bytes('little')`.
19

@Nekto89
1 year ago
 @Rawing77  I don't see any problems with using openmode for fstreams in C++
2

@jfftck
1 year ago
There are cases where enums are the better choice, but if you are using them and the strings you are using are more descriptive it doesn’t make sense. The example given isn’t any less clear than if it were using enums since you would most likely just name the enums the same as the strings.
4

@konsth191
1 year ago
I think, the main advantage of enums would be that since it's a closed set of values, no usage errors from entering an invalid string can occur. (and the autocomplete after `OpenMode.` can help you know which values are available). with strings, you always need to pay attention to what happens if you use an invalid one. in the video, you got a nicer error message in the first version with the `raise ValueError(f"Unknown strategy: {str...`, I think in the second version you only get an error for trying to call `Null(prices)` if I'm not mistaken, you would need to add a check if prices is in the keys of BUY_STRATEGIES. 
and if you would update BUY_STRATEGIES anywhere, you could even add pretty silent bugs if you just index into the dict with a string without checking first. I think an enum would be cleaner!
9

@nikolaychechulin3494
1 year ago
 @jfftck    I think using enums is way better because of 2 things: (1) Closed set of values. It integrates with autocomplete, so you see all the options and protects you from typos. (2) It exposes less implementation information. It is especially important if we speak about libraries - not all of them have pretty HTML pages with documentation, and not all of us read it - we often rely on autocomplete and docstrings. I really don't want to look at the code of a function inside a library just to get it running
5
@seerlite5256
@seerlite5256
1 year ago
 @konsth191  Trying to retrieve an element from a non-existent key raises a descriptive KeyError. No need to add any checks.
@bbbstocken3642
@bbbstocken3642
1 year ago
If you have a non extendable set of strategies that would be preferable, but by using strings you can let users of this function update the dict with their own strategies without changing the code. To make that safe you can add specific methods to add (or replace or remove) strategies.
@appuser
@appuser
1 year ago
 @Rawing77  Maybe I'm an idiot but I'm not a fan of those arguments in supplied to open. They are not queryable by IntelliSense. I'd much prefer FileOpenMode.OVERWRITE_THEN_READ than having to google which of 'r', 'w', 'r+', 'w+' I'm looking for etc. Maybe one day it will be updated or they can introduced some other kind of typed argument.
3
@Rawing77
@Rawing77
1 year ago
 @appuser  It's unfortunately not (yet) true in practice, but considering that `typing.Literal` has existed for a while now, magic strings should auto-complete just as well as enums. There is really no reason why IntelliSense can't support magic strings. It's only a matter of time until it actually does.

[Taken from ArjanCode's Dictionary over if-else statement shorts video on YT]
-x-x-x--x-x-x--x

### Other RoadMaps to Follow


1. MetaClass usage in Enum

2. Enums with Flags

3. Enums Clever Use cases

4. When not to use Enums | Dicts over Enums 


5. Nested Enums?

```
class Piece(Enum):
    KING = 1
    QUEEN = 2
    ROOK = 3

class PieceValue(Enum):
    KING = 0
    QUEEN = 9
    ROOK = 5
```


Is there any more nested/tricks/inhertited stuff you can do with this...


6. Pydantic Enums etc... Third party dataclasses enums....

7. 