# PEP8 is a set of python style guidelines
# naming conventions
# customer_name
#shipping is free for orders having total greater than 50
def calculate_total(price, quantity):
    total = price * quantity  
    if(total>50):
        shipping = 0
    else:
        shipping = 5
    return total +shipping


print(calculate_total(10, 2))
