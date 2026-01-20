# 1
numbers = [i for i in range(1, 11)]

print(numbers)

# 2
numbers_type = ["even" if i % 2 == 0 else "odd" for i in numbers]

print(numbers_type)

# 3
# 1)syntax error - ხდება მაშინ, როცა კოდის წერის დროს ხდება სინტაქსის დარღვევა
print("Hello, World!")
# 2)index error - ხდება მაშინ, როცა ცდებით მიუწვდეთ ელემენტს, რომელიც არ არსებობს სიაში
list_numbers = [1, 2, 3, 4, 5]
print(list_numbers[10])
# 3)type error - ხდება მაშინ, როცა ცდებით გამოიყენოთ ოპერაცია ან ფუნქცია, რომელიც არ შეესაბამება მონაცემთა ტიპს
print("5" + 10)
# 4)value error - ხდება მაშინ, როცა ფუნქციას გადაეცემა არგუმენტი, რომლის მნიშვნელობა არ არის მისაღები
int("hello")
# 5)name error - ხდება მაშინ, როცა ვიყენებთ ცვლადს ან ფუნქციას, რომელიც არ არის გამოყენებული 
name = "John"
print("x")