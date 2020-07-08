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

#SELECT ITEMS:
cursor.execute("SELECT * FROM table2 WHERE completed='f' order by id;")
#Prints as a list of tuples : ex [(1, True), (2, False), (7, False)]
res = cursor.fetchall()
print(res)
#THIS WORKS, but when you fetchall, fetch will not work again (as there are no statement to fetch).  You then need to execute a
#new select statement to fetch more results


#close connections, necessary
connection.close()
cursor.close()
