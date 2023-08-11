'''Validating package.json in Marshmallow


Marshmallow can be used to validate configuration according to a schema.

This example demonstrates the foll features:
    - Validation and deserialization using Schema.load()
    - Custom Fields 
        - You have custom Field class, Method field, Function field
    - Specify deser


For this package.json structure,
let's validate this using Marshmallow


{
  "name": "dunderscore",
  "version": "1.2.3",
  "description": "The Pythonic JavaScript toolkit",
  "devDependencies": {
    "pest": "^23.4.1"
  },
  "main": "index.js",
  "scripts": {
    "test": "pest"
  },
  "license": "MIT"
}

'''

import sys
import json
from packaging import version
from pprint import pprint

from marshmallow import Schema, fields, INCLUDE, ValidationError


class Version(fields.Field):
    """Version field that de-serializes to a version object"""
    
    
    def _deserialize(self, value, *args, **kwargs):
        try:
            return version.Version(value)
        except version.InvalidVersion as e:
            raise ValidationError('Not a valid version') from e
    
    def _serialize(self, value, *args, **kwargs):
        return str(value)



'''
{
  "name": "dunderscore",
  "version": "1.2.3",
  "description": "The Pythonic JavaScript toolkit",
  "devDependencies": {
    "pest": "^23.4.1"
  },
  "main": "index.js",
  "scripts": {
    "test": "pest"
  },
  "license": "MIT"
}
'''
class JsonSchema(Schema):
    name: fields.Str(required=True)
    version = Version(required=True)
    description = fields.Str(required=True)
    main = fields.Str(required=False)
    homepage = fields.URL(required=False)
    dependencies = fields.Dict(keys=fields.Str(), values=fields.Str(), required=False)
    dev_dependencies = fields.Dict(
        keys=fields.Str(),
        values=fields.Str(),
        required=False,
        data_key="devDependencies",
    )
    
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

if __name__ == "__main__":
    # Test it out...
    pkg = {
  "name": "dunderscore",
  "version": "1.2.3",
  "description": "The Pythonic JavaScript toolkit",
  "devDependencies": {
    "pest": "^23.4.1"
  },
  "main": "index.js",
  "scripts": {
    "test": "pest"
  },
  "license": "MIT"
}
    
    try:
        pprint(JsonSchema().load(pkg))
    except ValidationError as error:
        print("ERROR: package.json is invalid")
        pprint(error.messages)
        sys.exit(1)

'''
# OUTPUT :::




{'description': 'The Pythonic JavaScript toolkit',
 'dev_dependencies': {'pest': '^23.4.1'},
 'license': 'MIT',
 'main': 'index.js',
 'name': 'dunderscore',
 'scripts': {'test': 'pest'},
 'version': <Version('1.2.3')>}

'''