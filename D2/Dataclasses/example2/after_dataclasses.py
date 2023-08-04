from dataclasses import dataclass, astuple, asdict, field
from pprint import pprint
import inspect

# by default it just writes init , eq and repr
# if you want hash, needs the frozen so that it makes it immutable
# watch out for default immutable arguments... 
# here in replies, we dont want every instance of commment class to share this replies list[].. 
# so use a field(default_factory=list) instead. use a field() method
# in classes with more attributes, we might want to use field() for every attribute to modify how they act
@dataclass(frozen=True, order=True)
class Comment:
    id: "int" = field()
    text: "str" = field(default="")
    replies: "list[int]" = field(default_factory=list, compare=False, hash=False, repr=False)
    
    
def main():
    comment = Comment(1, "I just wanted to say this is cool")
    print(comment) 
    
    # comment.id = 3 # this is error because its immutable. 
    
    # printing out the obj
    # print(Comment.__annotations__)
    # print(astuple(comment))
    # print(asdict(comment))
    
    
    
    #inspect
    pprint(inspect.getmembers(Comment, inspect.isfunction))

if __name__ == "__main__":
    main()  
    

    """attr is another library with which dataclasses was based out of ..
    - It allows to type check at runtime or converter to specific type convert
    
    As of now, to my knowledge, dataclasses doesn't support slots feature. 
    So if you want your classes to use slots feature instead of dictionary, attr supports it but dataclasses dont.
    
    """