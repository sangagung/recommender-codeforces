import urllib.request
import json
import sys

data_location = '../Data/'

base_url = 'http://codeforces.com/api/'

method = 'user.status'

userlist_filename = 'username-list.txt'


# Read from file
username_list = []
userlist_file = open(data_location + userlist_filename, 'r')
for username in userlist_file:
    username_list.append(username[:-1])

start_index = int(sys.argv[1])-1
end_index = min(int(sys.argv[2]),len(username_list))
userdata_filename = 'userdata_'+str(start_index+1)+'-'+str(end_index)+'.txt'
userdata_file = open(data_location + userdata_filename,'w', 1)

# Query every user
# for i in range(start_index,min(end_index,len(username_list))):
i = start_index
while i < min(end_index,len(username_list)):
    try:
        username = username_list[i]
        url = base_url + method + '?handle=' + username

        print('Retrieving user data ' + str(i) + ': ' + username)

        response = urllib.request.urlopen(url).read()
        response = str(response,'utf-8')
        user_status = json.loads(response)
        
        submissions = user_status['result']
        user_submissions = []
        for sub in submissions:
            user_submissions.append({ 'contest_id':sub['problem']['contestId'], 'problem_index':sub['problem']['index'], 'verdict':sub['verdict'] })
        
        data = {'handle':username, 'submissions':user_submissions}
        userdata_file.write(str(data))
        userdata_file.write('\n')
        i = i + 1
    except:
        print('Error occured while retrieving user ' + username_list[i] + '. Reattempting')