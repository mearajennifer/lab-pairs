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
        student_name = student_info[0]
        student_pairs = set([name for name in student_info[1:]])
        students[student_name] = student_pairs
        
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

    # if odd number, add leftover name
    if students:
        last_student = students.popitem()
        todays_pairs.append([last_student])
    
    # return pair list
    return(todays_pairs)


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




student_file = "student_file.txt"
print()

students = create_students(student_file)
print('**** STUDENT DICTIONARY SUCCESS!!!! ****')
print()

todays_pairs = create_pairs(students)
print('**** STUDENT PAIRS SUCCESS!!!! ****')
print()

print_lab_assignments(todays_pairs)
print()



