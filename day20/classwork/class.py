# Dictionary გამოყენება მაშინ, როცა გვინდა :
# 1. მონაცემებზე წვდომა key-ის საშუალებით
# 2. დავაკავშიროთ ერთი მონაცემი მეორესთან
# 3. შევინახოთ სტრუქტურული მონაცემები
# 4. სწრაფი წვდომა მონაცემებზე

student = {
    "name": "John", 
    "age": 21, 
    "grades": 12,
    "city": "New York"
}


# მონაცემებზე წვდომა key-ის საშუალებით
keys = student.keys()
print(keys)  # dict_keys(['name', 'age', 'grades', 'city'])


# მონაცემებზე წვდომა value-ის საშუალებით
values = student.values()
print(values)  # dict_values(['John', 21, 12, 'New York'])


# მონაცემებზე წვდომა key-value წყვილების საშუალებით
items = student.items()
print(items)  # dict_items([('name', 'John'), ('age', 21