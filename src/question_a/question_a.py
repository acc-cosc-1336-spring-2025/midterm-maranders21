#write functions here, don't add input('') statements here!
def test_config_a():
    test_11 = get_sum_of_evens(11)
    if test_11 != 30:
        print("Error! Testing the value of 11 has failed.")
        return False
    test_10 = get_sum_of_evens(10)
    if test_10 != 30:
        print("Error! Testing the value of 10 has failed.")
        return False
    test_8 = get_sum_of_evens(8)
    if test_8 != 20:
        print("Error! Testing the value of 8 has failed.")
        return False
    return True

def get_sum_of_evens(num):
    return_sum = 0
    for i in range(2, num + 1, 2):
        return_sum += i
    return return_sum
