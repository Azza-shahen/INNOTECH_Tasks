
##########LAB (1) Python Basics##########
# 1. Compute Area of a Circle
import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"Area of the circle = {area:.2f}")

# 2. Check if a Number is Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# 3. Sum of Three Integers (0 if two are equal)
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if a == b or b == c or a == c:
    print("Sum = 0")
else:
    print(f"Sum = {a + b + c}")

# 4. Natural Numbers Summation Pattern
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
    print(f"{' + '.join(str(x) for x in range(1, i + 1))} = {sum}")

# 5. Check Prime Number
num = int(input("Enter a number: "))
if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

# 6. First 16 Powers of 2 Starting from 1
for i in range(16):
    print(f"2^{i} = {2**i}")

# 7. All Even Numbers from 1 to n (Given Range)
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Even numbers in the range:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
# -------------------------
# LAB (2) - Python Fundamentals
# -------------------------

# ======= BASICS =======

# 1. Convert inches to centimeters
inches = float(input("Enter length in inches: "))
cm = inches * 2.54
print(f"Length in centimeters = {cm:.2f}")

# 2. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

# 3. Volume of a Sphere
radius = float(input("Enter radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
print(f"Volume of sphere: {volume:.2f}")

# 4. Gross and Net Pay
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
gross = hours * rate
net = gross * 0.80
print(f"Gross Pay: {gross:.2f}, Net Pay: {net:.2f}")

# 5. Print numbers 1 - 10
for i in range(1, 11):
    print(i, end=" ")
print()

# 6. Accept numbers until a negative is entered
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break

# 7. Range identifier
num = int(input("Enter a number: "))
if 0 <= num <= 10:
    print("Range 1: 0 to 10")
elif 11 <= num <= 20:
    print("Range 2: 11 to 20")
elif 21 <= num <= 30:
    print("Range 3: 21 to 30")
elif 31 <= num <= 40:
    print("Range 4: 31 to 40")
else:
    print("Out of range")

# ======= STRINGS =======

# 1. Reverse a string
s = "1234abcd"
print("Reversed string:", s[::-1])

# 2. Count upper and lower case letters
def count_case(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    print("Upper case characters:", upper)
    print("Lower case characters:", lower)

count_case('The quick Brow Fox')

# 3. Palindrome check
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print("Palindrome:", is_palindrome("madam"))

# ======= LISTS =======

# 1. Distinct elements from list
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,2,3,3,3,3,4,5]))

# 2. Even numbers from list
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

print(even_numbers([1,2,3,4,5,6,7,8,9]))

# 3. Kth largest element
def kth_largest(lst, k):
    return sorted(lst, reverse=True)[k-1]

print(kth_largest([3, 1, 4, 2, 5], 2))  # 2nd largest

# 4. Check if list is a palindrome
def is_list_palindrome(lst):
    return lst == lst[::-1]

print(is_list_palindrome([1, 2, 3, 2, 1]))

# 5. Shopping list and access specific items
shopping = ["milk", "bread", "eggs", "tea", "coffee", "sugar", "cheese", "butter", "jam", "soap"]
print("Full list:", shopping)
print("Item 2:", shopping[1])
print("Item 8:", shopping[7])

# 6. Insert item into shopping list
shopping.insert(5, "biscuits")
print("Updated list:", shopping)

# ======= DICTIONARIES =======

# 1. Sort dictionary by value
d = {'a': 3, 'b': 1, 'c': 2}
print("Ascending:", dict(sorted(d.items(), key=lambda item: item[1])))
print("Descending:", dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))

# 2. Check if key exists
key = 'a'
print("Key exists?" , key in d)

# 3. Iterate over dictionary
for k, v in d.items():
    print(f"{k} : {v}")

# 4. Dictionary of squares
squares = {x: x**2 for x in range(1, 11)}
print("Squares:", squares)

# 5. Employee data
employees = {
    1001: {"name": "John", "age": 30},
    1002: {"name": "Jane", "age": 25}
}
print("Employees:", employees)

# ======= FUNCTIONS =======

# 1. Square a number
def square(n):
    return n ** 2

num = int(input("Enter number to square: "))
print("Squared:", square(num))

# 2. Max of two numbers
def max_of_two(a, b):
    return a if a > b else b

print("Max:", max_of_two(3, 7))

# ======= OOP =======

# 1. Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

c = Circle(5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())

# 2. Person class
from datetime import datetime

class Person:
    def __init__(self, name, country, birthdate):
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

p = Person("Alice", "USA", "2000-05-20")
print("Age:", p.age())

# 3. Calculator class
class Calculator:
    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def div(self, a, b): return a / b if b != 0 else "Error"

calc = Calculator()
print("Add:", calc.add(5, 3))
print("Divide:", calc.div(10, 2))

# 4. Shape class and subclasses
class Shape:
    def area(self): pass
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self): return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

shapes = [Square(4), Triangle(3, 4, 5)]
for s in shapes:
    print(type(s).__name__, "Area:", s.area(), "Perimeter:", s.perimeter())

