import psycopg2
connection = psycopg2.connect("dbname=example")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY, 
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('''
    INSERT INTO table2 VALUES (1, True);
''')
connection.commit()
connection.close()
cursor.close()