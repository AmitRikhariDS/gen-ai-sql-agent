import sqlite3

connection= sqlite3.connect("student.db")

cursor= connection.cursor()
table_info="""

create table STUDENT(
NAME VARCHAR(25),
CLASS VARCHAR(25),
SECTION VARCHAR(25),
MARKS INT
)

"""
cursor.execute(table_info)

##insert records

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'DS', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Amit', 'AI', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Neha', 'CS', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ravi', 'DS', 'C', 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Anita', 'IT', 'B', 80)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Manish', 'AI', 'A', 76)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Pooja', 'CS', 'C', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikram', 'IT', 'B', 89)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Sneha', 'DS', 'A', 91)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Arjun', 'AI', 'C', 84)''')

# Display the records
print("Inserted records are")
data=cursor.execute('''select * from STUDENT''')
for row in data:
    print(row )

# Commit changes
connection.commit()
connection.close()