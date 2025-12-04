# task 1

for i in range(5):
    print(i)

for i in range(2,5,1):
    print(i)

for i in range (10,0,-2):
    print(i)

# task 2

i = 0
while i < 5:
    print(i)
    i += 1

i = 10
while i > 0:
    print(i)
    i -= 2

i = 2
while i < 10:
    print(i)
    i += 2

# task 3
# for loop გამოიყენება მაშინ როდესაც ვიცით რამდენჯერ უნდა შესრულდეს ციკლი
# მაგალითად
for i in range(5):
    print("hello world")

# while loop გამოიყენება მაშინ როდესაც არ ვიცით რამდენჯერ უნდა შესრულდეს ციკლი
# მაგალითად
i = 0
while i < 5:
    print("hello world")
    i += 1

# task 4
age = 17

if age >= 18:
    print("srulwlovani xar")
elif age == 17:
    print("erti welic da")
else:
    print("ar srulwlovani xar")

age = 15

if age >= 18:
    print("no discount")
elif age <= 16:
    print("10% discount")
else:
    print("5% discount")

age = 20

if age >= 18:
    print("adult")
    if age >= 65:
        print("senior citizen")
else:
    print("kid")

score = 50

if score == 100:
    print("A+")
    if score >= 90:
        print("A")
        if score >= 80:
            print("B")
else :
    print("C")
