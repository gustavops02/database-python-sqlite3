from database import get_connection as connection

def findall(connection):
  cursor = connection.cursor()
  cursor.execute('SELECT * FROM Pessoa')
  return cursor.fetchall()