'''
Use this script over to simulate
our endpoints ...

1) We first test our FLASK API endpoints //use curl here or requests
2) We then run a few iterations on our producer.py file   //import and directly call 

'''

import sys
# sys.path.append('/home/albanero/github_repos/albanero/Final_project/flask_app/models/Model.py')
from model import User
# from models.Model import Uservalue
from pprint import pprint

def main():
# testing models                
    validated_data = {
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

    # valid data . Will not fail
    user = User(**validated_data)

    # would print the standard __str__ value for the model
    pprint(user)

    unvalidated_data = {
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

    # this would raise a User error since the IDs
    # are different
    user = User(**unvalidated_data)
    pprint(user)
    
if __name__ == "__main__":
    main()