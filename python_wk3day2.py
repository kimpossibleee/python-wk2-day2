'''
Exercise 1) Filter out all of the empty strings from the list below
'''

places = [" ", "Argentina", " ", "San Diego",
          "", "  ", "", "Boston", "New York"]
print(list(filter(lambda x: x.strip() != '', places)))

'''
Exercise 2) Write an anonymous function that sorts this list by the last name
'''
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield",
          "David hassELHOFF", "Gary A.J. Bernstein"]

author.sort(key=lambda name: name.split(" ")[-1].lower())
print(author)

'''
Exercise 3) Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
'''
places = [('Nashua', 32), ("Boston", 12), ("Los Angelos", 44), ("Miami", 29)]

print(
    list(map(lambda location: (location[0], location[1]*(9/5) + 32), places)))

'''
Exercise 4) Write a recursion function to perform the fibonacci sequence up to the number passed in.
'''
def fibonacci(x):
    if x <= 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(5))
