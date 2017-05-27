import numpy
import os.path

# Data files location
data_location = '../Data/'

# Data files name
user_problem_filename = 'user-problem.csv'
user_problem_sample_filename = 'user-problem-sample.csv'

# Data files path
user_problem_filepath = data_location + user_problem_filename
user_problem_sample_filepath = data_location + user_problem_sample_filename

# Data files
user_problem_file = open(user_problem_filepath,'r')
user_problem_sample_file = open(user_problem_sample_filepath,'w')

sample = []
for user_line in user_problem_file:
	line_split = user_line.split(',')
	handle = line_split[0]
	features = line_split[1:]
	# If still on header, sample the problems
	if (handle == 'handle'):
		n_problem = len(features)
		step = 10
		for i in range(0, n_problem, step):
			sample_index = numpy.random.random_integers(i,min(i+step-1,n_problem-1))
			sample.append(sample_index)
	user_problem_sample_file.write(handle)
	for i in sample:
		user_problem_sample_file.write(',' + features[i])
	user_problem_sample_file.write('\n')