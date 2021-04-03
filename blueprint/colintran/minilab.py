import json

# dictionaries
colin = { "name":"Colin", "age":17, "food":"Sushi", "city":San Diego}
cory= { "name":"Cory", "age":18, "food":"Rice", "city":San Diego}
keven= { "name":"Keven", "age":24, "food":"Tacos", "city":Orange County}
susan= { "name":"Susan", "age":50, "food":"Bagels", "city":Saigon}

# making a list with dictionaries and printing it
list_of_family = [colin, cory, keven, susan]
print("List of family members:")
#print(type(list_of_family))
print(list_of_family)
print("Individual family members")
for person in list_of_family:
    print(person['name'] + "," + str(person['age']) + "," + person['food'] + "," + str(person['city']))
print()

# turn list to dictionary of family
family = {'people': list_of_family}
print(family)
print("Dictionary of family:")
dictionary_list_of_family = family['people']
print(dictionary_list_of_family)
print()

# turn dictionary to JSON
json_family = json.dumps(dictionary_list_of_family)
print("JSON family file")
print(json_family)
print(family)
for char in json_family:
    print(char, end ="_")
print()


# the result is a JSON file:
print()
print(json_family)
family = json.loads(json_family)


colin = { "name":"Colin", "age":17, "food":"Sushi", "city":San Diego}
cory= { "name":"Cory", "age":18, "food":"Rice", "city":San Diego}
keven= { "name":"Keven", "age":24, "food":"Tacos", "city":Orange County}
susan= { "name":"Susan", "age":50, "food":"Bagels", "city":Saigon}
list_of_players = [colin, cory, keven, susan]
family ={'people': list_of_family}
dictionary_list_of_players = family['people']
json_players=json.dumps(dictionary_list_of_family)
print(json_family)
