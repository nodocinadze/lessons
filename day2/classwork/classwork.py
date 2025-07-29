def make_tea():
    print("1:წყლის ჩასხმა მადუღარაში")

    print("2:წყლის ადუღება")

    print("3:ჩაის პაკეტის მოთავსება ჭიქაში")

    print("4:წყლის დასხმა ჭიქაში")

    print("5:ჩაის დაყენება (3-5წუთი)")

    print("6:სურვილისამებრ შაქრის დამატება")

    print("7:ჩაის მირთმევა")


for i in range(1,11):
    if i % 7 == 0:
        print(f"{i}")
    else:
        print(i)

while True:
    age = int(input("გთხოვტ შეიყვანოთ თქვენი ასაკი: "))
    if age >= 18:
        print("შეგიძლიათ შეიძენთ ბილეთები")
        break
    else:
        print("თქვენ ვერ შეიძენთ ბილეთებს")
        break

num = int(input("შეიწვანე რიცხვი"))

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

secret_number = 9

while True:
    guess = int(input("გამოიცანი საიდუმლო რიცხვი"))

    if guess == secret_number:
        print("გილოცავთ! თქვენ სწორედ გამოიცანით")
        break
    else:
        print("არასწორია სცადეთ ისევ")
