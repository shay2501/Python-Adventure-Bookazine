import json

filename = "adventureDB.txt"

if filename:
    with open(filename, 'r') as database:
        datastore = json.load(database)

print(datastore["adventure"]["Kingdom"])
print(datastore["adventure"]["StartingPlace"])
for name in datastore["adventure"]["NPCNames"]:
     print(name)
