'''
consume Rest API 
and write users data(uid,name,city,company_name) into new json file
Information about REST API
________________________________
Usage :Get all users
API URL:https://jsonplaceholder.typicode.com/users
Method Type:GET
Required Fields:None
Access Type:Public
'''

import requests
import json


url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
new_users=[]

users = response.json()
for user in users:
    user_data = {
        "uid": user["id"],
        "name": user["name"],
        "city": user["address"]["city"],
        "company_name": user["company"]["name"]
    }
    new_users.append(user_data)
fp = open("users.json", "w")
json.dump(new_users, fp, )
fp.close()

print("new json file created")
