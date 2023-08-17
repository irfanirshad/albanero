'''
STATUS: Ongoing
TO_DO: Loosely coupled custom error exceptions integration to be imported from ValidationError. 
'''


# import required modules
from enum import Enum
from typing import Optional
from pydantic import BaseModel, PositiveInt, validator, root_validator, constr
from validations import UserError, AddressError, PersonalDetailsError


# custom class used as choices for state
# pydantic choices using the built-in Enum of python
# which reduces the need for additional packages
class StateTypes(str, Enum):
    DELHI = "DLH"
    UTTAR_PRADESH = "UP"
    BENGALURU = "BLR"
    WEST_BENGAL = "WB"



# class to get personal credentials
class PersonalDetails(BaseModel):
    '''
    Add comment or generate docs + shorten it
    '''
    id: int
    # constr used for size constraint
    name: constr(min_length=2, max_length=25)
    phone: PositiveInt

    # validation at field level
    @validator("phone")
    # get phone number
    @classmethod
    def phone_length(cls, v):
        # phone number validator: should typically be of length 10
        if len(str(v)) != 10:
            raise PersonalDetailsError("Phone number must be of ten digits")
        return v

# class to get address                
class Address(BaseModel):
    id: int
    address_line_1: constr(max_length=50)

    # assigning some fields to be optional
    address_line_2: Optional[constr(max_length=50)] = None
    pincode: PositiveInt
    city: constr(max_length=30)
    
    # using choices in python is this simple.
    # Just create a class with Enums as choices
    # and the pass the class as type for the field
    state: StateTypes

    @validator("pincode")
    @classmethod
    def pincode_length(cls, v):
        if len(str(v)) != 6:
            raise AddressError("Pincode must be of six digits")
        return v


class User(BaseModel):
    '''Model of a User. Validation is being done here to check if
    id of User is equal to Address 
    '''
    personal_details: PersonalDetails
    address: Address

    # skip_on_failure=True means it will skip the
    # validation for this class if it's custom
    # fields are not validated
    @root_validator(skip_on_failure=True)
    @classmethod
    def check_id(cls, values):
        # custom validation ensuring personal_details.id is
        # same as address.id
        personal_details: PersonalDetails = values.get("personal_details")
        address: Address = values.get("address")
        if personal_details.id != address.id:
            raise UserError(value=personal_details, message="Address ID should be same as Personal ID")
        return values



'''
DATA 


validated_data = {
        "personal_details": {
            "id": 1,
            "name": "GeeksforGeeks",
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

    # valid data . Will not fail
    user = User(**validated_data)

    # would print the standard __str__ value for the model
    print(user)

    unvalidated_data = {
        "personal_details": {
            "id": 1,
            "name": "GeeksforGeeks",
            "phone": 9999999999,
        },
        "address": {
            "id": 2,
            "address_line_1": "Sector- 136",
            "pincode": 201305,
            "city": "Noida",
            "state": "UP",
        },
    }

'''



# class ISBN10FormatError(Exception):
#     ''' Custom error for ISBN10 format..'''
    
#     def __init__(self, value: str, message: str) -> None:
#         self.value = value
#         self.message = message
#         super().__init__(message)


#     @pydantic.root_validator(pre=True)
#     @classmethod
#     def check_isbn10_or_isbn13(cls, values):
#         '''Make sure there is either an isbn10 or isbn13 value defined...'''
#         if isbn_10 not in values or isbn_13 not in values:
#             raise ISBNMissingError(
#                 title=values['title'],
#                 message="Document should either have an ISBN10 or ISBN13 ",
#             )
            
#         return values

# class Book(pydantic.BaseModel):
#     title: Optional[str]
#     author: Optional[str]
#     publisher: Optional[str]
#     price: Optional[float]
#     isbn_10: Optional[str]
#     # subtitle: Optional[str]
#     isbn_13: Optional[str]
    
    
#     # 2nd step
#     # classmethod not strictly needed but will run into problems with style if removed(?)
#     # raise CustomError
#     @pydantic.validator("isbn_10")
#     @classmethod
#     def isbn_10_validator(cls, value):
#         '''Validator to check if ISBN10 is legit or not'''
#         chars = [c for c in value if c in "0123456789Xx"]
#         if len(chars != 10):
#             raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits")
        
#         weighted_sum = sum((10-i)*1 for i,x in enumerate(chars))
#         # if weighted_sum % 11 != 0:
#         #     raise ISBN10FormatError(
#         #         value=value, message="ISBN10 digit should be div by 11."
#         #     )
        
#         return value