def opposite(number):
    return number * -1


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    if boolean == False:
        return "No"
    

def remove_char(s):
    return s[1:-1]
    

def is_isogram(string):
    string = string.lower()
    counter = 0
    for letter in string:
        occurences = string.count(letter)
        counter +=occurences
    return counter == len(string)

print(is_isogram("Dermatoglyphics"))


def find_short(s):
    s_list = s.split()
    starting_point = len(s_list[0])
    for word in s_list:
        if len(word) < starting_point:
            starting_point = len(word)
    return starting_point


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


def friend(x):
    friends = []
    for name in x:
        if len(name) == 4:
            friends.append(name)
    return friends


def likes(names):
    n = len(names)
    
    if not names:
        return 'no one likes this'
    if n == 1:
        return f'{names[0]} likes this'
    if n == 2:
        return f'{names[0]} and {names[1]} like this'
    if n == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    
    return f'{names[0]}, {names[1]} and {n - 2} others like this'