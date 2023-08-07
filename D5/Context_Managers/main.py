'''
Context managers sample code snippet
'''

with open('test.txt', "wb") as test_file:
    test_file.append("this is a sample test append sentence")



# creating own contex manager ....

'''At the very least, a context manager should have an __enter__() and __exit__() 
'''


# Implementing context manager as a class with exceptions

class File(object):
    def __init__(self, filename, action):
        self.file = open (filename, action)
    
    def __enter__(self):
        return self.file
    def __exit__(self, type, Traceback):
    
        self.file.close()
    
with File("test.txt",'w') as file_obj:
    file_obj.append("Apple") # type: ignore
