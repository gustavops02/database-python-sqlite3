import sqlite3 as conector

def create_connection(database):
  connection = None
  try:
    connection = conector.connect(database)
    return connection
  
  except conector.DatabaseError as err:
    print( "database error: ", err)

  return connection