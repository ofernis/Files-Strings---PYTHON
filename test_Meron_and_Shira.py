from gradesCalc import *




# Testing your implemented functions, feel free to add more tests below
def main():
    # Testing the `final_grade` function
    input_path = 'tests/input'
    output_path = 'tests/out'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    assert course_avg == 70
    tests_courses_avgs = [0,64,61,88,65,68]
    
    for i in range(6):
        course_avg = final_grade(input_path=input_path+str(i), output_path=output_path+str(i))
        assert tests_courses_avgs[i] == course_avg
    

    # Testing the `check_strings` function
    s1 = 'naanb'
    s2 = 'baNaNa'
    result = check_strings(s1=s1, s2=s2)
    assert result

    
    is_constructed_from = check_strings("aabbcc","abcabc")
    assert is_constructed_from is True
    is_constructed_from = check_strings("caba","abcabc")
    assert is_constructed_from is True
    is_constructed_from = check_strings("aaa","abcabc")
    assert is_constructed_from is False
    is_constructed_from = check_strings("naanb","baNaNa")
    assert is_constructed_from is True   
    is_constructed_from = check_strings("ananas","baNaNa")
    assert is_constructed_from is False  
    is_constructed_from = check_strings("bannn","baNaNa")   
    assert is_constructed_from is False    
    
    is_constructed_from = check_strings("","")
    assert is_constructed_from is True  
    is_constructed_from = check_strings("a","")
    assert is_constructed_from is False  
    is_constructed_from = check_strings("","a")
    assert is_constructed_from is True  
    is_constructed_from = check_strings("Sarah","Haras")
    assert is_constructed_from is True  
    is_constructed_from = check_strings("St","sttt")
    assert is_constructed_from is True  
    is_constructed_from = check_strings("sttt","st")
    assert is_constructed_from is False 
    print("Congrats!! Passed All tests!")

        
if __name__ == "__main__":
    main()
