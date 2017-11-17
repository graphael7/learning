import math

amt_digits = int(raw_input("What number would you like factors for?"))
arr = []
for x in range(1,amt_digits-1):
    if amt_digits%x == 0:
        arr.append(x)

print arr
