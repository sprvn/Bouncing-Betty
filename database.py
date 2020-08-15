import sqlite3
import os
import sys

database_directory = 'instance'

if not os.path.exists(os.path.join(sys.path[0], database_directory)):
    os.makedirs(os.path.join(sys.path[0], database_directory))

def getDBConnection():
    db = sqlite3.connect(
	'instance/database.sqlite',
    	detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    return db

def initDB():
    
    answer = input('Type YES to initialize the database: ')

    if answer != 'YES':
        print('Aborting initialization.')
        return False

    db = getDBConnection()

    with open(os.path.join(sys.path[0], 'schema.sql')) as f:
        db.executescript(f.read())


#getDBConnection()
#initDB()
