from gradesCalc import *


# Testing your implemented functions, feel free to add more tests below
def main():
    # Testing the `final_grade` function
    input_path = 'tests/input.txt'
    output_path = 'tests/out.txt'
    course_avg = final_grade(input_path=input_path, output_path=output_path)
    assert course_avg == 70

    # Testing the `check_strings` function
    s1 = 'a'
    s2 = ""
    result = check_strings(s1=s1, s2=s2)
    assert not result
    s3 = 'aa'
    s4 = 'aA'
    result = check_strings(s3, s4)
    assert result


if __name__ == "__main__":
    main()
