import ast
import json

data_location = '../Data/'
problems_data_file_name = 'problems.txt'
problems_indonesia_nonspecial_file_name = 'problems_indonesia_nonspecial.txt'
problems_difficulty_file_name = 'problem-difficulty.csv'
problems_data_file = open(data_location + problems_data_file_name,'r')
problems_indonesia_nonspecial_file = open(data_location + problems_indonesia_nonspecial_file_name,'r')
problems_difficulty_file = open(data_location + problems_difficulty_file_name,'w')

problem_statistics = json.loads(problems_data_file.readline())['result']['problemStatistics']
problems_indonesia_nonspecial = ast.literal_eval(problems_indonesia_nonspecial_file.readline())

problems_difficulty = []
for problem in problem_statistics:
    problem_name = str(problem['contestId']) + problem['index']
    if problem_name in problems_indonesia_nonspecial:
        problems_difficulty.append((problem_name,problem['solvedCount']))
problems_difficulty = sorted(problems_difficulty, key=lambda x:x[1],reverse=True)

problems_difficulty_file.write('problem_code,solved_count\n')
for (problem_code,solved_count) in problems_difficulty:
    problems_difficulty_file.write(problem_code + ',' + str(solved_count) + '\n')