import requests
from bs4 import BeautifulSoup
import csv


# This is a crawler for Jira Camel
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}
url = 'https://issues.apache.org/jira/browse/CAMEL-10597' 
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

detailsA = soup.find_all('div', {'class': 'wrap'})
for i in detailsA:
    try:
        attribution = i.find('strong', {'class': 'name'}).get_text().strip()
        answer=i.find('span', {'class': 'value'}).get_text().strip()
        print(attribution,end='')
        print(answer)
        
        # CSV save data
        with open('data.csv','a+',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([ attribution, answer])
            csvfile.close()
        '''
        csv_obj = open('data.csv', 'a', encoding="utf-8")
        csv.writer(csv_obj).writerow([ attribution, answer])
        csv_obj.close()
        '''
    except AttributeError as e:
        continue
print('---------')

detailsB = soup.find_all('li', {'class': 'people-details'})
for j in detailsB:           # Problem 1: this loop can not get information of the reporter Bob Paulin
    try:
        position = j.find('dt').get_text().strip()
        information=j.find('span', {'class': 'view-issue-field'}).get_text().strip()
        print(position,end='')
        print(information)
        
        # CSV save data
        with open('data.csv','a+',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([ position, information])
            csvfile.close()
        '''
        csv_obj = open('data.csv', 'a', encoding="utf-8")
        csv.writer(csv_obj).writerow([ position, information])
        csv_obj.close()
        '''
    except AttributeError as e:
        continue
print('---------')

detailsC = soup.find_all('dl', {'class': 'dates'})
for k in detailsC:
    try:
        time_type = k.find('dt').get_text().strip()
        time_value = k.find('time', {'class': 'livestamp'}).get_text().strip()
        print(time_type,end='')
        print(time_value)
        
        # CSV save data
        with open('data.csv','a+',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow([ time_type, time_value])
            csvfile.close()
        '''
        csv_obj = open('data.csv', 'a', encoding="utf-8")
        csv.writer(csv_obj).writerow([ time_type, time_value])
        csv_obj.close()
        '''
    except AttributeError as e:
        continue
print('---------')

detailsD = soup.find('div',{'class': 'user-content-block'})
description=detailsD.get_text()
print(description)
print('---------')
# CSV save data
with open('data.csv','a+',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([description])
    csvfile.close()
'''
csv_obj = open('data.csv', 'a', encoding="utf-8")
csv.writer(csv_obj).writerow([ description])
csv_obj.close()
'''
detailsE = soup.find_all('div', {'class': 'action-body flooded'})     # Problem 2: this function can not get anything. This is strange because other functions work well 
print(detailsE)

'''
for i in detailsE:
    try:
        comment=i.find('div', {'class': 'twixi-wrap verbose actionContainer'}).get_text().strip()
        print(comment)

    except AttributeError as e:
        continue
print('---------')
'''

'''
# CSV save data
csv_obj = open('data.csv', 'w', encoding="utf-8")
csv.writer(csv_obj).writerow([ attribution, answer, position, information, time_type, time_value, description])
csv_obj.close()
'''


