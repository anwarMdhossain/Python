import json

data = '''{
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}'''

data1={
    "user1": {
        "name": "Sumit kumar",
        "age": 31,
        "Place": "Patna",
        "Blood group": "O-"
    }
}

json_string = json.loads(data)
json_string.update(data1)

for data_key in json_string:
    for key,val in json_string[data_key].items():
        print(key+":"+str(val))

with open( "datafile.json" , "w" ) as write:
    json.dump( json_string , write , indent=3)

