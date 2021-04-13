person = {"name": "Lou", "position": "backend", "age": 24}

# access value using key
# ! DOT NOTATION DOES NOT WORK IN PYTHON
# print(person["name"])
# print(person.name)  # throws error

# iterating dictionaries
for item in person.keys():
    print(item)

for item in person.values():
    print(item)


# both at the same time use items() func
for key, value in person.items():
    print(f"key is {key} and value is {value}")


# check if dictionary has a key
"name" in person  # True
"address" in person  # False

if "name" in person:
    print(person["name"])

if "addess" in person:
    print(person["address"])

# check if dictionary has value
"Lou" in person.values()
25 in person.values()

if "Lou" in person.values():
    print(person["name"])


# dictionary methods
