#add import
from question_d import test_config_d
from question_d import use_local_variable

def main():
    if test_config_d() == False:
        return

    num = 15
    use_local_variable(num)
    print(num)


main()