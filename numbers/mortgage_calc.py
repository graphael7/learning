import math

number_of_terms = 60
interest_rate = .034/12
months_to_payoff = 0

get_property_cost = float(raw_input("What is the cost of the property?"))
print get_property_cost
monthly_payments = (get_property_cost * (interest_rate * math.pow((1+interest_rate), number_of_terms)))/(math.pow((1 + interest_rate),number_of_terms) - 1)

print monthly_payments
