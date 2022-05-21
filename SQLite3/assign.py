import sqlite3


def create():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE if not exists customer(firstname TEXT, lastname TEXT, age INTEGER, gender TEXT)")
    conn.commit()
    conn.close()

# create()


def insert(firstname, lastname, age, gender):
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO customer VALUES(?,?,?,?)",
                (firstname, lastname, age, gender))
    conn.commit()
    conn.close()

# insert('Akshay','Kumar', 20, 'M')
# insert('Rahul','Goyal', 21, 'M')
# insert('Raveena','Rathore', 30, 'F')
# insert('Riya','Gupta', 25, 'F')
# insert('Abc','Kumar', 18, 'M')


def view1():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer WHERE firstname LIKE 'A%'")
    rows = cur.fetchall()
    conn.close()
    return rows

# data1 = view1()
# for d in data1:
#     print(d)


def view2():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer WHERE age>50")
    rows = cur.fetchall()
    conn.close()
    return rows


# data2 = view2()
# for d in data2:
#     print(d)


def view3():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customer")
    rows = cur.fetchall()
    conn.close()
    return rows

# data2 = view3()
# for d in data2:
#     print(d)


def view4():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("SELECT rowid,* FROM customer where rowid=4")
    rows = cur.fetchall()
    conn.close()
    return rows

# data2 = view4()
# for d in data2:
#     print(d)


def update(lastname, rowid):
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("UPDATE customer SET lastname=? WHERE rowid=?",
                (lastname, rowid))
    conn.commit()
    conn.close()

# update('Xyz',5)

# data2 = view3()
# for d in data2:
#     print(d)


def delete(lastname):
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM customer where lastname=?", (lastname,))
    conn.commit()
    conn.close()

# delete('jess')
# data2 = view3()
# for d in data2:
#     print(d)


def update2():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("UPDATE customer SET gender='Others'")
    conn.commit()
    conn.close()

# update2()
# data2 = view3()
# for d in data2:
#     print(d)


def update3():
    conn = sqlite3.connect('assign.db')
    cur = conn.cursor()
    cur.execute("UPDATE customer SET gender='F' where age<20")
    conn.commit()
    conn.close()


# update3()
# data2 = view3()
# for d in data2:
#     print(d)
