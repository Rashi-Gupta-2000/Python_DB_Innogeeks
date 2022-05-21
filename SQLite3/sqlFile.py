import sqlite3

def create():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE if not exists store(item TEXT,quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

# create()
# insert('Pencils', 10, 10)
# insert('Pens', 10, 20)

# order by
# update
# and or


def view():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM store")
    # cur.execute("SELECT rowid,* FROM store ORDER BY item DESC")
    # cur.execute("SELECT rowid,* FROM store where item = 'Books' Or rowid = 1")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE rowid=?", (item,)) # mind the ',' after item
    conn.commit()
    conn.close()


def update(item, rowid):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    # cur.execute("UPDATE store set quantity=?, price=? WHERE rowid=?", (quantity, price, rowid))
    cur.execute("UPDATE store SET item=? where rowid=?", (item, rowid))
    conn.commit()
    conn.close()


# delete()
# update('Books', 3)

def dropTable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE store")
    conn.commit()
    conn.close()

data = view()
for d in data:
    print(d)


# connection created
# conn = sqlite3.connect('lite.db')
# # cursor created
# cur = conn.cursor()
# cur.execute("CREATE TABLE if not exists store(item TEXT,quantity INTEGER, price REAL)")
# cur.execute("INSERT INTO store VALUES('books',10, 100.70)")
# # changes made here will be submitted to the database by
# conn.commit()
# # close the connection
# conn.close()
