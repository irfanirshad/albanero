
'''
Using Context Manager
'''


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



class SQLite

