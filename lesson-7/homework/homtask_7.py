import math

# 1. Modify String with Underscores
def modify_string(txt):
    vowels = "aeiou"
    result = []
    count = 0
    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            if i + 1 < len(txt) and txt[i + 1] not in vowels and txt[i] != '_':
                result.append('_')
            count = 0
        i += 1
    return ''.join(result)

print(modify_string("hello"))  # hel_lo
print(modify_string("assalom"))  # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

# 2. Integer Squares Exercise
def print_squares(n):
    for i in range(n):
        print(i ** 2)

print_squares(5)

# 3. Loop-Based Exercises

# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print pattern
for i in range(1, 6):
    print(*range(1, i + 1))

# Exercise 3: Calculate sum of all numbers from 1 to a given number
def sum_numbers(n):
    return sum(range(1, n + 1))

print("Sum is:", sum_numbers(10))

# Exercise 4: Print multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(n * i)

multiplication_table(2)

# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num in {75, 150, 145}:
        print(num)

# Exercise 6: Count total number of digits in a number
print(len(str(75869)))

# Exercise 7: Print reverse number pattern
for i in range(5, 0, -1):
    print(*range(i, 0, -1))

# Exercise 8: Print list in reverse order
list1 = [10, 20, 30, 40, 50]
for num in reversed(list1):
    print(num)

# Exercise 9: Display numbers from -10 to -1
for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution
for i in range(5):
    print(i)
print("Done!")

# Exercise 11: Print all prime numbers within a range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

prime_numbers(25, 50)

# Exercise 12: Display Fibonacci series up to 10 terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci(10)

# Exercise 13: Find the factorial of a given number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("5! =", factorial(5))

# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    from collections import Counter
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []
    for key in count1:
        if key not in count2:
            result.extend([key] * count1[key])
    for key in count2:
        if key not in count1:
            result.extend([key] * count2[key])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]

# Homework

# map va filter funksiyalarini tushuntiruvchi misollar
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, nums))
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Squares:", squares)
print("Even Numbers:", even_nums)

# 1. is_prime(n) funksiyasi
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(4))  # False
print(is_prime(7))  # True

# 2. digit_sum(k) funksiyasi
def digit_sum(k):
    return sum(map(int, str(k)))

print(digit_sum(24))  # 6
print(digit_sum(502))  # 7

# 3. Ikki sonning darajalari
def powers_of_two(N):
    k = 1
    while k <= N:
        print(k, end=' ')
        k *= 2
    print()

powers_of_two(10)  # 2 4 8
