from marshmallow import Schema, fields, ValidationError
from pprint import pprint

def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)

class CamelCaseSchema(Schema):
    """Schema that uses camel-case for its external representation
    and snake-case for its internal representation.
    """

    def __init__(self, *args, **kwargs):
        self.camel_case_output = kwargs.pop('camel_case_output', True)
        super().__init__(*args, **kwargs)

    def on_bind_field(self, field_name, field_obj):
        if self.camel_case_output:
            field_obj.data_key = camelcase(field_obj.data_key or field_name)

# Sample Custom Validation Exception Class
class AgeValidatorException(ValidationError):
    def __init__(self, message="Age must be between 0 and 250"):
        self.message = message
        super().__init__(self.message)

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
total_population_instance = TotalCityPopulationSchema().load({'city_name': 'Tokyo', 'country': 'Japan', 'people': people_instances})

print(total_population_instance)

# Serialize the TotalPopulation instance using TotalCityPopulationSchema with camelCase keys
total_population_schema = TotalCityPopulationSchema(camel_case_output=True)

# Serialize the instance to JSON with camelCase keys
serialized_data = total_population_schema.dump(total_population_instance)

# Print the serialized data
pprint(serialized_data)
