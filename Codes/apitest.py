import urllib.request
import json

handle = 'ZakyKh26'

response = urllib.request.urlopen("http://codeforces.com/api/user.status?handle=" + handle).read()
response = str(response,'utf-8')

# print(response)
# print(response[0])
# print(response[len(response)-1])

print('Handle: ' + handle)
user_status = json.loads(response)
submissions = user_status['result']
submission_count = len(submissions)
print('Submissions count: ' + str(submission_count))
print('Submission verdicts:')
for i in range(0,submission_count):
    problem = submissions[i]['problem']
    contest_id = problem['contestId']
    problem_index = problem['index']
    problem_name = problem['name']
    verdict = submissions[i]['verdict']
    print('> ' + str(contest_id) + problem_index + ' (' + problem_name + ') ' + '[' + verdict + ']')