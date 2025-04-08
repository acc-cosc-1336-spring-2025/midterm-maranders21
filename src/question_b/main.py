#add import
from question_b import test_config_b
from question_b import get_assessment_value
from question_b import get_tax_assessed

def main():
    if test_config_b() == False:
        return
    
    while True:
        actual_value = input("Enter property value or quit: ")
        if actual_value.lower() == "quit":
            break
        assess_val = get_assessment_value(int(actual_value))
        tax_val = get_tax_assessed(assess_val)
        print(f"Property Value: {actual_value}")
        print(f"Assessment Value: {assess_val}")
        print(f"Tax Assessed: {tax_val}")
    return

main()