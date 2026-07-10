import sqlite3
import pandas as pd

conn = sqlite3.connect('pets_database.db')
cursor = conn.cursor()


cats_data = pd.read_sql("SELECT * FROM cats;", conn)
# print(cats_data)


age_5 = pd.read_sql("""
    SELECT * FROM cats WHERE age >= 5;
""", conn)
# print(age_5)

use_btw = pd.read_sql("""
    SELECT * FROM cats WHERE age BETWEEN 1 AND 3; 
""", conn)
# print(use_btw)


null_owner = pd.read_sql("""
    SELECT * FROM cats WHERE owner_id IS NULL;
""", conn)
# print(null_owner)


initial_keyword = pd.read_sql("""
    SELECT * FROM cats WHERE name LIKE 'M%';
""", conn)
# print(initial_keyword)


middle_keyword = pd.read_sql("""
    SELECT * FROM cats WHERE name LIKE '_a__';
""", conn)
# print(middle_keyword)


owner_count = pd.read_sql("""
    SELECT COUNT(owner_id) AS owner_count FROM cats WHERE owner_id = 1;
""", conn)
print(owner_count)

conn.close()