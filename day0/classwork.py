goa = ["nika","luka","dachi","danieli"]
for i in goa:
  print (i)

name = "nodo tsinadze"

print(name.lower)
print(name.upper)
print(name.capitalize)
print(name.find("n"))

films = ["rush hour","fast and fourious","sherekilebi"]

films.append("run niggers")



films.insert(1,"taxi_3")
print(films)


films.pop(0)
print(films)

for films in films:
    print(films)

def calculator(num1, num2, operations):
    # adding
    if operations == "+":
        print(int(num1) + int(num2))
    elif operations == "-":
        print(int(num1) - int(num2))
    elif operations == "*":
        print(int(num1) * int(num2))
    elif operations == "//":
        print(int(num1) // int(num2))
    elif operations == "/":
        print(int(num1) / int(num2))
    else:
        print("no valid operations")


numbers = []
i = 0
while True:
    numbers.append(i)
    i += 1