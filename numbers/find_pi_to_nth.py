
import math

amt_digits = int(raw_input("How many digits of PI do you want?"))

pi_approx = 22/7.0
print round(pi_approx, amt_digits)
print '%.*f' % (amt_digits, pi_approx)


print '%.*f' % (amt_digits, math.pi)
