import json
import csv
import pickle


my_object = [{"name": "alex", "age": 23, "married": None}, {"name": "jim", "age": 22, "married": True}]
json_string = json.dumps(my_object, indent=2)

with open("my.json", "r") as f:
    temp = f.read()
    my_object = json.loads(temp)

print(my_object["web-app"].keys())

somedict = dict(raymond="red", rachel="blue", matthew="green")
somedict2 = dict(raymond="red2", rachel="blu2e", matthew="gree2n")
with open("mycsvfile.csv", "wt") as f:

    writer = csv.DictWriter(f,somedict.keys())
    writer.writeheader()
    writer.writerow(somedict)
    writer.writerow(somedict2)



