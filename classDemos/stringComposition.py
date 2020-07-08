#python3
import psycopg2
connection = psycopg2.connect("dbname=example")
cursor = connection.cursor()


cursor.execute('DROP TABLE IF EXISTS table2')
cursor.execute('''
    CREATE TABLE table2(
        id INTEGER PRIMARY KEY, 
        completed BOOLEAN NOT NULL DEFAULT False
    );
''')
#use specified values, less reusable statement.
cursor.execute('INSERT INTO table2 VALUES (3, False);')

#Tuple string composition
cursor.execute('INSERT INTO table2 VALUES (%s, %s);', (1, True))

#use dictionary to insert data, more reusable statement!
myData = {
    'id': 2,
    'bool': False
}
cursor.execute('INSERT INTO table2 VALUES (%(id)s, %(bool)s);', myData)

#create dictionary on the spot
cursor.execute('INSERT INTO table2 VALUES (%(id)s, %(bool)s);', {
    'id':15,
    'bool':True
})
#commit to DB
connection.commit()

#close connections, necessary
connection.close()
cursor.close()