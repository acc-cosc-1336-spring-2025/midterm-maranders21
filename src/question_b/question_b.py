#write functions here, don't add input('') statements here!
def test_config_b():
    test_assess_1 = get_assessment_value(10000)
    if test_assess_1 != 6000:
        print(f"Error! The assessment value of 10000 returned {test_assess_1} instead of 6000")
        return False
    test_assess_2 = get_assessment_value(20000)
    if test_assess_2 != 12000:
        print(f"Error! The assessment value of 20000 returned {test_assess_2} instead of 12000")
        return False
    test_tax_1 = get_tax_assessed(6000)
    if test_tax_1 != 43.2:
        print(f"Error! The tax value of 6000 returned {test_tax_1} instead of 43.2")
        return False      
    test_tax_2 = get_tax_assessed(10000)  
    if test_tax_2 != 72:
        print(f"Error! The tax value of 10000 returned {test_tax_2} instead of 72")
        return False
    return True

def get_assessment_value (prop_val):
    assess_val = prop_val * 0.6
    return assess_val

def get_tax_assessed (assess_val):
    tax_val = assess_val / 100 * 0.72
    tax_val = round(tax_val, 2)
    return tax_val