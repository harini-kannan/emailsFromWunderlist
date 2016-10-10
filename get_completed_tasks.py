from __future__ import print_function
import urllib
import urllib2
import json
import datetime

def get_date():
    now = datetime.datetime.now()
    day = now.day
    month = now.month

    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)

    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)

    date = str(now.year) + "-" + month + "-" + day
    return date

credentials_file = '/Users/harini/Dropbox/Code/emailWunderlist/email.txt'
credentials = open(credentials_file).readlines()

access_token = credentials[4].strip()
client_id = credentials[2].strip()

task_endpoint = 'https://a.wunderlist.com/api/v1/tasks?' 
list_endpoint = 'https://a.wunderlist.com/api/v1/lists?'
list_params = urllib.urlencode({'access_token':access_token, 'client_id':client_id})
list_resp = urllib2.urlopen(list_endpoint+list_params).read()
all_lists = json.loads(list_resp)

output_file = open('/Users/harini/Dropbox/Code/emailWunderlist/example.txt', 'w')

print("<html><head></head><body>", file=output_file)
print("Hi Harini,<br>", file=output_file)
print("Here are all the tasks you did today. Great work! :)<br>", file=output_file)

for task_list in all_lists:
    list_id = task_list['id']

    task_params = urllib.urlencode({'access_token':access_token, 'client_id':client_id, 'list_id':list_id, 'completed':'true'})
    task_resp = urllib2.urlopen(task_endpoint+task_params).read()
    completed_tasks = json.loads(task_resp)

    date = get_date()

    todays_tasks = []
    for task in completed_tasks:
        if date == task['completed_at'][0:10]:
            todays_tasks.append(task['title'])

    if len(todays_tasks) > 0:
        print("<p><b>", file=output_file)
        print(task_list['title'], file=output_file)
        print("</b>", file=output_file)
        print("<br>", file=output_file)
        index = 1
        for task in todays_tasks:
            print(str(index) + ".", file=output_file)
            print(task, file=output_file)
            print("<br>", file=output_file)
            index = index + 1
        print("\n", file=output_file)

print("</body></html>", file=output_file)
