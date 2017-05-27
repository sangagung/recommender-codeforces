import ast

data_location = '../Data/'

input_file_name = 'userdata.txt'
input_file = open(data_location + input_file_name, 'r')

problem_pool_file_name = 'problems_indonesia.txt'
problem_pool_file = open(data_location + problem_pool_file_name,'w')

user_problem_file_name = 'user_problems_indonesia.txt'
user_problem_file = open(data_location + user_problem_file_name,'w')

problem_pool = set()

for line in input_file:
    line = line[:-1] #omit newline at end-of-line
    userdata = ast.literal_eval(line)
    solved = set()
    attempted_not_solved = set()
    for sub in userdata['submissions']:
        problem_code = str(sub['contest_id']) + sub['problem_index']
        if (sub['verdict'] == 'OK'):
            solved.add(problem_code)
        else:
            attempted_not_solved.add(problem_code)
        problem_pool.add(problem_code)
    attempted_not_solved = attempted_not_solved - solved
    data = {'handle':userdata['handle']}
    if (solved):
        data['solved'] = solved
    if (attempted_not_solved):
        data['attempted_not_solved'] = attempted_not_solved
    user_problem_file.write(str(data))
    user_problem_file.write('\n')
problem_pool_file.write(str(problem_pool))