"""
Exercise 4.3A - Quality Review and Refactor Practice Component

This is a simple working component for a quality review exercise.
"""


def process_order(customer: str, price: float, quantity: int, member: bool) -> str:
    """Calculate the total for a customer order and return a status summary.

    This function calculates the subtotal for an order, applies discounts based on
    order value and membership status, and returns a formatted message describing
    the customer's purchase and final order status.

    Args:
        customer (str): The name of the customer placing the order.
        price (float): The unit price of each item in the order.
        quantity (int): The number of items ordered.
        member (bool): True if the customer is a member and eligible for the
            membership discount; False otherwise.

    Returns:
        str: A multi-line summary containing the customer name, unit price,
        quantity, subtotal, applicable discounts, final total, and order status.

    Notes:
        - A 10% discount is applied when the subtotal exceeds 100.
        - A 5% membership discount is applied only if `member` is True.
        - The order is classified as "Standard" when the final total is at least
          100, otherwise it is classified as "Small".
    """

    subtotal = price * quantity

    if subtotal > 100:
        discount = subtotal * 0.10
    else:
        discount = 0

    if member:
        member_discount = subtotal * 0.05
    else:
        member_discount = 0

    total = subtotal - discount - member_discount

    message = f"Customer: {customer} \n Price: {price} \n Quantity:  {quantity} \n Subtotal {subtotal} \n"
    message = message+ f"Discount : {discount} \n member_discount: {member_discount} \n Final Total {total} \n"
    

    if total >= 100:
        message = message + "Order status: Standard \n"
    else:
        message = message + "Order status: Small \n"
    return message
    # below two are the repeated statements
    # print("Customer:", customer)
    # print("Final total:", total)



print(process_order("Aisha", 30, 2, False))

print(process_order("Ben", 60, 2, True))
print(process_order("Chloe", 50, 3, False))
