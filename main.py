name =  str(input(" enter your username "))
password = str(input(" enter your Password   "))
# import ipdb; ipdb.set_trace()
import json
with open('user.json') as feedsjson: # first reading the json file
    old_data = json.load(feedsjson)
    user_credentails = {"username":name,"password":password}
    old_data["user"].append(user_credentails)
with open('user.json' , 'w') as feedsjson:
    json.dump(old_data,feedsjson)  
    