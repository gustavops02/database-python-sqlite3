from services import create_table, delete, find_all, insert, read_by_id, update
from database import get_connection as connection
from entities.Pessoa import Pessoa

try:
  conn = connection.create_connection('meu_banco.db')

  create_table.create(conn)

  pessoa1 = Pessoa(None,'Gustavo', '2002-12-25')
  pessoa2 = Pessoa(None,'Guilherme', '2002-12-25')

  insert.insert(conn, (pessoa1.name, pessoa1.birth_date))
  insert.insert(conn, (pessoa2.name, pessoa2.birth_date))

  data = find_all.findall(conn)
  print(data)

  delete.delete(conn, 2)

  newData = Pessoa(None, "Roberto", "1995-02-02")
  update.update(conn, 1, newData)

except conn.DatabaseError as err:
  print("Database error: ", err)

finally:
  conn.close()