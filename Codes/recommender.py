import math
import numpy

def get_score(verdict):
	if (verdict == 'S'):
		return 1
	elif (verdict == 'A'):
		return 0.5
	else:
		return 0

# Hardcoded binary search, easier than debugging binary search but still as efficient
def get_rating_index(rating):
	if (rating >= 1900):
		if (rating >= 2400):
			if (rating >= 2600):
				if (rating >= 2900):
					return 10
				else:
					return 9
			else:
				return 8
		else:
			if (rating >= 2200):
				if (rating >= 2300):
					return 7
				else:
					return 6
			else:
				return 5
	else:
		if (rating >= 1400):
			if (rating >= 1600):
				return 4
			else:
				return 3
		else:
			if (rating >= 1200):
				return 2
			else:
				return 1

data_location = '../Data/'

user_problem_filename = 'user-problem.csv'
user_rating_filename = 'user-rating.csv'

user_problem_filepath = data_location + user_problem_filename
user_rating_filepath = data_location + user_rating_filename

print('Reading data... (' + user_problem_filepath + ')')
user_problem_file = open(user_problem_filepath,'r')
print('Reading data... (' + user_rating_filepath + ')')
user_rating_file = open(user_rating_filepath,'r')

print('Processing data...')
print('Creating user-problem matrix...')
user_problem_matrix = []
user_list = []
problem_list = []
for user_line in user_problem_file:
	line_split = user_line.split(',')
	handle = line_split[0]
	if (handle == 'handle'):
		problem_list = line_split[1:]
	else:
		user_list.append(handle)
		scores = []
		for problem_verdict in line_split[1:]:
			scores.append(get_score(problem_verdict))
		user_problem_matrix.append(scores)
print('Creating user rating index list...')
user_rating_index = []
for user_line in user_rating_file:
	line_split = user_line.split(',')
	handle = line_split[0]
	if (handle != 'handle'):
		user_rating_index.append(get_rating_index(int(line_split[1])))


user_index = -1
while (user_index < 0):
	username = input('Input your username: ')
	try:
		user_index = user_list.index(username)
	except ValueError as e:
		print('Username not found!')
# Get number of users and problems
n_user = len(user_list)
n_problem = len(problem_list)
# Compute mean rating of user
user_rating_mean = 0
for problem_score in user_problem_matrix[user_index]:
	user_rating_mean += problem_score
user_rating_mean /= n_problem
# Compute correlation with all other (n-1) users
correlation_list = []
for i in range(0,n_user):
	if (i == user_index):
		continue
	# Get weight of user i from perspective of user a
	weight = abs(user_rating_index[i] - user_rating_index[user_index])
	# Compute mean rating of user i
	user_i_rating_mean = 0
	for problem_score in user_problem_matrix[i]:
		user_i_rating_mean += problem_score
	user_i_rating_mean /= n_problem
	# Calculate formula
	nominator = 0
	denominator_1 = 0
	denominator_2 = 0
	for j in range(0,n_problem):
		user_rating_diff = user_problem_matrix[user_index][j] - user_rating_mean
		user_i_rating_diff = user_problem_matrix[i][j] - user_i_rating_mean
		nominator += user_rating_diff * user_i_rating_diff
		denominator_1 += math.pow(user_rating_diff,2)
		denominator_2 += math.pow(user_i_rating_diff,2)
	corr = nominator / math.sqrt(denominator_1 * denominator_2)
	correlation_list.append((corr,i))
correlation_list = sorted(correlation_list, key = lambda x:x[0], reverse=True)
nearest = 20