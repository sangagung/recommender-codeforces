from bs4 import BeautifulSoup
import requests

data_location = '../Data/'

base_url = 'http://codeforces.com/profile/'

user_list_file_name = 'username-list.txt'
user_list_file = open(data_location + user_list_file_name,'r')

username_list = []
for line in user_list_file:
    username_list.append(line[:-1])

user_rating_file_name = 'user-rating.csv'
user_rating_file = open(data_location + user_rating_file_name, 'w')

user_rating_file.write('handle;current_rating;max_rating\n')

i = 0
while i < len(username_list):
    try:
        handle = username_list[i]
        print('Retrieving rating of user: ' + handle)
        url = base_url + handle
        page = requests.get(url)
        
        page_content = BeautifulSoup(page.content,'html.parser')
        rating_div = page_content.select('.info ul li')[0]
        rating_spans = rating_div.find_all('span',recursive=False)
        max_rating_spans = rating_spans[1].find_all('span',recursive=False)
        
        current_rating = rating_spans[0].string
        max_rating = max_rating_spans[1].string
        
        user_rating_file.write(handle + ';' + current_rating + ';' + max_rating + '\n')
        user_rating_file.flush()
        i = i + 1
    except:
        print('Error occured while retrieving user ' + username_list[i] + '. Reattempting')