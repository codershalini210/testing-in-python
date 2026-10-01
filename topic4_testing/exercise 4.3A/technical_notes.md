# Technical Notes – Exercise 4.3A Quality Review and Refactor

## 1. Overview

This document records the technical decisions made while reviewing and refactoring the `process_order` component.

The main objective of the refactoring was to improve code quality, readability, documentation and maintainability without changing the required order calculation rules.

The original component used direct `print()` statements and contained repeated output. The refactored component returns a formatted summary string instead.

---

## 2. Technical Changes Made

| Area                | Baseline Code                               | Refactored Code                          | Reason for Change                                       |
| ------------------- | ------------------------------------------- | ---------------------------------------- | ------------------------------------------------------- |
| Function parameters | Parameters had no type information          | Added type hints                         | Makes expected input types clearer                      |
| Documentation       | No function-level documentation             | Added a detailed docstring               | Explains purpose, inputs, outputs and calculation rules |
| Output handling     | Used multiple `print()` statements          | Builds and returns a string              | Makes the function easier to reuse and test             |
| Duplicate output    | Customer and final total were printed twice | Duplicate statements removed             | Avoids unnecessary repeated output                      |
| Formatting          | Basic formatting                            | Improved spacing and line structure      | Improves readability                                    |
| Variable naming     | Basic names such as `subtotal` and `total`  | Clear existing names retained            | Names already describe their purpose                    |
| Order status        | Printed directly                            | Added to the returned message            | Keeps output generation within the returned result      |
| Testing             | Function called directly                    | Returned result is printed by test cases | Allows the function to return a testable value          |

---

## 3. Decision: Add Type Hints

Type hints were added to the function parameters:

```python
def process_order(
    customer: str,
    price: float,
    quantity: int,
    member: bool
) -> str:
```

The type hints document the expected data types.

* `customer` is expected to be a string.
* `price` is expected to be a floating-point number.
* `quantity` is expected to be an integer.
* `member` is expected to be a Boolean value.
* The function returns a string.

Type hints improve readability and make the intended use of the function clearer.

They do not perform automatic validation of the input values.

---

## 4. Decision: Add a Function Docstring

A docstring was added to document the purpose and behaviour of the function.

The docstring describes:

* What the function does
* The parameters it accepts
* The value it returns
* The discount rules
* The order-status rule

This provides technical documentation directly alongside the code and makes the function easier for another developer to understand.

---

## 5. Decision: Replace Direct Printing with a Return Value

### Baseline approach

The original function printed each result directly:

```python
print("Customer:", customer)
print("Final total:", total)
```

This means the function is responsible for both calculating the order and displaying the result.

### Refactored approach

The function now creates a summary message and returns it:

```python
return message
```

The test code is responsible for displaying the returned value:

```python
print(process_order("Aisha", 30, 2, False))
```

This separates the calculation/output creation from the decision about where the result should be displayed.

It also makes the function easier to test because the returned value can be checked directly.

---

## 6. Removal of Duplicate Statements

The baseline code contained duplicate output:

```python
print("Customer:", customer)
print("Final total:", total)
```

These statements appeared again after the order-status output.

The repeated statements did not provide additional information, so they were removed from the working implementation.

This reduces unnecessary code and prevents the same information from being displayed twice.

---

## 7. Discount Calculation

The original discount rules were retained.

### Order discount

A 10% discount is applied when:

```text
subtotal > 100
```

The calculation is:

```python
discount = subtotal * 0.10
```

If the subtotal is 100 or below:

```python
discount = 0
```

### Membership discount

A 5% membership discount is applied when:

```python
member == True
```

The calculation is:

```python
member_discount = subtotal * 0.05
```

If the customer is not a member, the membership discount is zero.

No changes were made to these business rules during the refactoring.

---

## 8. Final Total Calculation

The final total continues to use the same calculation as the baseline:

```python
total = subtotal - discount - member_discount
```

The calculation order was not changed.

This was important because the purpose of the exercise was to improve code quality without changing the required behaviour.

---

## 9. Order Status Decision

The existing order-status rule was retained:

```python
if total >= 100:
    message = message + "Order status: Standard \n"
else:
    message = message + "Order status: Small \n"
```

The classification is therefore:

|   Final Total | Status   |
| ------------: | -------- |
|   100 or more | Standard |
| Less than 100 | Small    |

The boundary condition `>= 100` was preserved from the baseline implementation.

---

## 10. Test Cases

The same three customer scenarios were retained after refactoring.

```python
print(process_order("Aisha", 30, 2, False))

print(process_order("Ben", 60, 2, True))

print(process_order("Chloe", 50, 3, False))
```

Keeping the same test cases allows the refactored version to be compared with the baseline version.

### Expected calculations

| Customer | Price | Quantity | Member | Subtotal | Discount | Member Discount | Final Total | Status   |
| -------- | ----: | -------: | ------ | -------: | -------: | --------------: | ----------: | -------- |
| Aisha    |    30 |        2 | No     |       60 |        0 |               0 |          60 | Small    |
| Ben      |    60 |        2 | Yes    |      120 |       12 |               6 |         102 | Standard |
| Chloe    |    50 |        3 | No     |      150 |       15 |               0 |         135 | Standard |

The calculation rules remain consistent with the baseline implementation.

---

## 11. Code Quality Improvements

The refactoring addressed several basic code-quality areas.

### Readability

Type hints, meaningful variable names and a function docstring make the purpose of the code easier to understand.

### Maintainability

Returning a result rather than printing each value makes the function easier to reuse in another part of an application.

### Duplication

Repeated customer and final-total output was removed.

### Documentation

The function now documents its inputs, output and business rules.

### Consistency

The same calculation rules and test scenarios were retained after the changes.

---

## 12. Formatting Considerations

The refactored file was formatted to make the structure easier to read.

The following areas were reviewed:

* Indentation
* Blank lines
* Function definition formatting
* Long lines
* Spacing around operators
* String formatting
* Naming consistency

The code can also be checked using the quality tools specified for the exercise, such as Black, Ruff or Pylint.

---

## 13. Behaviour Preservation

The main technical constraint was to improve the internal quality of the component without changing the required calculation behaviour.

The following behaviour was preserved:

1. Subtotal is calculated using price multiplied by quantity.
2. A 10% discount is applied when the subtotal is greater than 100.
3. A 5% membership discount is applied for members.
4. Both discounts are deducted from the subtotal.
5. A final total is calculated.
6. Orders with a final total of 100 or more are classified as `Standard`.
7. Orders below 100 are classified as `Small`.

The main change is how the result is handled: the refactored function returns a formatted summary instead of directly printing each individual value.

---

## 14. Technical Limitations

The current function is intentionally simple for the quality-review exercise.

It does not currently validate:

* Negative prices
* Zero or negative quantities
* Empty customer names
* Invalid data types
* Invalid membership values

These checks were not added because they would introduce additional behaviour beyond the scope of the controlled refactoring exercise.

---

## 15. Refactoring Summary

The refactoring focused on improving the existing component rather than redesigning it.

The main improvements were:

* Added type hints.
* Added a function docstring.
* Improved formatting and readability.
* Removed duplicated output.
* Changed the function to return a formatted result.
* Preserved the existing discount calculations.
* Preserved the existing order-status rules.
* Retained the original test scenarios.
* Documented the technical decisions made during the refactoring.

The refactored component is therefore easier to read, document, test and reuse while retaining the intended calculation logic.
