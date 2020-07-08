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

# BEST METHOD -->
#VAR for reusable sql with dict:
SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(bool)s);'
#Use loop to create 30 rows with reusable SQL statemtn
for i in range(20, 50):
    cursor.execute(SQL, {
        'id':i,
        'bool':(i%2==0)
    })

connection.commit()
#close connections, necessary
connection.close()
cursor.close()

#USING PSQL -> Table looks like this with Query : SELECT id, completed FROM table2 WHERE completed='f' order by id;
'''id | completed 
----+-----------
  2 | f
  3 | f
 21 | f
 23 | f
 25 | f
 27 | f
 29 | f
 31 | f
 33 | f
 35 | f
 37 | f
 39 | f
 41 | f
 43 | f
 45 | f
 47 | f
 49 | f
(17 rows)'''
