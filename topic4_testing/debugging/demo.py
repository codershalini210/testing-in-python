# price = int(input("Enter price"))
# quantity = int(input("Enter quantity"))
# # print("price",price)
# # print("quantity",quantity)
# total = price*quantity
# print(total)
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Invalid input"
    except:
        return "invalid case"
print(divide(10,2))
print(divide(10,0))
print(divide("4","b"))