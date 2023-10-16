import requests
from bs4 import BeautifulSoup

URL = 'https://rotoprospects.com/rotoprospects-top-500-rankings/'
insert_list = []

response = requests.get(URL)
prospectdata = response.text.split("<tbody>")[1]
prospects = prospectdata.split("<tr>")
prospects = prospects[2:502]

i = 1
for p in prospects:
    # p = list(filter(None, p))
    plist = filter(None, BeautifulSoup(p, "html.parser").get_text().splitlines())
    ptuple = tuple(plist)
    if i == 500: #the last record has some extra content form the page footer, clean it out
        ptuple = ptuple[0:10]
    insert_list.append(ptuple)
    i = i + 1

import mysql.connector
from dbconfig import config

connection = mysql.connector.connect(**config)
cursor = connection.cursor(dictionary=True)

insert_query = """INSERT INTO prospects (rank, name, pos, team, bat_throw, future_grades, level, age, eta, last) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
cursor.executemany(insert_query, insert_list)
connection.commit()
connection.close()