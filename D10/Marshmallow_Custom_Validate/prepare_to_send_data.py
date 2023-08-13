from marshmallow import Schema, fields

from pprint import pprint

# Define a schema for the Person model
class PersonSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    email = fields.Email()

# Define a schema for the TotalPopulation model
class TotalPopulationSchema(Schema):
    people = fields.Nested(PersonSchema, many=True)

# Create a list to hold instances of PersonSchema
people_instances = []

# Create and add 10 instances of PersonSchema to the list
for i in range(10):
    person_instance = PersonSchema().load({'name': f"Person {i}", 'age': 20 + i, 'email': f"person{i}@example.com"})
    people_instances.append(person_instance)

# Create an instance of TotalPopulationSchema with the list of people instances
total_population_instance = TotalPopulationSchema().load({'people': people_instances})

# Serialize the TotalPopulation instance using TotalPopulationSchema
total_population_schema = TotalPopulationSchema()
serialized_data = total_population_schema.dump(total_population_instance)

# In a real scenario, you would send the serialized data
# to another microservice or an API endpoint
pprint(serialized_data)
# pprint("{sdf}: {sds}")