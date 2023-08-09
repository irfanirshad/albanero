'''Creating the model of Todo Item here'''

class Todo:
    def __init__(self, todo_id, title, description):
        self.id = todo_id
        self.title = title
        self.description = description


'''Can add __repr__ , __lt__ and __iter__ here 

Based on last week's learning, better to use dataclasses here as they autogenerate all that code
for you resulting in faster development time...

'''