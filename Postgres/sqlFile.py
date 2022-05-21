import psycopg2


def create():
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER) ")
    conn.commit()
    conn.close()

# create()


def insert(first_name, last_name, age):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (first_name,last_name,age) values(%s,%s,%s)",
                (first_name, last_name, age))
    conn.commit()
    conn.close()


# insert('Rahul', 'Yadav', 50)
# insert('Karan', 'Verma', 35)
# insert('Eliza', 'Jess', 25)

def view():
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    conn.close()
    return rows

# print(view())

def delete(id):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id= %s", (id,))
    conn.commit()
    conn.close()

# delete(4)
# print(view())

def update(firstname, age):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE users SET age=%s WHERE first_name LIKE %s", (age, firstname))
    conn.commit()
    conn.close()

# update('Karan', 34)
# print(view())

