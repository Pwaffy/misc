import math
import string
import itertools
import hashlib

courses = [
    "COWT10023",
    "COWT18888",
    "COWT28888",
    "DBAS14444",
    "DBAS17370",
    "DBAS35738",
    "ENGL17889GD",
    "INFO10111",
    "INFO16529",
    "INFO30004",
    "INFO32297",
    "INFO33192",
    "INFO33921",
    "INFO36206",
    "INFO37721",
    "INFO39207",
    "INFO40025",
    "INFO40051",
    "INFO40587",
    "INFO43921",
    "INFO46206",
    "INFO49402",
    "MATH14998",
    "MATH24178",
    "MATH26367",
    "MATH36206",
    "PROG12974",
    "PROG20025",
    "PROG23199",
    "PROG36577",
    "PROG36859",
    "PROG43431",
    "SYST18713",
    "SYST19534",
    "SYST27198",
    "SYST44288",
    "SYST44998",
    "SYST45713",
    "SYST45904",
    "TELE16048",
    "TELE29599",
    "TELE30004",
]

test = 0
# result = 37
result = "9e6748174634e2f9bce003cc7ae98c9d" # change this

def func(test):
    test = 88 * test + 101
    test = test % 199
    return test

def func1(test):
    test = 3 * test ** 2 + 7
    test = test % 53
    return test

def func2(test):
    counter = 0
    for n in range(test + 1):
        counter += n ** 2 + 1
        counter = counter % 33921
    counter = counter % 33921
    return counter

def func3(test):
    test *= math.pi
    test %= 1
    test *= 1000
    test = math.floor(test)
    return test

def func4(test):
    n = test ** 2 % 101
    for _ in range(n):
        test = 2 * test + 3
    test %= 101
    return test

def func5(test):
    return sum(ord(char) for char in test) % 100

def func6(test):
    return hashlib.md5(test.encode()).hexdigest()

# while True:
#     test += 1
#     if func4(test) == result:
#         print(test)
#         break
#     if test == 1000000:
#         print("stop")
#         break

# for chars in itertools.product(string.ascii_lowercase, repeat=3):
#     word = ''.join(chars)
#     if func5(word) == result:
#         print(word)
# else:
#     print("done")

for code in courses:
    if func6(code) == result:
        print(code)


