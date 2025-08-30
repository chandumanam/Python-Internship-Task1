my_list = [1, 2, 3, 4, 5, 2, 3]
my_tuple = (10, 20, 30)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Chandu", "role": "Data Science Intern"}

print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

def sum_of_squares(numbers):
    """Return sum of squares of numbers in a list"""
    return sum([x**2 for x in numbers])

print("Sum of squares:", sum_of_squares([1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (lambda + filter):", even_numbers)

def factorial(n):
    """Recursive function to find factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

squares = [x**2 for x in range(1, 6)]
print("Squares using list comprehension:", squares)

def clean_data(data):
    """Remove duplicates and filter only positive numbers"""
    cleaned = list(set(data))  # remove duplicates
    filtered = [x for x in cleaned if x > 0]  # keep only positive numbers
    return filtered

raw_data = [10, -5, 3, 10, 0, -2, 3, 5]
cleaned_data = clean_data(raw_data)
print("Raw data:", raw_data)
print("Cleaned data:", cleaned_data)
