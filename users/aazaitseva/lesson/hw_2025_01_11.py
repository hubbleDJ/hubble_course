import sqlite3

with sqlite3.connect('my_db.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        create table if not exists messages (
            id int,
            text string,
            user_id int
        )
    ''')

    cursor.execute('''
        delete from messages where id = 0
    ''')

    cursor.execute('''
        insert into messages (id, text, user_id)
        values(0, 'ПРИВЕТ!', 0)
    ''')


    id_message = cursor.execute('''select user_id from messages limit 1''').fetchall()[0][0]