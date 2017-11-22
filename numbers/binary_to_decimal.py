import math

binary_decimal = raw_input("Would you like to convert 1)binary to decimal or 2)decimal to binary?(type number choice)")
sum = 0
if binary_decimal == "1":
    binary_input = raw_input("What is the binary number you want to change to decimal?")
    ending = len(binary_input)
    for x in range(0,ending):
        sum = sum + (int(binary_input[x-1])*math.pow(2,(ending - x-1)))
    print sum
elif binary_decimal == "2":
    binary_arr = []
    quotient = int(raw_input("What is the decimal number you want to change to binary?"))
    while quotient > 0:
        remainder = quotient%2
        quotient = quotient/2
        binary_arr.append(remainder)
    for i in reversed(binary_arr):
        print i,
