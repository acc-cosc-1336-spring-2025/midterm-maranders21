#write functions here, don't add input('') statements here!
def test_config_c():
    test_0 = get_fahrenheit(0)
    if test_0 != 32:
        print(f"Error! 0 deg celsius should not return {test_0} deg fahrenheit!")
    test_5 = get_fahrenheit(5)
    if test_5 != 41:
        print(f"Error! 5 deg celsius should not return {test_5} deg fahrenheit!")
    test_10 = get_fahrenheit(10)
    if test_10 != 50:
        print(f"Error! 10 deg celsius should not return {test_10} deg fahrenheit!")
    return True

def get_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit = round(fahrenheit, 2)
    return fahrenheit