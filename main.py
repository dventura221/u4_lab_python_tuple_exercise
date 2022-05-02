# Exercise 1
# - Create a list named `students` containing some student names (strings).
# - Print out the second student's name.
# - Print out the last student's name.
students = ['Dan', 'Chris', 'Adrian']
print(students[1])
print(students[2])

# Exercise 2
# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
# - Use a `for` loop to print out the string "_food goes here_ is a good food".
# foods = tuple('Pizza', 'Sushi', 'Steak') Did not work right
foods = ('Pizza', 'Sushi', 'Steak')
for word in foods:
    print('{} is a good food'.format(word))

# Exercise 3
# - Using a `for` loop, print just the last two food strings from `foods`.
for word in foods[1:]:
    print(word)

# Exercise 4
# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format:<br>"I was born in _city_, _state_ - population of _population_"
home_town = {
    "city": "Denver",
    "state": "Colorado",
    "population": 125000
}
print('I was born in ' + home_town["city"] + ', ' +
      home_town["state"] + ' - population of ' + str(home_town["population"]))

# Exercise 5
# - Iterate over the _key: value_ pairs in `home_town` and print a string for each item, for example:<br>"city = Arcadia"<br>"state = California"<br>"population = 58000"
for key in home_town:
    print(key + " = " + str(home_town[key]))

# Exercise 6
# - Create an empty list named `cohort`.
# - Using a `for` loop, add one dictionary to the `cohort` list for each student name. Each dictionary should have this shape:

# 	```python
# 	{
# 	  'student': 'Tina',
# 	  'fav_food' 'Cheeseburger'
# 	}
# 	```
# - Iterate over `cohort` printing out each element.
cohort = []
for i in range(0, len(students)):
    newdict = {}
    newdict["student"] = students[i]
    newdict["fav_food"] = foods[i]
    cohort.append(newdict)
    print(newdict)


# Exercise 7
# - Using the list of `students` and list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over `awesome_students` printing out each string.
awesome_students = [(x + " is awesome!") for x in students]
for x in awesome_students:
    print(x)

# Exercise 8
# - Using the tuple `foods` and list comprehension within a `for` loop, print each food string that contains the letter `a`.
# find_e = [(x)for x in foods]
# print(x) if x.find("e") > 0 else print(None)
find_e = [(print(x) if x.find("e") > 0 else None) for x in foods]  # SOLUTION
