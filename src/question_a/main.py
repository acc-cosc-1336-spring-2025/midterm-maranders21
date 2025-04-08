#add import
from question_a import test_config_a
from question_a import get_sum_of_evens

def main():
    if test_config_a() == False:
        return
    
    while True:
        user_num = input("Enter number or quit: ")
        if user_num.lower() == "quit":
            break
        total = get_sum_of_evens(int(user_num))
        print(total)
    return

main()