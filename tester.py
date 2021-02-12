# code here
import json

# some dictionaries
p1 = { "name":"John", "age":30, "city":"New York"}
p2 = { "name":"Gavin", "age":18, "city":"San Diego"}
p3 = { "name":"George", "age":40, "city":"San Diego"}

# a list of dictionaries
list_of_people = [p1, p2, p3]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()



# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
list_of_people2 = dict_people['people']
print(list_of_people2)
for person in list_of_people2:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()




# turn dictionary to JSON (aka string)
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end =" ")
for char in json_people:
    print(char, end = "-")
print()






# turn dictionary to JSON, this can be sent via a browser
json_people = json.dumps(dict_people)
# the result is a JSON file:
print("JSON People #2")
print(type(json_people))
print(json_people)
# write some code to unwind JSON using json.loads and print the people
for char in json_people:
    print(char, end = "-")
print()

