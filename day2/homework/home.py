print(5 > 3 and 8 > 6)         # True
print(10 > 20 and 5 < 10)      # False
print(7 > 2 or 4 > 10)         # True
print(3 < 1 or 2 > 5)          # False
print(4 < 6 and 8 == 8)        # True
print(10 > 5 or 5 > 10)        # True
print(2 < 3 and 9 < 8)         # False
print(12 > 7 or 6 < 3)         # True
print(7 == 7 and 10 <= 20)     # True
print(9 > 10 or 2 < 4)         # True

# and ოპერატორი — ორივე პირობა უნდა იყოს True, რომ შედეგიც True იყოს.
# თუ რომელიმე პირობა False იქნება, შედეგი იქნება False.

print(5 > 3 and 10 > 6)   # True, რადგან ორივე პირობა სწორია
print(5 > 8 and 10 > 6)   # False, რადგან პირველი პირობა არასწორია

# or ოპერატორი — ერთ-ერთი პირობა მაინც უნდა იყოს True, რომ შედეგი იყოს True.
# შედეგი False იქნება მხოლოდ მაშინ, როცა ორივე პირობაა False-ია.

print(5 > 3 or 10 > 6)    # True, რადგან ორივე პირობა სწორია
print(5 > 8 or 10 > 6)    # True, რადგან მეორე პირობა სწორია
print(5 > 8 or 2 > 9)     # False, რადგან არცერთი პირობა არ არის სწორი