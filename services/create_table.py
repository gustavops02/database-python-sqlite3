from database import get_connection as connection

def create(connection):
  query = '''CREATE TABLE IF NOT EXISTS Pessoa (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100) NOT NULL, date DATE NOT NULL)'''
  cursor = connection.cursor()
  cursor.execute(query)
  connection.commit()
