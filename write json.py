import json
x = {
  "name": "shivani",
  "age": 20,
  "city": "New York"
}
with open("write.json","w") as file:
    json.dump(x,file)