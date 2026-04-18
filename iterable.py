print("============ Iterable objects & RANGE ============")
# Iterable objects > string, dict, tuple, list, range, map, filter

text = "FanTalk"
for i in text:
    print(f"the letter: {i}")

range_obj = range(3)
print(f"range_obj: {range_obj}")

for ele in range_obj:
    print(f"the element: {ele}")

print("==== DICTIONARY =====")
# Dictionary is JSON object!
person = {"name": "Umar", "age": 20, "single": True}
person_obj = dict(name="Ali", age=22, single=False)
print(person)
print(person_obj)

name = person["name"]
print(f'the person name is {name}')

single = person_obj["single"]
print(f"{person_obj['name']} is married ? {single}")

# hobby =person["hobby"]
# print(hobby)  #KeyError: 'hobby'

# method: get()
name = person_obj.get("name")
hobby = person_obj.get('hobby')
balance = person_obj.get("balance", "balance yo'q")
print(f'the name: {name},hobby: {hobby} and balance: {balance}')

del person_obj["single"]

for key in person_obj:
    print(f"the key: {key}, the value: {person_obj[key]}")
    print(f"the key: {key}, the value: {person_obj.get(key)}")
