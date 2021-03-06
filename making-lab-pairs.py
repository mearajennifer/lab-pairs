""" A quick script connected to a db to make lab pairs. """

# create db with corresponding class for Students
# table consists of ID, name, pair_list
# 
import random
# pull a dictionary of items {(id, 'name', set(pair_list)), ... }
students = {1: ('Marjana', set([2, 3, 4, 5])),
            2: ('Andra', set([1, 5, 3])),
            3: ('Joy', set([4, 1, 5, 2])),
            4: ('Sameea', set([3, 1])),
            5: ('Emily', set([6, 2, 3, 1])),
            6: ('Christina', set([5, 7, 8, 10])),
            7: ('Nicole', set([8, 6, 10, 19])),
            8: ('QueenTesa', set([7, 9, 6, 22])),
            9: ('Celeste', set([10, 8, 13, 12])),
            10: ('Kelsey', set([9, 22, 7, 6])),
            11: ('Gabriella', set([12, 13, 16, 17])),
            12: ('Melissa', set([11, 16, 22, 9])),
            13: ('Kellie', set([14, 11, 9, 16])),
            14: ('Rosemond', set([13, 23, 20, 21])),
            15: ('Susmitha', set([16, 17, 23, 18])),
            16: ('Quanisha', set([15, 12, 11, 13])),
            17: ('Sarah', set([18, 15, 19, 11])),
            18: ('Deepti', set([17, 19, 21, 15])),
            19: ('Yuliana', set([20, 18, 17, 7])),
            20: ('Jessica', set([19, 21, 14, 23])),
            21: ('Noelle', set([22, 20, 18, 14])),
            22: ('Sherry', set([21, 10, 12, 8])),
            23: ('Kioshi', set([14, 15, 20]))
            }

# make a variable with an empty list for todays pairs
todays_pairs = []

# first loop
# randomly choose one student from dictionary, remove it from the dictionary, and save as variable
# randomly choose a partner student from dictionary
# if partner ID is in student's pair set, choose a different one
# once you have a partner whose ID isn't in the pair set, remove student from dictionary and save as variable
# add student and partner names to today's pairs (nested lists? or nested tuples?)
# repeat until there are no more dictionary items
# add final name.

# second loop
# loop through pairs and print assignment to labs Malala a - g and ruth a - g

# voila
