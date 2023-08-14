# Serialization


Beyond accessing model attributes directly via their field names, models can be converted, dumped , serialized and exported in a number of ways...

#### Serialize vs Dump
``` 
Pydantic uses the terms "serialize" and "dump" interchangeably. Both refer to the process of converting a model to a dictionary or JSON-encoded string.


Outside of Pydantic, the word "serialize" usually refers to converting in-memory data into a string or bytes. However, in the context of Pydantic, there is a very close relationship between converting an object from a more structured form — such as a Pydantic model, a dataclass, etc. — into a less structured form comprised of Python built-ins such as dict.

```


### 