import pdb

get_cost = float(raw_input("What is the cost?"))
get_amt_paid = float(raw_input("What is the amount of money given?"))
quarters = 0
dimes=0
nickels=0
pennies=0
remaining = round(get_amt_paid - get_cost,2)

while round(remaining,2) > 0:

    if remaining >= .25:
        quarters = int(remaining/.25)
        remaining = remaining - (quarters * .25)
    elif remaining >= .10:
        dimes = int(remaining/.10)
        remaining = remaining - (dimes * .10)
    elif remaining >= .05:
        nickels = int(remaining/.05)
        remaining = remaining - (nickels * .05)
    elif remaining >= .01:
        pennies = int(remaining/.01)
        remaining = remaining - (pennies * .01)


print "Quarters:" + str(quarters)
print "Dimes:" + str(dimes)
print "Nickels:" + str(nickels)
print "Pennies:" + str(pennies)
