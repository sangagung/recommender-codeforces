import urllib.request
import json

handle = 'ZakyKh26'

response = urllib.request.urlopen("http://codeforces.com/api/problemset.problems").read()
response = str(response,'ascii',errors='ignore')

# print(response)
# print(response[0])
# print(response[len(response)-1])

print(response)

# response = json.loads(response)
# problems = response['result']['problems']
# problems_count = len(problems)
# print('Problem count: ' + str(problems_count))
# special_problems_count = 0
# for i in range(0,problems_count):
    # problem_tags = problems[i]['tags']
    # for j in range(0,len(problem_tags)):
        # if problems[i]['tags'][j]['name'] == '*special':
            # special_problems_count += 1
            # break
# print('Special problems count: ' + str(special_problems_count))

# problems_stats = response['result']['problemStatistics']

# problems_stats_sorted = sorted(problems_stats, key=lambda x: x['solvedCount'], reverse=True)
# solved_stats = [x['solvedCount'] for x in problems_stats_sorted]
# print(solved_stats)
