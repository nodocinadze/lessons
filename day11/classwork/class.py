# task 1
# function არის კონსტრუქტორი, რომელიც იღებს პარამეტრად სახელს და არგუმენტს 

# task 2
text = "Hello, World!"

print(text.upper())  # ყველა ასოს გარდაქმნის დიდი ასოებად
print(text.lower())  # ყველა ასოს გარდაქმნის პატარა ასოებად
print(text.capitalize())  # პირველი ასოს გარდაქმნის დიდ ასოდ
print(text.find("World"))  # აბრუნებს სტრიქონის პოზიციას სადაც იწყება "World"


# task 3

number = [38, 21, 45, 67, 89, 12]

print(len(number))  # აბრუნებს სიის ელემენტების რაოდენობას
number.append(100)  # სიის ბოლოს დამატება
print(number)
number.insert(2, 50)  # დამატება კონკრეტულ პოზიციაზე
print(number)
number.pop(1)  # წაშლა კონკრეტული პოზიციიდან
print(number)

