from database import get_connection as connection

def delete(connection, id):
  query = '''DELETE FROM Pessoa WHERE id=?'''
  cursor = connection.cursor()
  cursor.execute(query, (id,))

  connection.commit()