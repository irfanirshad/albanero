from enum import Enum
from typing import Optional
from pydantic import BaseModel, PositiveInt, validator, root_validator, constr, field_validator, ValidationError
import re


# 3 utility functions
def to_pascal(snake: str) -> str:
    """Convert a snake_case string to PascalCase"""
    camel = snake.title()
    return re.sub('([0-9A-Za-z])_(?=[0-9A-Z])', lambda m: m.group(1), camel)

def to_camel(snake: str) -> str:
    ''' Convert a snake_case string to camelCase.'''
    camel = to_pascal(snake)
    return re.sub('(^_*[A-Z])', lambda m: m.group(1).lower(), camel)

def to_snake(camel: str) -> str:
    """Convert a PascalCase or camelCase string to snake_case.

    Args:
        camel: The string to convert.

    Returns:
        The converted string in snake_case.
    """
    snake = re.sub(r'([a-zA-Z])([0-9])', lambda m: f'{m.group(1)}_{m.group(2)}', camel)
    snake = re.sub(r'([a-z0-9])([A-Z])', lambda m: f'{m.group(1)}_{m.group(2)}', snake)
    return snake.lower()



class StateTypes(str, Enum):
    DELHI = "DLH"
    UTTAR_PRADESH = "UP"
    BENGALURU = "BLR"
    WEST_BENGAL = "WB"

class PersonalDetails(BaseModel):
    id: int
    name: constr(min_length=2, max_length=25)
    phone: PositiveInt

    @field_validator("phone")
    def phone_length(cls, v):
        if len(str(v)) != 10:
            raise ValueError("Phone number must be of ten digits")
        return v

    class Config:
        alias_generator = to_camel
        populate_by_name = True

class Address(BaseModel):
    id: int
    address_line_1: constr(max_length=50)
    address_line_2: Optional[constr(max_length=50)] = None
    pincode: PositiveInt
    city: constr(max_length=30)
    state: StateTypes

    @validator("pincode")
    def pincode_length(cls, v):
        if len(str(v)) != 6:
            raise ValueError("Pincode must be of six digits")
        return v

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

class User(BaseModel):
    personal_details: PersonalDetails
    address: Address

    @root_validator(skip_on_failure=True)
    def check_id(cls, values):
        personal_details: PersonalDetails = values.get("personal_details")
        address: Address = values.get("address")
        if personal_details.id != address.id:
            raise ValueError("Address ID should be same as Personal ID")
        return values

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True





# Your validated camelcase data
validated_data_camelCase = {
    "personalDetails": {
        "name": "GeeksforGeeks",
        "id": 1,
        "phone": 9999999999,
    },
    "address": {
        "id": 1,
        "addressLine1": "Sector- 136",
        "pincode": 201305,
        "city": "Noida",
        "state": "UP",
    },
}


not_valid_data = {
        "personal_details": {
            "name": "GeeksforGeeks",
            "id": 1,
            "phone": 9999999999,
        },
        "address": {
            "id": 1,
            "address_line_1": "Sector- 136",
            "pincode": 201305,
            "city": "Noida",
            "state": "UP",
        },
}
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["test_db"]  # Replace 'test_db' with your database name
collection = db["users"]

def get_all_data():
    try:
        all_data = list(collection.find({}))
        print(all_data)
        # return jsonify(all_data), 200
    except Exception as e:
        print(e)
        # return jsonify({"An error occurred": e}), 500

print(get_all_data())



# def save_data(data):
#     try:
#         # data = request.json
#         validated_data = User.model_validate(data)
#         document = validated_data.model_dump()  # Convert Pydantic model to dictionary
#         # collection.insert_one(document)
#         print("saving if all good")
#         # return jsonify({"message": "Data saved successfully"}), 201
#         print("return")
#     except ValidationError as e:
#         # return jsonify({"An Error occured while validating the data. Please try again": str(e)}), 400
#         print(f"Validation ERRORORO   :  {e}")
#     except Exception as e:
#         print(f"Exception:  {e}")
#         # return jsonify({"error": "An error occurred"}), 500


# print(save_data(validated_data_camelCase))







# def check_validation(user: User):
# # Convert camelcase keys to snakecase using Pydantic's alias_generator
#     try:
#         snakecase_data = User.model_validate(validated_data_camelCase)
#     except ValidationError as e:
#         print(f"An error occured while validation. {e} ")
#     else:
#         print("Your model has undergone validation.")
#     finally:
#         print(" The model has been successfully validated. Proceeding to send to the database for storage. ")



# print(snakecase_data.model_dump_json())  # Print the snakecase JSON
