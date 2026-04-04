from connect import get_connection

conn = get_connection()
cur = conn.cursor()


cur.execute("SELECT * FROM search_pattern(%s)", ('a',))
print(cur.fetchall())


cur.execute("CALL upsert_contact(%s, %s)", ('Alex', '8700'))


cur.execute("CALL delete_contact(%s)", ('Alex',))

conn.commit()
cur.close()
conn.close()