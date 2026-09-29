import logging

logging.basicConfig(
    filename="app.log", level=logging.ERROR, format="%(levelname)s: %(message)s"
)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def test_divide(a, b):
    try:
        r = divide(a, b)
    except Exception as e:
        logging.error(f"Error in divide {e}")


test_divide(10, 0)
# create a function that gives avg of ages from the dic passed as parameter
#  [{"id":1,"age":21,"name":"A"},
#             {"id":2,"age":22,"name":"B"},
#             {"id":3,"age":23,"name":"C"},
#  sum(21,22,23)
def average_age(pstudents):
    total_age = sum(stu["age"] for stu in pstudents)
    avg = total_age/len(pstudents)
    return avg

def total_count(pstudents):
    return len(pstudents) 
 
# print(average_age(students))     # 22   
# print(total_count(students))
def get_user_name(response):
    data = response.json()
    return data["name"]
