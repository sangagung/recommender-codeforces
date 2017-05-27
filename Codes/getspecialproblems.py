import json

data_location = '../Data/'

special_problems_file_name = 'problems_special.txt'
special_problems_file = open(data_location + special_problems_file_name,'w')
problems_file_name = 'problems.txt'
problems_file = open(data_location + problems_file_name,'r')
problems_json = problems_file.readline()
problems_data =  json.loads(problems_json)['result']

problems_list = problems_data['problems']

special_problems = set()
for problem in problems_list:
    for tag in problem['tags']:
        if (tag['name'] == '*special'):
            special_problems.add(str(problem['contestId']) + problem['index'])
            continue
special_problems_file.write(str(special_problems))