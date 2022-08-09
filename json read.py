import json
# a= {
#   "name": "shivani",
#   "age": 20,
#   "city": "New York"
# }

f=open("write.json","r")
a=f.read()
finaldata=json.loads(a)

print(finaldata)