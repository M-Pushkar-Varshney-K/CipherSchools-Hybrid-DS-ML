# Basics of Python for Beginners

# 1. If-Else Statement
print("1. If-Else Statement")
num = 10
if num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is not a positive number")

# 2. For Loop
print("\n2. For Loop")
for i in range(5):
    print(i)

# 3. While Loop
print("\n3. While Loop")
count = 0
while count < 5:
    print(count)
    count += 1

# 4. Set
print("\n4. Set")
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print("Set after adding an element:", my_set)

# 5. Dictionary
print("\n5. Dictionary")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Original Dictionary:", my_dict)
my_dict["email"] = "alice@example.com"
print("Dictionary after adding an element:", my_dict)

# 6. List
print("\n6. List")
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
my_list.append(6)
print("List after adding an element:", my_list)

# 7. Functions
print("\n7. Functions")
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 8. Lambda Functions
print("\n8. Lambda Functions")
add = lambda x, y: x + y
print("Sum using lambda function:", add(3, 5))

# 9. Error Handling
print("\n9. Error Handling")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("This block is always executed.")

# 10. Comprehensions
print("\n10. Comprehensions")
# List comprehension
squares = [x**2 for x in range(10)]
print("Squares using list comprehension:", squares)

# Set comprehension
unique_squares = {x**2 for x in range(10)}
print("Unique squares using set comprehension:", unique_squares)

# Dictionary comprehension
square_dict = {x: x**2 for x in range(10)}
print("Squares using dictionary comprehension:", square_dict)
