import math

num_digits = int(raw_input("How many digits?"))
fib_series = [1,1]

if num_digits == 2:
    print str(fib_series[0]) + " " + str(fib_series[1])
elif num_digits == 1:
    print fib_series[0]
elif num_digits <= 0:
    print "incorrect value"
else:
    print str(fib_series[0]) + " " + str(fib_series[1]),
    for x in range(1,num_digits-1):
        next = fib_series[x] + fib_series[x-1]
        fib_series.append(next)
        print str(next),
