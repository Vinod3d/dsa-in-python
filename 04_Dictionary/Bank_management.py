import json
import random
import string
from pathlib import Path

class Bank:
    database = Path(__file__).parent / "data.json"
    data = []

    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                content = fs.read().strip()
                if content:
                    data = json.loads(content)
        else:
            print("no such file exist")
    except Exception as err:
        print(f"there is error {err}")
    


    def create_account(self):
        name = input("enter your name:-")
        address = input("enter your address:-")
        mobile_no = input("enter your mobile number:-")
        acc_no = random.randint(1000, 9999)   
        if len(mobile_no) == 10 and mobile_no.isdigit():
            user_data = {
                'name': name,
                'address': address,
                'mobile_no': mobile_no,
                'acc_no': acc_no,
                'balance': 0
            }
            self.data.append(user_data)
            
            with open(self.database, 'w') as fs:
                json.dump(self.data, fs)
            print("account created successfully")
        else:
            print("invalid mobile number")

user = Bank()


print("press 1 for open account")
print("press 2 for deposit")
print("press 3 for withdraw")
print("press 4 for check balance")
print("press 5 for updating the details")
print("press 6 for deleting the account")
print("press 7 for exit")

check = int(input("tell your response :-"))

if check == 1:
    user.create_account()
# elif check == 2:
    # deposit()
# elif check == 3:
    # withdraw()
