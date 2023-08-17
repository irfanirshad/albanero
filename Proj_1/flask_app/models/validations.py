from typing import Optional, List
import pydantic

# class ValidationError(Exception):
#     def __init__(self, error_msg: str, status_code: int):
#         super().__init__(error_msg)
#         self.status_code = status_code
#         self.error_msg = error_msg


class AddressError(Exception):
    '''Custom error that is raised when address fields are not valid.'''
    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class UserError(Exception):
    '''Validation Error class that is raised when user validator fails'''
    def __init__(self, title:str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)
        
class PersonalDetailsError(Exception):
    '''Personal Details class that is raised when personal details validator fails'''
    def __init__(self, title:str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)
