import unittest
import requests
from database import UserCollection
from users import usersArray

user_id= "6274f3fee4a51bcd96c67d4a"
api_url = "http://127.0.0.1:5000/users/"+user_id

#  Test get user function
## Get
response = requests.get(url=api_url)
print("[-] Get users response:")
if response.status_code==200:
    print(response.text)
else:
    print("[!] Failde to get users, response status is ", str(response.status_code))

## Post
# response = requests.post(url=api_url, json=usersArray[1] )
# print("[-] Post users response:")

# if response.status_code==200:
#     print(response.text)
# else:
#     print("[!] Failde to create a new users, response status is ", str(response.status_code))


## Put
updatedData={
    "name": "Test test",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
response = requests.put(url=api_url, json=updatedData)
print("[-] put users response:")

if response.status_code==200:
    print(response.text)
else:
    print("[!] Failde to update user, response status is ", str(response.status_code))

## Delete 
# response = requests.delete(url=api_url)
# print("[-] put users response:")

# if response.status_code==200:
#     print(response.text)
# else:
#     print("[!] Failde to update user, response status is ", str(response.status_code))
