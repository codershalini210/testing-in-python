import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename="logeg.log",
                    filemode="a")
def divide(a,b):
    try:
        result = a/b
        logging.info(f" {a} divide by {b} is {result}")
        return result
    except ZeroDivisionError:
        logging.info(f"Divide by zero error")
        return "Divide by zero error"
    except:
        logging.info(f"Exception occurs")
        return "Exception occur"
print(divide(10,20))
# print(divide(10,0))
print(divide("4","b"))