from database import get_connection as connection

def insert(connection, data):
  query = '''INSERT INTO Pessoa (name, date) VALUES (?, ?)'''
  
  cursor = connection.cursor()
  cursor.execute(query, data)
  connection.commit()