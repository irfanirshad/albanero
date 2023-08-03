'''
Problem Statement: Due to Python's automatic memory management(reference counting for most objects && gc)
, the memory frees only after the last reference to it has been eliminated.

Now when you need to track this object's count, you'll need a reference for it which in turn creates another 


ask LLM and team:
1) Here, we're calling gc.collect() (with empty params) immediately after deleting the last reference(strong reference)?
What's the weightage value of this action i.e What happens if we don't call it? Does python's gc module automagically
takes care of it or what?  But surely the gc has to implicitly execute this 'gc.collect()' to .....

A) Solved.
The reason is that Python's garbage collection is based on simple reference counting.
When the reference count of an object reaches 0, it is immediately deleted. For
cyclic data structures, however, this never happens.

To deal with cycles, there is a separate garbage collector that runs periodically. However,
as a general rule, you never know when it might run. Consequently, you never really
know when cyclic data structures might get collected. If necessary, you can force garbage
collection, but doing so is a bit clunky


[Answer from Python3 cookbook(D.Beazly)] 


2) 

'''

import weakref, gc


gc.collect()
class A:
    def __init__(self, value):
        self.value = value 

    def __repr__(self):
        return str(self.value)

a_obj_ref_1 = A(10)
strong_dict_reference  = {1 : a_obj_ref_1}
print(strong_dict_reference)
del a_obj_ref_1
# del strong_dict_reference[]
print(f" Strong dict reference -> \t {strong_dict_reference}")
gc.collect() 

print(a_obj_ref_1)

a_obj_ref_2 = A(10)
d = weakref.WeakValueDictionary()
d[1] = a_obj_ref_2
del a_obj_ref_2
print(d)
gc.collect()
print(f"After gc collect {d}")



print(strong_dict_reference)