import discount
# # write test cases for 
# test_normal_Case
def test_normal_Case():
    assert discount.calculate_discount(2000) ==300
def test_boundary_case():
    assert  discount.calculate_discount(5000)== 500
# def test_boundry_at_discount():

def test_boundary_below_discount():
    assert  discount.calculate_discount(3000) == 450
def test_boundary_above_discount():
    assert  discount.calculate_discount(5500) ==550