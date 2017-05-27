import ast
import json

data_location = '../Data/'
problems_data_file_name = 'problems.txt'
problems_indonesia_nonspecial_file_name = 'problems_indonesia_nonspecial.txt'
problems_difficulty_file_name = 'problem-difficulty.csv'
problems_data_file = open(data_location + problems_data_file_name,'r')
problems_indonesia_nonspecial_file = open(data_location + problems_indonesia_nonspecial_file_name,'r')
problems_difficulty_file = open(data_location + problems_difficulty_file_name,'w')

problem_data = json.loads(problems_data_file.readline())['result']
problem_list = problem_data['problems']
problem_statistics = problem_data['problemStatistics']
problems_indonesia_nonspecial = ast.literal_eval(problems_indonesia_nonspecial_file.readline())

problem_names = {}
for problem in problem_list:
    problem_code = str(problem['contestId']) + problem['index']
    problem_name = problem['name']
    problem_names[problem_code] = problem_name

problems_difficulty = []
for problem in problem_statistics:
    problem_code = str(problem['contestId']) + problem['index']
    if problem_code in problems_indonesia_nonspecial:
        problems_difficulty.append((problem_code,problem_names[problem_code],problem['solvedCount']))
problems_difficulty = sorted(problems_difficulty, key=lambda x:x[2],reverse=True)

problems_difficulty_file.write('problem_code;problem_name;solved_count\n')
for (problem_code,problem_name,solved_count) in problems_difficulty:
    problems_difficulty_file.write(problem_code + ';' + problem_name + ';' + str(solved_count) + '\n')