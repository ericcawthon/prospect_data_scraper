import mysql.connector
from dbconfig import config

connection = mysql.connector.connect(**config)
cursor = connection.cursor(dictionary=True)

select_query = """SELECT id, future_grades FROM prospects"""
cursor.execute(select_query)
results = cursor.fetchall()

insert_list = []
for row in results:
    grades = row['future_grades'].split("-")
    for g in grades:
        gtuple = (row['id'], g[0:2], g[2:])
        insert_list.append(gtuple)

insert_query = """INSERT INTO prospects_future_grades (prospect_id, grade, label) VALUES (%s, %s, %s) """
cursor.executemany(insert_query, insert_list)
connection.commit()
connection.close()