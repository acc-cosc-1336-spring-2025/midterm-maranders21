#add import
from question_c import test_config_c
from question_c import get_fahrenheit

def main():
    if test_config_c() == False:
        return
    
    for cel in range(0, 21, 1):
        print(cel, '\t', get_fahrenheit(cel))

main()