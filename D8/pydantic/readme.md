# Pydantic


### Pydantic over DataClasses

You'll need to install pydantic whereas dataclasses are officially accepted in the 
standard lib approved by Raymond Hettinger ...

Other Features:
    -  Data validation
    - Conversion
    - Sanitization



## Why use Pydantic?

    Powered by type hints — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools. 
    Speed — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. 
    JSON Schema — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. 
    Strict and Lax mode — Pydantic can run in either strict=True mode (where data is not converted) or strict=False mode where Pydantic tries to coerce data to the correct type where appropriate. 
    Dataclasses, TypedDicts and more — Pydantic supports validation of many standard library types including dataclass and TypedDict. 
    Customisation — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. 
    Ecosystem — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like FastAPI, huggingface, Django Ninja, SQLModel, & LangChain. 
    Battle tested — Pydantic is downloaded over 70M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it



## JSON Schema

Pydantic allows automatic creation of JSON schemas from models....

Using Pydantic, there are serveral ways to generate JSON schemas or JSON representations from fields or models...

1. BaseModel.model_json_schema: returns a dict of the schema
2. BaseModel.model_dump_json: returns a JSON string representation of the dict of the schema
3. TypeAdapter.dump_json: serializes an instance of the adapted type to JSON
4. TypeAdapter.json_schema: generates a JSON schema for the adapted type



