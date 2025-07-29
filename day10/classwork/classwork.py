# 1) b
# 2) c
# 3) c
# 4) 
def hello():
    print("hello world")



def opposite(number):
    return -number
print(opposite(5))
print(opposite(-7))


def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
print(even_or_odd(3))
print(even_or_odd(8))



def sum_of_positives(numbers):
    return sum(n for n in numbers if n > 0)

print(sum_of_positives([1, -2, 3, 4, -5]))
print(sum_of_positives([-1, -2, -3]))
# 1) b
# 2) c
# 3) b
# 4) d
# 5) if-ის მიზანია პროგრამას მისცეს გადაწყვეტილების მიღების უნარი მაგ:
age = 18 

if age >= 18:
    print("ცოლის მოყვანის დროა")
else:
    print("ჯერ ადრეა პატარა კაცი")

# 6)
def square(number):
    return number ** 2
print(square(4))
