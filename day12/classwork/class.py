# task-1:
text = "Hello, World!"

# task-replace: ცვლსი სიტყვებს ტექსტიდა ნა ასევე ნებისმიერ ასოს რისი შეცვლაც გვინდა
print(text.replace("World", "Python"))

# task-len: გამოითვლის ტექსტის სიმბოლოების რაოდენობას
print(len(text))

# task-upper: ტექსტს გადააქცევს დიდ ასოებად
print(text.upper())

# task-lower: ტექსტს გადააქცევს პატარა ასოებად
print(text.lower())

# text-capitalize: ტექსტის პირველ ასოს გადააქცევს დიდ ასოდ
print(text.capitalize())

# task-find: მოძებნის ტექსტში კონკრეტულ სიტყვას ან ასოს და დააბრუნებს მის პოზიციას
print(text.find("H"))

# task-2:

numbers = [10, 20, 30, 40, 50]
print(numbers)

# task-insert: ჩასვამს ახალ ელემენტს სიაში კონკრეტულ პოზიციაზე
numbers.insert(2, 25)  # ჩასვამს 25-ს ინდექსზე 2
print(numbers)

# task-append: დაამატებს ახალ ელემენტს სიას ბოლოს
numbers.append(60)
print(numbers)

# task-pop: წაშლის ელემენტს სიიდან კონკრეტული პოზიციიდან და დააბრუნებს მას
removed_element = numbers.pop(3)  # წაშლის ელემენტს ინდექსზე 3
print(removed_element)

# task-len: გამოითვლის სიაში ელემენტების რაოდენობას
print(len(numbers))


# task-3: functions გამოიყენება კოდის ნაწილების განმეორებად გამოყენებისთვის და კოდის ორგანიზებისთვის

# task-4:
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet("Bob"))

# task-5:
def multiply(a, b):
    return a * b

print(multiply(3, 4))

# task-6: default value არის ფუნქციის პარამეტრის ნაგულისხმევი მნიშვნელობა, რომელიც გამოიყენება მაშინ, როდესაც ფუნქცია იძახება და ამ პარამეტრისთვის არ არის მიწოდებული არგუმენტი.
def greet(name="Guest"):
    return "hello, " + name + "!"

print(greet())          # გამოიყენებს ნაგულისხმევ მნიშვნელობას "Guest"
print(greet("Alice"))   # გამოიყენებს მიწოდებულ მნიშვნელობას "Alice"