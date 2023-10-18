from database import get_connection as connection

def update(connection, id, data):
  sql = '''UPDATE Pessoa SET name = ?, date = ? WHERE id = ?'''

  cursor = connection.cursor()
  cursor.execute(sql, (data.name, data.birth_date, id))
  connection.commit()

