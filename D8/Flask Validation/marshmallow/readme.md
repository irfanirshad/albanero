# Marshmallow: Simplified Object Serialization

marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

```
from datetime import data
frim pprint import pprint

from marshmallow import Schema, fields

class ArtistSchema(Schema)
```



### Validation

 - validate(data: Mapping[str, Any] | Iterable[Mapping[str, Any]], *, many: bool | None = None, partial: bool | types.StrSequenceOrSet | None = None) → dict[str, list[str]]


 OR 

 - validate(data, *, many, partial ) -> dict[str, list[str]]

Validate data against the schema, returning a dictionary of validation errors.

Parameters:

        data – The data to validate.

        many – Whether to validate data as a collection. If None, the value for self.many is used.

        partial – Whether to ignore missing fields and not require any fields declared. Propagates down to Nested fields as well. If its value is an iterable, only missing fields listed in that iterable will be ignored. Use dot delimiters to specify nested fields.

Returns:

    A dictionary of validation errors.
