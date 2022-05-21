import psycopg2


def create():
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS students(id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT,grade INTEGER, total_score INTEGER,gender TEXT, age INTEGER, result TEXT) ")
    conn.commit()
    conn.close()

# create()


def insert(first_name, last_name, grade, total_score, gender, age, result):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, grade, total_score, gender, age, result) values(%s,%s,%s,%s,%s,%s,%s)",
                (first_name, last_name, grade, total_score, gender, age, result))
    conn.commit()
    conn.close()


# insert('Ruhi', 'Jain', 2, 77, 'F', 9, 'Pass')
# insert('Jay', 'Chopra', 1, 40, 'M', 4, 'Hold')
# insert('Jay', 'Gandhi', 10, 80, 'M', 14, 'Pass')
# insert('Garvita', 'Jain', 5, 46, 'F', 10, 'Hold')
# insert('Alia', 'Arora', 8, 23, 'F', 12, 'Fail')
# insert('Tanmay', 'Bhatt', 2, 89, 'M', 5, 'Pass')


def view(choice, lastname):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    if choice == 1:
        cur.execute("SELECT * from students where grade = 8")
    elif choice == 2:
        cur.execute("SELECT * from students where last_name like %s", (lastname,))
    elif choice == 3:
        cur.execute("SELECT * from students")
    rows = cur.fetchall()
    conn.close()
    return rows


print(view(2,'B%'))

def update(choice):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    if choice == 1:
        cur.execute(
            "UPDATE students SET grade = 5 WHERE first_name = 'Jay' and grade = 10")
    elif choice == 2:
        cur.execute("UPDATE students set result ='Fail' where total_score<45")
    elif choice == 3:
        cur.execute("UPDATE students SET result= 'Hold' where age<10")
    elif choice == 4:
        cur.execute("UPDATE students set gender='M' where result='Hold'")

    conn.commit()
    conn.close()


def updateln(last_name):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    cur.execute(
        "UPDATE students set last_name = %s where first_name like 'Ruhi'", (last_name,))
    conn.commit()
    conn.close()


def delete(choice):
    conn = psycopg2.connect(
        "dbname='python_test' user = 'dakshbindal' password='123' host='localhost' port ='5432'")
    cur = conn.cursor()
    if choice == 1:
        cur.execute("DELETE from students where age<5")
    if choice == 2:
        cur.execute("DELETE from students where grade=1")
    conn.commit()
    conn.close()

# print(view(1))

# print(view(2))

# update(1)
# print(view(3))

# delete(1)
# print(view(3))

# update(2)
# print(view(3))

# update(3)
# print(view(3))

# delete(2)
# print(view(3))

# update(4)
# print(view(3))

# updateln('XYZ')
# print(view(3))
