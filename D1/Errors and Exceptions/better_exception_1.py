'''Sample code snippet '''

'''Better exception handling for say a scenario where you are connectiing to the database
and you want to handle the exception gracefully.

Lower level code - lower exception 
Let it bubble up ...

Use of the finally statement
'''


# BEFORE 
def fetch_blog_old(id: str):
    try:
        # connect to database
        conn = sqlite3.connect('application.db')
        cur = con.cursor()
        
        # execute query and fetch the data
        cur.execute(f"SELECT * FROM blogs where id = {id}")
        result = cur.fetchone()
        
        data = blog_lst_to_json(result)
        
        return data


#  AFTER
'''
Consider two errors that could occur here which maybe the blog doesnt 
exist or the blog is not public
LETS DEfine two error classes then...

Side note.. Read Exceptions class and make notes of its family


Seperate High Level Exceptions from Low level Exceptions 
'''

class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass


import sqlite3
def fetch_blog_new(id: str):
    try:
        # connect to database
        con = sqlite3.connect('application.db')
        cur = con.cursor()

        # execute query and fetch the data
        cur.execute(f"SELECT * FROM blogs where id = {id}")
        result = cur.fetchone()

        if result is None:
            raise NotFoundError(f'Unable to find id={id}')

        # Add an exception here as well for precise control
        data = blog_lst_to_json(result)

        return data
    except sqlite3.OperationalError as e:
        print(e)
        raise NotFoundError(f'Unable to find id={id}')
    finally:
        con.close()