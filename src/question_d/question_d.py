#write functions here, don't add input('') statements here!

def test_config_d():
    num = 100
    use_local_variable(num)
    if num != 100:
        print(f"Error! Value should still be 100, not {num}!")
        return False
    return True

def use_local_variable(num):
    num = 10