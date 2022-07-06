#!/usr/bin/python3
def fizzbuzz():
    string = range(1, 101)
    new_list = list(string)
    for i in new_list:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz ", end="")
        elif i % 3 == 0:
            print("fizz ", end="")
        elif i % 5 == 0:
            print("buzz ", end="")
        else:
            print(f"{i} ", end="")
