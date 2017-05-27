import json
import ast

data_location = '../Data/'
problem_indonesia_file_name = 'problems_indonesia.txt'
problem_special_file_name = 'problems_special.txt'
problem_indonesia_nonspecial_file_name = 'problems_indonesia_nonspecial.txt'

problem_indonesia_file = open(data_location + problem_indonesia_file_name,'r')
problem_special_file = open(data_location + problem_special_file_name,'r')
problem_indonesia_nonspecial_file = open(data_location + problem_indonesia_nonspecial_file_name,'w')

problem_indonesia = ast.literal_eval(problem_indonesia_file.readline())
problem_special = ast.literal_eval(problem_special_file.readline())

problem_indonesia_nonspecial = set()
for problem in problem_indonesia:
    if problem not in problem_special:
        problem_indonesia_nonspecial.add(problem)
problem_indonesia_nonspecial_file.write(str(problem_indonesia_nonspecial))