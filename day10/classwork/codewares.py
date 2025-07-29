# 1)
def reverse_string(text):
    return text[::-1]

# 2)
def find_smallest(number):
    return min(number)

print(find_smallest([5, 3, 7, 1, 9])) 

# 3) 
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# 4)
def count_words(sentence):
    words = sentence.split()
    return len(words)

# 5)
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

# 6)
def sum_middle(lst):
    if len(lst) <= 2:
        return 0
    return sum(lst) - max(lst) - min(lst)