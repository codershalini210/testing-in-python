"""
Exercise 4.2B -> fault order processor

 program processes a simple customer order ,
this program contains several defects that must be identified, corr
and corrected using proper debugging process

Order calculation rules :
1. subtotal = price* quantiy
  50 *5
  250
2. a 10% discount when subtotal is greater than 100, discount
should be calulated from the subtotal
250-25 =225
3. shipping in 5 when the amount after discount is below 50
225+0
4. quantity must be greater than 0
5. price must not be negative
6. function should return the final order total
"""


def calculate_order_total(price, quantity):
    try:
        subtotal = price * quantity  # correction 1 prevously it was price +quantity
        if subtotal > 100:
            discount = subtotal * 0.10
        else:
            discount = 0
        amount_after_discount = subtotal - discount
        if amount_after_discount < 50:  # correction 02  prevously it was >
            shipping = 5
        else:
            shipping = 0
        if quantity <= 0: #correction 3  prevously it was quantity<0
            raise ValueError("Quantity ,must be greater than 0") 
        if price<=0: #correction 4  prevously it was not present 
            raise ValueError("Price , must be a postive no ")
        
        return amount_after_discount + shipping
    except Exception as e:
        print(e)



final_cost = calculate_order_total(50, 5)
print(final_cost)  # 225
final_cost = calculate_order_total(10, 5)
print(final_cost)  # 50
final_cost = calculate_order_total(10, 4)
print(final_cost)  # 205
final_cost = calculate_order_total(10,0)
print(final_cost)
final_cost = calculate_order_total(-5,10)
print(final_cost)