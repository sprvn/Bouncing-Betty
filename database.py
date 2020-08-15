import sqlite3
import os
import sys

import helpers
import logger

log = logger.getLogger(__name__)

def getDBConnection():
    db = sqlite3.connect(
	'instance/database.sqlite',
    	detect_types=sqlite3.PARSE_DECLTYPES
    )
    db.row_factory = sqlite3.Row

    return db

def initDB():

    helpers.createDirectory('instance')
    
    answer = input('Type YES to initialize the database: ')

    if answer != 'YES':
        log.warning('Aborting initialization')
        return False

    db = getDBConnection()

    with open(os.path.join(sys.path[0], 'schema.sql')) as f:
        db.executescript(f.read())

