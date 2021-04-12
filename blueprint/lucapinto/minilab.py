import json
#Make a Dictionary of my family.  Have at least 4 attributes per person.
fm1 = { "name":"Luca ", "age":17, "sport":"waterpolo", "color":"blue", "sibling":True}
fm2 = { "name":"Matteo", "age":25, "sport":"track", "color":"orange", "sibling":True}
fm3 = { "name":"Davide", "age":22, "sport":"tennis", "color":"blue", "sibling":True}
fm4 = { "name":"Simona", "age":45, "sport":"basketball", "color":"red", "parent":True}
fm5 = { "name":"Angelo", "age":47, "sport":"weightlifting", "color":"green", "parent":True}
familymem = [fm1, fm2, fm3, fm4, fm5]
print("List Of Family Members")
print(type(familymem))
print(familymem)
print()
for family_member in familymem:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['sport'] + ", " + family_member['color'])
print()
family = {'familylist': familymem}
print(type(family))
print(family)
familylist_members = family['familylist_members']
print()
for familylist_members in familylist_members:
    print(familylist_members['name'] + ", " + str(familylist_members['age']) + ", " + familylist_members['sport'] + ", " + familylist_members['color'])
print()
json_familylist_members = json.dumps(family)
print("JSON Family Members")
print(type(json_familylist_members))
print(json_familylist_members)
x = json.loads(json_familylist_members)
family_members = x['familylist_members']
print()
for family_member in familylist_members:
    print(family_member['name'] + ", " + str(family_member['age']) + ", " + family_member['sport'] + ", " + family_member['color'])
print()
print("Return JSON File To A Dictionary - Key is familylist_members")
print(json_familylist_members)
dictfamilymembers = json.loads(json_familylist_members)
listfamilymembers = dictfamilymembers['familylist_members']
parents = []
siblings = []
me = []
print()
print("Organized Members")
print()
print("Parents")
print(parents)
print()
for member in parents:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()
print("Siblings")
print(siblings)
print()
for member in siblings:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()
print("Me")
print(me)
print()
for member in me:
    print(member['name'] + ", " + str(member['age']) + ", " + member['sport'] + ", " + member['color'])
print()