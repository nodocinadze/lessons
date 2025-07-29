
age = 16 
name = "ნოდო ცინაძე"  
for _ in range(age):
    print(name)

print("\n---\n")


for i in range(1, 21):
    print(i)

print("\n---\n")


for i in range(20, -1, -1):
    print(i)

print("\n---\n")


total = 0
for i in range(1, 51):
    total += i
print("ჯამი 1-დან 50-მდე:", total)

print("\n---\n")


even_sum = 0
for i in range(1, 11):
    if i % 2 == 0:
        even_sum += i
print("ლუწი რიცხვების ჯამი 1-დან 10-მდე:", even_sum)

print("\n---\n")


num = int(input("შეიყვანე რიცხვი: "))
for i in range(0, num + 1):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
