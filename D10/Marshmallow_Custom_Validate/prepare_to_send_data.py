'''The above code defines two schemas, PersonSchema and TotalCityPopulationSchema, and demonstrates how
to use them for serialization and deserialization of data.
See exmaples of Nested schemas, Validate decorators , loading, dumping 

Scroll down for tips and Questions to ask lead
'''


from marshmallow import Schema, fields, ValidationError
from pprint import pprint




def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)



class CamelCaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """
    
    def on_bind_field(self, field_name, field_obj):
        field_obj.data_key = camelcase(field_obj.data_key or field_name)



# Sample Custom Validation Exception Class
class AgeValidatorException(ValidationError):
    def __init__(self, message="Age must be between 0 and 250"):
        self.message = message
        super().__init__(self.message)


# Ask lead about whether we convert 
class PersonSchema(CamelCaseSchema):
    name = fields.Str(required=True)
    age = fields.Int(required=True, validate=lambda n: 0 <= n <= 250, error=AgeValidatorException())  # Adjusted age limit
    email = fields.Email(required=True)

class TotalCityPopulationSchema(CamelCaseSchema):
    city_name = fields.Str(required=True)
    country = fields.Str(required=True)
    people = fields.Nested(PersonSchema, many=True)
    
    

    def pre_load(self, data):
        if 'people' in data:
            # Lowercase all email addresses before loading
            for person in data['people']:
                if 'email' in person:
                    person['email'] = person['email'].lower()
        return data

    def post_load(self, data):
        if 'people' in data:
            # Add 10 to the age of each person after loading
            for person in data['people']:
                if 'age' in person:
                    person['age'] += 10
        return data

# Create a list to hold instances of PersonSchema
people_instances = []

# Create and add 10 instances of PersonSchema to the list
for i in range(10):
    person_instance = {'name': f"Person {i}", 'age': 20 + i, 'email': f"person{i}@example.com"}
    people_instances.append(person_instance)

# Create an instance of TotalCityPopulationSchema with the list of people instances
total_population_instance = TotalCityPopulationSchema().load({'cityName': 'Tokyo', 'country': 'Japan', 'people': people_instances})
pprint(total_population_instance)


'''Try this out for the camelCase pr oblem'''
# total_population_instance1 = TotalCityPopulationSchema(city_name= 'Tokyo', country= 'Japan', people= people_instances)
# serialized_data1 = total_population_schema.dump(total_population_instance1)


# Serialize the TotalPopulation instance using TotalCityPopulationSchema
total_population_schema = TotalCityPopulationSchema()

serialized_data = total_population_schema.dump(total_population_instance)



# Print the serialized data
pprint(serialized_data)

# TIP 1
''' 
Incase you already have the data that does not match your schema then you can manually 
specify the fields. See below code snippet ..


Specifying Serialization/Deserialization Keys

Schemas will (de)serialize an input dictionary from/to an output dictionary whose keys are identical to the field names. If you are consuming and producing data that does not match your schema, you can specify the output keys via the data_key argument.


-x-x-x-x-x-x


class UserSchema(Schema):
    name = fields.String()
    email = fields.Email(data_key="emailAddress")


s = UserSchema()

data = {"name": "Mike", "email": "foo@bar.com"}
result = s.dump(data)
# {'name': u'Mike',
# 'emailAddress': 'foo@bar.com'}

data = {"name": "Mike", "emailAddress": "foo@bar.com"}
result = s.load(data)
# {'name': u'Mike',
# 'email': 'foo@bar.com'}
'''


# Q and A
''' QUestion for lead

- After I specified the camelcase as subclass for my model class instead of normal Model(Schema)
it looks like I cant 'load' in my snake_case fields anymore...


I simply want to maintain snake_case in my python program and Not worry ABOUT 
camelCase untill its time to dump my instance into a JSON representation...


Here, python gives me an error when I try to 'load' in with my snake_case fields as
marshmallow is expecting a CamelCase field....(which is correct as the docs say)
but how else Would i 'load' or initialize data within my model instances if not 'load'
...Other than __init__ ofcourse ....

How do i control the program to not deal with camelcase now but only do it when i


Not tried yet:
- use camelCase data_keys for this.... not sure if this solves this problem

'''