# Pydantic supports Dataclasses

Pydantic provides 4 ways to create schemas and perform validation and serialization
## 



### JSON DUMPING

Pydantic dataclasses do not feature a .model_dump_json()





### INITIALIZATION HOOKS

When you initialize a dataclass, it is possible to execute code before or after validation with the help of the @model_validator decorator mode parameter.

