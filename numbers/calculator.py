import math

def add(first_num, second_num):
    return first_num + second_num

def subtract(first_num,second_num):
    return first_num - second_num

def divide(first_num,second_num):
    return first_num/float(second_num)

def multiply(first_num,second_num):
    return first_num * second_num

get_first = float(raw_input("What is first number?"))
get_operator = raw_input("What is Operator?")
get_second = float(raw_input("What is second number?"))

if get_operator == "+":
    print add(get_first,get_second)
elif get_operator == "-":
    print subtract(get_first,get_second)
elif get_operator == "/":
    print divide(get_first,get_second)
elif get_operator == "*":
    print multiply(get_first,get_second)
