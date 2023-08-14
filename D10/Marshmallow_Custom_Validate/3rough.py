'''
Incomplete due to camelCase to snake_case problem not being solved..

Overall the concept run would look like this:

1 - Recieve(input) JSON data in a camelCase format
2 - Marshal/map these attributes to a Schema 
3 - Perform validation here ?
4 - Use for processing... 

'''

class CreateUserDto(ma.Schema):
    __model__ = user

    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)

    id = ma.Integer(required=True, dump_only=True)
    first_name = ma.String(required=True, data_key="firstName")
    last_name = ma.String(required=True, data_key="lastName")
    user_name = ma.String(required=True, data_key="userName")
    password = ma.String(required=True, load_only=True)
    
    '''With the user of “data_key” attribute, one can specify the value that is in the JSON payload. The name of the variable would be the key in the dictionary that is generated after validation. This is what is passed in the “data” to the “make_object” function. Since the fields directly map to the that in the DB model, it is converted into model and can be saved in DB
Conclusion

“data_key” can be used to specify the key names in the JSON payload

In the next post, we look at how to update an existing model
'''