''' Sample User-defined exception code snippet
'''
    
# from all_exceptions_file import *

class UserNotFoundException(RuntimeError):
    def __init__(self,email=None):
        super().__init__(f"Can't find the user with the ID: {email} ...")


logBook = { 
    "aditya@mycompany" : "Aditya Verma",
    "snehaj@mycompany" : "Sneha Joshi",
    "nidhi20@mycompany" : "Nidhi Kapoor"
}

class Login(UserNotFoundException):
    def display(self, email):
        if email in logBook:
            print(logBook.get(email))
        else:
            raise UserNotFoundException(email)
        
try:
    temp = Login()
    temp.display("irfan@albanero.io")
    temp.display("nidhi20@mycompany")
except UserNotFoundException as e:
    print(e)