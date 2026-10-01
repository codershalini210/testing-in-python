# Order Processing Component

## Overview

This Python program processes a customer order and calculates the final amount based on the order value and customer membership.

The program calculates:

* Subtotal
* Order discount
* Membership discount
* Final total
* Order status

## Function

The main function is:

```python
process_order(customer, price, quantity, member)
```

### Parameters

| Parameter  | Type    | Description                                |
| ---------- | ------- | ------------------------------------------ |
| `customer` | `str`   | Name of the customer                       |
| `price`    | `float` | Price of one item                          |
| `quantity` | `int`   | Number of items ordered                    |
| `member`   | `bool`  | Indicates whether the customer is a member |

## Calculation Rules

### Subtotal

The subtotal is calculated using:

```text
subtotal = price × quantity
```

### Order Discount

If the subtotal is greater than 100, a 10% discount is applied.

```text
discount = subtotal × 10%
```

If the subtotal is 100 or less, no order discount is applied.

### Membership Discount

If the customer is a member, a 5% membership discount is applied to the subtotal.

```text
member discount = subtotal × 5%
```

Non-members receive no membership discount.

### Final Total

The final total is calculated as:

```text
final total = subtotal - discount - member discount
```

### Order Status

The order status depends on the final total.

|   Final Total | Order Status |
| ------------: | ------------ |
|   100 or more | Standard     |
| Less than 100 | Small        |

## Example

```python
print(process_order("Aisha", 30, 2, False))
```

Output:

```text
Customer: Aisha
Price: 30
Quantity: 2
Subtotal: 60
Discount: 0
Member discount: 0
Final total: 60
Order status: Small
```

## Test Data

The program includes the following sample orders:

| Customer | Price | Quantity | Member | Final Total | Status   |
| -------- | ----: | -------: | ------ | ----------: | -------- |
| Aisha    |    30 |        2 | No     |          60 | Small    |
| Ben      |    60 |        2 | Yes    |       102.0 | Standard |
| Chloe    |    50 |        3 | No     |       135.0 | Standard |

## Running the Program

Save the Python code in a file such as:

```text
process_order.py
```

Run it from the terminal:

```bash
python process_order.py
```

The program will process the sample orders and display the order summaries.
