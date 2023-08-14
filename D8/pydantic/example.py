import pydantic
import json
from typing import Optional, List

'''
1) Created Base Model

2) Adding a validator for isbn_10 . Can biz logic will contain there. Validator checks

3) Model validation(validating the whole of the model):::: root_validator()
Can check before or after... use root_validator(pre=True)
So basically lets say you want to check if either isbn_10 or isbn_13 is present...

4) 

'''

class ISBNMissingError(Exception):
    '''Custom error that is raised when both ISBN10 and ISBN13 are missing.'''
    
    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)



class ISBN10FormatError(Exception):
    ''' Custom error for ISBN10 format..'''
    
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        '''Make sure there is either an isbn10 or isbn13 value defined...'''
        if isbn_10 not in values or isbn_13 not in values:
            raise ISBNMissingError(
                title=values['title'],
                message="Document should either have an ISBN10 or ISBN13 ",
            )
            
        return values

class Book(pydantic.BaseModel):
    title: Optional[str]
    author: Optional[str]
    publisher: Optional[str]
    price: Optional[float]
    isbn_10: Optional[str]
    # subtitle: Optional[str]
    isbn_13: Optional[str]
    
    
    # 2nd step
    # classmethod not strictly needed but will run into problems with style if removed(?)
    # raise CustomError
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value):
        '''Validator to check if ISBN10 is legit or not'''
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars != 10):
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits")
        
        weighted_sum = sum((10-i)*1 for i,x in enumerate(chars))
        # if weighted_sum % 11 != 0:
        #     raise ISBN10FormatError(
        #         value=value, message="ISBN10 digit should be div by 11."
        #     )
        
        return value



def main() -> None:
    
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # print(books)
        print(books[0])
        # print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())




if __name__ == "__main__":
    main()