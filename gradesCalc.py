MIN_SEMESTER = 1
MIN_GRADE = 50
MAX_GRADE = 100

# The function checks whether the first digit in the given string is zero and returns
# True/False accordingly
def isFirstDigitZero(id: str) -> bool:
    return id[0] == 0

# The function checks whether the length of the given number is eight digits and
# returns True/False accordingly
def isLengthEightDigits(id: int) -> bool:
    return  int(id) >= pow(10, 7) and int(id) < pow(10,8)

# The function checks whether the given ID is valid and returns
# True/False accordingly
def isValidID(id: int) -> bool:
    return not isFirstDigitZero(id) and isLengthEightDigits(id)

# The function checks whether the given name is valid and returns
# True/False accordingly
def isValidName(name: str) -> bool:
    for character in name:
        if not character.isalpha() and character != ' ':
            return False
    return True

# The function checks whether the given semester string is eight and returns
# True/False accordingly
def isValidSemester(semester: int) -> bool:
    return int(semester) >= MIN_SEMESTER

# The function checks whether the given homework average is valid and returns
# True/False accordingly
def isValidHomeworkAvg(homework_avg: int) -> bool:
    return int(homework_avg) > MIN_GRADE and int(homework_avg) <= MAX_GRADE

# The function return the value of the highest integer which is smaller than
# the given number
def floor(num: int) -> int:
    return int(int(num) // 1)

# The function calculates the final grade based on the given ID is and 
# the homework average
def calculateFinalGrade(id: int, homework_avg: int) -> int:
    id_last_two_digits = int(id) % 100
    return floor((id_last_two_digits + int(homework_avg)) / 2)

# The function checks whether the given info is valid and returns
# True/False accordingly
def isInfoValid(id: int, name: str, semester: int, homework_avg: int) -> bool:
    return isValidID(id) and isValidName(name) and \
           isValidSemester(semester) and isValidHomeworkAvg(homework_avg)

#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output
def final_grade(input_path: str, output_path: str) -> int:
    read_file = open(input_path, 'r')
    write_file = open(output_path, 'a')
    student_grades = {}
    sum_of_final_grades = 0

    for line in read_file:
        student_info = line.split(',')
        id = student_info[0].replace(" ", "")
        name = student_info[1].replace(" ", "")
        semester = student_info[2].replace(" 0", "")
        semester = semester.replace(" ", "")
        homework_avg = student_info[3].replace(" 0", "")
        homework_avg = homework_avg.replace(" ", "")
        homework_avg = homework_avg.replace("\n", "")

        if isInfoValid(id, name, semester, homework_avg):
                       final_grade = calculateFinalGrade(id, homework_avg)  
                       info_tuple = (id, homework_avg, str(final_grade))
                       student_grades[id] = ", ".join(info_tuple)

    sorted_student_grades = sorted(student_grades.items())
    for id_key, info in sorted_student_grades:
        tmp_info = info.split(',')
        sum_of_final_grades += int(tmp_info[2])
        write_file.write(info + "\n")
    write_file.close()
    read_file.close()
    if sum_of_final_grades == 0:
        return 0
    return floor(sum_of_final_grades / len(student_grades))


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    remained_s2 = s2.lower()
    for s1_letter in s1.lower():
        if len(remained_s2) == 0:
            return False
        for i, s2_letter in enumerate(remained_s2):
            if s1_letter == s2_letter:
                remained_s2 = remained_s2[:i] + remained_s2[i+1:]
                break 
            elif i == len(remained_s2) - 1:
                return False
    return True 
