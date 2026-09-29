import pytest
from unittest.mock import Mock
# from app import add, average_age, divide, multiply, sub, total_count
import app

# import app

def test_add():
    assert  app.add(2, 3) == 5


def test_add_one_str():
    assert  app.add( 3,2) == 5


def test_add_str():
    assert  app.add("a", "b") == "ab"

   #this function is a fixer , and I may need 
# to provide its result
# to my test cases
@pytest.fixture
def students():
    return [{"id":1,"age":21,"name":"A"},
            {"id":2,"age":22,"name":"B"},
            {"id":3,"age":23,"name":"C"}]

def test_average_age(students):
    assert  app.average_age(students)==22

def test_total_count(students):
    assert  app.total_count(students) ==3

def test_get_user_name():
    mock_response = Mock()
    mock_response.json.return_value = {"name":"John"}
    assert app.get_user_name(mock_response) == "Johny"