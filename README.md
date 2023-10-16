## About the Code
Python scripts for scrapping prospect ranking and grades from rotoprospects.com and normalizing the prospects and their grades into separate tables for querying purposes.

## Python libraries needed:
bs4, requests, mysql.connector

## Usage
1. Create tables in a MySQL database using create_tables.sql
2. Install the required libraries listed above
3. Create your own dbconfig.py from the provided dbconfig_template.py file, providing information for connecting to your MySQL database
4. Run scrape_prospect_data_mysql.py to scrape the rotoprospects site
5. Run normalize_grades_mysql.py to break the future_grades values into a normalized list were each grade gets it's own record
6. Enjoy querying the data