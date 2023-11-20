# creating dictionaries
 
person = {"name": "Bilal","age": 20, "location":"Nairobi","email":"bilalmaalim57@gmail.com"}

# how to access values in a dictionary


#updating values in a dictionary
person["age"]=70
person["name"]="john"
person["location"]="nyandarua"
person["email"]="john@gmail.com"
# print(person)
# print(person["name"])

# adding a new key value pair
person["Gender"] = "Male"
person["Address"] = "55-00100"

#dictionary methods


print(person.pop("name"))
print(person.get("age"))
print(person.fromkeys(""))
print(person.items())

# update method

new_data ={"course":"IT","campus":"JKUAT"}
person.update(new_data)
person.popitem()
print(person)

