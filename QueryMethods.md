# Query Methods
Here are some useful query methods to get to know.
## Select records

#### all()

`MyModel.query.all()`

Fetches all records from table. Returns list of objects.
#### first()

`MyModel.query.first()`

Fetches just the first result. Returns object or None .

## Filtering 

#### filter_by
`MyModel.query.filter_by(attr='some value')`
Similar to SELECT * from ... WHERE

#### filter

Examples:

~~~
MyModel.query.filter(MyOtherModel.some_attr='some value')
OrderItem.query.filter(Product.id=3)
~~~~

Similar to `filter_by` , but instead, you specify attributes on a given Model.
equals: `query.filter(User.name == 'ed')` not equals: `query.filter(User.name != 'ed')`
          
LIKE: `query.filter(User.name.like('%ed%'))`

ILIKE (case-insensitive LIKE): `query.filter(User.name.ilike('%ed%'))`

IN: `query.filter(User.name.in_(['ed', 'wendy', 'jack']))`

NOT IN: `query.filter(~User.name.in_(['ed', 'wendy', 'jack']))`

IS NULL: `query.filter(User.name == None)`

IS NOT NULL: `query.filter(User.name != None)`

AND: `query.filter(User.name == 'ed', User.fullname == 'Ed Jones') or chain filter methods together.`

OR: `query.filter(User.name == 'a' | User.name == 'b')`

MATCH: `query.filter(User.name.match('wendy'))`

### Ordering 
#### order_by
~~~
MyModel.order_by(MyModel.created_at) 
MyModel.order_by(db.desc(MyModel.created_at))
~~~~

To order the results by a given attribute. Use db.desc to order in descending order. 

### limit
`Order.query.limit(100).all()`

`limit(max_num_rows)` limits the number of returned records from the query. ala LIMIT in SQL.

### Aggregates 

#### count()

Example:
~~~
query = Task.query.filter(completed=True) query.count()
Returns an integer set to the number of records that would have been returned by running the query.
~~~
#### get()

Get object by ID
~~~
model_id = 3 
MyModel.query.get(model_id)
~~~

Returns the object as a result of querying the model by its primary key.

#### Bulk Deletes

Example:
~~~
query = Task.query.filter_by(category='Archived') 
query.delete()
~~~
`delete()` does a bulk delete operation that deletes every record matching the given query.

#### Joined Queries
Example:
`Driver.query.join('vehicles')`
Query has a method join(<table_name>) for joining one model to another table.
