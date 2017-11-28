
num = int(raw_input("What is the number to start with"))
steps = 0
while not num == 1:
    steps = steps +1
    if num % 2 == 0:
        num = num/2
    else:
        num = (num * 3) + 1

print steps
