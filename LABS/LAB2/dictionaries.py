thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
person = dict(name = "John", age = 36, country = "Norway")

print(thisdict)
print(thisdict["brand"])
print(person)
print(thisdict.get("year"))

x = thisdict.keys()

print(x) #before the change
thisdict["color"] = "white"
print(x) #after the change

print(thisdict.values())
print(thisdict.items())

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict.update({"year": 2020})
print(thisdict)

thisdict.pop("colors")
print(thisdict)

for x in thisdict:
    print(thisdict[x])

for x in thisdict:
    print(thisdict[x])

mydict = thisdict.copy()
print(mydict)

print(myfamily["child2"]["name"])