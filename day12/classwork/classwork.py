print("Hello World!")

name = input ("სჰეიყვანე შენი სახელი:")
print("hello," + name )

a = int(input("შეიყვანე პირველი რიცხვი"))
b = int(input("სჰეიყვანე მეორე რიცხვი"))
print("რიცხვის ჯამია:", a + b)

year_of_birth = int(input("შეიყვანე შენი დაბადების წელი:"))
current_year = 2025
age = current_year - year_of_birth
print("შენ ხარ", age, "წლის")

number = int(input("სეიყვანე რიცხი:"))
cube = number ** 3
print("სჰეყვანი რიცხვის კუბია:", cube)

number = int(input("სეიყვანე რიცხვი:"))

if number % 2 == 0:
    print("ეს რიცხვი ლუწია")
else:
    print("ეს რიცხვი კენტია")

num1 = float("სეიყვანე პირველი რიცხვი")
num2 = float("სეიყვანე მეორე რიცხვი")
num3 = float("სეიყვანე მესამე რიცხვი")

average = (num1 + num2 + num3) / 3

print("სამი რიცხვის საშუალო:", average)

name = input("სეიყვანე სახელი:" )
print("სახელი სეიცავს:", len(name))

hours = int(input("საათი:"))
minutes = int(input("წუთი:"))
seconds = int(input("წამი:"))

total_seconds = hours * 3600 + minutes * 60 + seconds
print("სულ წამებში")

number = int(input("სეიყვანე რიცხვი:"))

if number > 100:
    print("big number:")
else:
    print("low number:")

a = int(input("შეიყვანე პირველი რიცხვი:"))
b = int(input("შეიყვანე მეორე რიცხვი:"))

print("მთლიანი გაყოფა:", a // b)
print("ნაშთი:", a % b)

n = int(input("შეიყვანე რიცხვი: "))

if n % 3 == 0 or n % 5 == 0:
    print("არის 3-ის ან 5-ის ჯერადი")
else:
    print("არცერთია ჯერადი არ არის")

for i in range(1, 11):
    print(i)

while True:
    text = input("შეიყვანე ტექსტი (stop გასასვლელად): ")
    if text.lower() == "stop":
        break

numbres = [5, 10, 15, 20]
average = sum(numbres) / len(numbres)
print("საშუალო: ", average)

nums = [1, 2, 3, 4]
doubled = [x * 2 for x in nums]
print("გაორმაგებული სია:", doubled)

nums = [4, 5, 19, 591, 5615]
print("უდიდესი რიცხვია:", max(nums))

word = input("სეიყვანე სიტყვა: ")
print("შეაბრუნე სიტყვა:", word[::-1])

n = int(input("შიყვანე n:"))
total = sum(range(1, n + 1))
print("ჯამი:", total)





