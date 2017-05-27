import ast

data_location = '../Data/'
problem_difficulty_file_name = 'problem-difficulty.csv'
user_problem_file_name = 'user_problems_indonesia.txt'
user_problem_matrix_file_name = 'user-problem.csv'

problem_difficulty_file = open(data_location + problem_difficulty_file_name,'r')
user_problem_file = open(data_location + user_problem_file_name,'r')
user_problem_matrix_file = open(data_location + user_problem_matrix_file_name,'w')

problem_code_list = []
for line in problem_difficulty_file:
    line = line[:-1]
    problem_code,problem_name,solved_count = line.split(';')
    if (problem_code == 'problem_code'):
        continue
    problem_code_list.append(problem_code)

user_problem_matrix_file.write('handle')
for problem_code in problem_code_list:
    user_problem_matrix_file.write(';' + problem_code)
user_problem_matrix_file.write('\n')

for line in user_problem_file:
    line = line[:-1]
    user_problem = ast.literal_eval(line)
    user_problem_matrix_file.write(user_problem['handle'])
    for problem_code in problem_code_list:
        user_problem_matrix_file.write(';')
        if ('solved' in user_problem) and (problem_code in user_problem['solved']):
            user_problem_matrix_file.write('S')
        elif ('attempted_not_solved' in user_problem) and (problem_code in user_problem['attempted_not_solved']):
            user_problem_matrix_file.write('A')
        else:
            user_problem_matrix_file.write('-')
    user_problem_matrix_file.write('\n')