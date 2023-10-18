from database import get_connection as connection

def find_by_id(connection, id):
  query = '''SELECT * FROM Pessoa WHERE id = ?'''
  
  cursor = connection.cursor()
  cursor.execute(query, (id))

  return cursor.fetchone()
