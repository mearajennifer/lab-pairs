""" A quick script connected to a .txt file to make lab pairs. """

import random

def create_students(student_file):
    """
    open file, add student info into a dictionary
    """
    
    students = {}
    
    with open(student_file) as s_file:
        for line in s_file:
            line = line.rstrip()
            student_info = line.split()
            student_name = student_info[0]
            student_pairs = [name for name in student_info[1:]]
            students[student_name] = student_pairs
            
    return(students)


def create_pairs(students):
    """ 
    take in dictionary of student information and create pairs without repeats from previous labs
    """

    todays_pairs = []
    student_count = len(students)
    students_new = {}

    # loop: while more than 1 item is in dict
    while len(students) > 1:
        
        # randomly choose first student in pair & update student info dict and num list        
        first_student = students.popitem()
        remaining_names = list(students.keys())
        
        # second student must not be the same as first, and must not be within first's previous pairs
        # randomly choose second student in pair & update student info dict and num list
        while True:
            name = random.choice(remaining_names)
            if name not in first_student[1]:
                break
        prev_pairs = students.pop(name)
        second_student = (name, prev_pairs)
        
        todays_pairs.append([first_student, second_student])
        students_new[first_student[0]] = first_student[1]
        students_new[second_student[0]] = second_student[1]


    # if odd number, add leftover name
    if students:
        last_student = students.popitem()
        todays_pairs.append([last_student])
        students_new[last_student[0]] = last_student[1]

    
    # return pair list
    return(todays_pairs, students_new)


def print_lab_assignments(todays_pairs):
    """ 
    loop through pairs and print assignment to labs Malala a - g and ruth a - g
    """
    rooms = ['A', 'B', 'C', 'D', 'E', 'F']
        
    print('Malala:')
    for i in range(len(rooms)):
        room = rooms[i]
        room_pair = todays_pairs[i]
        if len(room_pair) == 2:
                print(room, room_pair[0][0], room_pair[1][0])
        else:
            print(room, room_pair[0][0])
    
    print('Ruth:')
    for i in range(len(rooms)):
        room = rooms[i]
        room_pair = todays_pairs[i+5]
        if len(room_pair) == 2:
                print(room, room_pair[0][0], room_pair[1][0])
        else:
            print(room, room_pair[0][0])


def update_student_file(students_new, todays_pairs, student_file):
    """
    rewrite student_file.txt with updated pair information
    """
        
    for pair in todays_pairs:
        if len(pair) > 1:
            first = pair[0][0]
            second = pair[1][0]
            students_new[first].append(second)
            students_new[second].append(first)

    with open(student_file, "w") as f:
        for key, value in students_new.items():
            updated_student = key
            for item in value:
                updated_student = updated_student + ' ' + item
            updated_student = updated_student + '\n'
            f.write(updated_student)
            




student_file = "student_file.txt"
print()

students = create_students(student_file)
print('**** STUDENT DICTIONARY SUCCESS!!!! ****')
print()

todays_pairs, students_new = create_pairs(students)
print('**** STUDENT PAIRS SUCCESS!!!! ****')
print()

update_student_file(students_new, todays_pairs, student_file)
print('**** STUDENT FILE UPDATED!!!! ****')

# print_lab_assignments(todays_pairs)
print()



