""" A quick script connected to a .txt file to make lab pairs. """

import random

def create_students(student_file):
    """
    open file, add student info into a dictionary
    """
    
    students = {}
    s_file = open(student_file)
    
    for line in s_file:
        line = line.rstrip()
        student_info = line.split()
        student_num = int(student_info[0])
        student_name = str(student_info[1])
        student_pairs = set([int(num) for num in student_info[2:]])
        students[student_num] = (student_name, student_pairs)
        
    s_file.close()
        
    return(students)


def create_pairs(students):
    """ 
    take in dictionary of student information and create pairs without repeats from previous labs
    """

    todays_pairs = []
    student_count = len(students)

    # loop: while more than 1 item is in dict
    while len(students) > 1:
        
        # randomly choose first student in pair & update student info dict and num list
        first_num = 0
        while True:
            first_num = random.randint(1, student_count + 1)
            if first_num not in set(students.keys()):
                continue
            else:
                break    
        first_student = students.pop(first_num)
        
        # second student must not be the same as first, and must not be within first's previous pairs
        # randomly choose second student in pair & update student info dict and num list
        second_num = 0
        while True:
            second_num = random.randint(1, student_count + 1)
            if second_num not in set(students.keys()):
                continue
            if (second_num == first_num) or (second_num in first_student[1]):
                continue
            else:
                break
        second_student = students.pop(second_num)
        
        # add student and partner names to today's pairs (nested lists? or nested tuples?)
        todays_pairs.append([first_student[0], second_student[0]])

    # if odd number, add leftover name
    if students:
        last_num = list(students.keys())[0]
        last_student = students.pop(last_num)
        todays_pairs.append([last_student[0]])
    
    # return pair list
    return(todays_pairs)


student_file = "student_file.txt"

students = create_students(student_file)
print('**** STUDENT DICTIONARY SUCCESS!!!! ****')
print()

todays_pairs = create_pairs(students)
print('**** STUDENT PAIRS SUCCESS!!!! ****')



# loop through pairs and print assignment to labs Malala a - g and ruth a - g
# for pair in todays_pairs:
#     print(pair)


