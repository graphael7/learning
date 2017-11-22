keep_going = True
arr = []
x=1
while keep_going:
    found_prime = True
    while found_prime:
        x=x+1
        if x == 2:
            arr.append(x)
            found_prime = False
            print arr[-1]
        else:
            b = False
            for y in range(2,x-1):
                if x%y == 0:
                    b = True

            if not b:
                arr.append(x)
                found_prime = False
                print arr[-1]



    take_in = raw_input("Would you like the next Prime number?(y/n)")
    if take_in.lower() == 'n':
        keep_going = False
