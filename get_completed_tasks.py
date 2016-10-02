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

credentials_file = 'email.txt'
credentials = open(credentials_file).readlines()

access_token = credentials[4]
client_id = credentials[2]

task_endpoint = 'https://a.wunderlist.com/api/v1/tasks?' 
list_endpoint = 'https://a.wunderlist.com/api/v1/lists?'
list_params = urllib.urlencode({'access_token':access_token, 'client_id':client_id})
list_resp = urllib2.urlopen(list_endpoint+list_params).read()
all_lists = json.loads(list_resp)

output_file = open('example.txt', 'w')

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
        print(task_list['title'], file=output_file)
        for task in todays_tasks:
            print(task, file=output_file)
        print("\n", file=output_file)

