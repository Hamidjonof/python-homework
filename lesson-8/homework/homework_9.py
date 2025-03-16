import os
import random

def handle_zero_division():
    try:
        a, b = 5, 0
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")

handle_zero_division()

def handle_value_error():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# handle_value_error()

def handle_file_not_found():
    try:
        with open("non_existent_file.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found!")

handle_file_not_found()

def handle_type_error():
    try:
        a, b = input("Enter two numbers: ").split()
        print(float(a) + float(b))
    except ValueError:
        print("Both inputs must be numbers.")

# handle_type_error()

def handle_permission_error():
    try:
        with open("restricted_file.txt", "w") as f:
            f.write("Test data")
    except PermissionError:
        print("Permission denied!")

# handle_permission_error()

def handle_index_error():
    try:
        lst = [1, 2, 3]
        print(lst[10])
    except IndexError:
        print("Index out of range!")

handle_index_error()

def handle_keyboard_interrupt():
    try:
        num = input("Enter a number: ")
        print(num)
    except KeyboardInterrupt:
        print("Input cancelled.")

# handle_keyboard_interrupt()

def handle_arithmetic_error():
    try:
        print(10 / 0)
    except ArithmeticError:
        print("Arithmetic error occurred!")

handle_arithmetic_error()

def handle_unicode_decode_error():
    try:
        with open("test.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        print("Encoding issue encountered.")

# handle_unicode_decode_error()

def handle_attribute_error():
    try:
        num = 10
        num.append(5)
    except AttributeError:
        print("Object has no such attribute!")

handle_attribute_error()

def read_entire_file():
    with open("sample.txt", "r") as f:
        print(f.read())

def read_n_lines(n):
    with open("sample.txt", "r") as f:
        for _ in range(n):
            print(f.readline().strip())

def append_text_to_file(text):
    with open("sample.txt", "a") as f:
        f.write(text + "\n")

def read_last_n_lines(n):
    with open("sample.txt", "r") as f:
        print("".join(f.readlines()[-n:]))

def read_file_into_list():
    with open("sample.txt", "r") as f:
        return f.readlines()

def read_file_into_variable():
    with open("sample.txt", "r") as f:
        return f.read()

def find_longest_words():
    with open("sample.txt", "r") as f:
        words = f.read().split()
        longest = max(words, key=len)
        print("Longest word:", longest)

def count_lines():
    with open("sample.txt", "r") as f:
        print("Line count:", len(f.readlines()))

def count_word_frequency():
    from collections import Counter
    with open("sample.txt", "r") as f:
        words = f.read().split()
        freq = Counter(words)
        print(freq)

def get_file_size():
    print("File size:", os.path.getsize("sample.txt"), "bytes")

def write_list_to_file(lst):
    with open("output.txt", "w") as f:
        f.writelines("\n".join(map(str, lst)))

def copy_file():
    with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
        dest.write(src.read())

def combine_files():
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("combined.txt", "w") as out:
        for line1, line2 in zip(f1, f2):
            out.write(line1.strip() + " " + line2)

def read_random_line():
    with open("sample.txt", "r") as f:
        print(random.choice(f.readlines()))

def check_file_closed():
    f = open("sample.txt", "r")
    print("Is closed:", f.closed)
    f.close()
    print("Is closed after closing:", f.closed)

def remove_newline_chars():
    with open("sample.txt", "r") as f:
        print([line.strip() for line in f])

def count_words_in_file():
    with open("sample.txt", "r") as f:
        words = f.read().replace(",", " ").split()
        print("Word count:", len(words))

def extract_chars_from_files():
    char_list = []
    for filename in os.listdir():
        if filename.endswith(".txt"):
            with open(filename, "r") as f:
                char_list.extend(f.read())
    print(char_list)

def generate_alphabet_files():
    for i in range(26):
        with open(chr(65 + i) + ".txt", "w") as f:
            f.write(chr(65 + i))

def create_letter_file(letters_per_line):
    with open("letters.txt", "w") as f:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(0, len(alphabet), letters_per_line):
            f.write(alphabet[i:i+letters_per_line] + "\n")
