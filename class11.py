import mysql.connector

my_database = mysql.connector.connect(
    host = 'localhost', 
    user = 'root',
    passwd = '',
    database = 'studentprofile',
    
)
action = my_database.cursor()

# To create a table, call the action

# action.execute('CREATE TABLE studentprofile (firstname VARCHAR(50), lastname VARCHAR(50), phonenumber VARCHAR(50), friends VARCHAR(3000), age INT')

action.execute('SHOW TABLES')
for table in action:
    print(table)

action.execute('SELECT * FROM profile')
allProfiles = action.fetchall()

for profile in allProfiles:
    print(profile)

    '''
    create a new database call note_DB, connect the database 
    use the command on w3 mysql to create notes which should have title and body
    should be like dictionary name =
    atleast five notes
    '''
