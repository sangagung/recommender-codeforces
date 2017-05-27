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
problem_difficulty_filename = 'problem-difficulty.csv'

user_problem_filepath = data_location + user_problem_filename
user_rating_filepath = data_location + user_rating_filename
problem_difficulty_filepath = data_location + problem_difficulty_filename


print('Reading data... (' + user_problem_filepath + ')')
user_problem_file = open(user_problem_filepath,'r')
print('Reading data... (' + user_rating_filepath + ')')
user_rating_file = open(user_rating_filepath,'r')
print('Reading data... (' + problem_difficulty_filepath + ')')
problem_difficulty_file = open(problem_difficulty_filepath,'r')

print('Processing data...')
user_list = []
print('Creating user list and user rating index list...')
user_rating_index = []
for user_line in user_rating_file:
	line_split = user_line.split(';')
	handle = line_split[0]
	if (handle != 'handle'):
		user_list.append(handle)
		user_rating_index.append(get_rating_index(int(line_split[1])))

print('Creating problem list...')
problems = {}
for problem_line in problem_difficulty_file:
	line_split = problem_line.split(';')
	problem_code = line_split[0]
	if (problem_code == 'problem_code'):
		continue
	else:
		problems[problem_code] = {'name':line_split[1],'solved_count':int(line_split[2])}

print('Welcome to Codeforces recommender system!')
user_index = -1
while (user_index < 0):
	username = input('Input your username: ')
	try:
		user_index = user_list.index(username)
	except ValueError as e:
		print('Username not found!')

print('Creating user-problem matrix...')
user_problem_matrix = []
problem_list = []
attempted_problem_set = set()
for user_line in user_problem_file:
	line_split = user_line.split(';')
	handle = line_split[0]
	if (handle == 'handle'):
		problem_list = line_split[1:]
	else:
		scores = []
		idx = 0
		for problem_verdict in line_split[1:]:
			if (handle == username and problem_verdict != '-'):
				attempted_problem_set.add(problem_list[idx])
			scores.append(get_score(problem_verdict))
			idx += 1
		user_problem_matrix.append(scores)

# Get number of users and problems
n_user = len(user_list)
n_problem = len(problem_list)

print('Computing mean score of all users...')
# Compute mean scores of every user
user_score_mean = []
for i in range(0,n_user):
	score_mean = 0
	for problem_score in user_problem_matrix[user_index]:
		score_mean += problem_score
	score_mean /= n_problem
	user_score_mean.append(score_mean)

print('Computing pearson correlation coefficients between user ' + username + ' and other users...')
# Compute correlation with all other (n-1) users
correlation_list = []
for i in range(0,n_user):
	if (i == user_index):
		continue
	# Get weight of user i from perspective of user a
	weight = 1 - 0.1*abs(user_rating_index[i] - user_rating_index[user_index])
	
	# Calculate formula
	nominator = 0
	denominator_1 = 0
	denominator_2 = 0
	for j in range(0,n_problem):
		user_score_diff = user_problem_matrix[user_index][j] - user_score_mean[user_index]
		user_i_score_diff = user_problem_matrix[i][j] - user_score_mean[i]
		nominator += user_score_diff * user_i_score_diff
		denominator_1 += math.pow(user_score_diff,2)
		denominator_2 += math.pow(user_i_score_diff,2)
	corr = nominator / math.sqrt(denominator_1 * denominator_2)
	
	# Make result to always fall within [0,1] without messing with data distribution
	corr = (corr + 1) / 2
	correlation_list.append((corr * weight,i))

# Sort by correlation value	
correlation_list = sorted(correlation_list, key = lambda x:x[0], reverse=True)

# Take top few to use for preferrence prediction
nearest = 10
neighbors = correlation_list[:nearest]

print('Calculating product preferrence scores...')
# Calculate product preferrence prediction values (Predicted problem verdict value)
predict_score = []
for i in range(0,n_problem):
	predict = user_score_mean[user_index]
	nominator = 0
	denominator = 0
	for (corr_w,j) in neighbors:
		nominator += (user_problem_matrix[j][i] - user_score_mean[j]) * corr_w
		denominator += corr_w
	predict_score.append((predict + nominator / denominator, i))
# Sort by prediction value
predict_score = sorted(predict_score, key = lambda x:x[0], reverse=True)

print('Filtering recommendations...')
predict_score = list(filter(lambda x: problem_list[x[1]] not in attempted_problem_set,predict_score))

# Take top few as recommended problems
n_top = 5
recommendations = list(map(lambda x:(problem_list[x[1]],x[0]), predict_score))[:n_top]

# Sort recommendations by difficulty
recommendations = sorted(recommendations, key=lambda x:problems[x[0]]['solved_count'], reverse=True)

base_url = 'http://codeforces.com/problemset/problem/'
print('Done! Recommended problems (sorted by difficulty, from easiest):')
for problem in recommendations:
	full_url = base_url + problem[0][:-1] + '/' + problem[0][-1]
	print(problem[0] + ' - ' + problems[problem[0]]['name'] + ' (' + full_url + ')')