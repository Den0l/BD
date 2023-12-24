import sqlite3
import goods

class Staff:
    def __init__(self, firstname, secondname, post):
        self.firstname = firstname
        self.secondname = secondname
        self.post = post

    @staticmethod
    def create_table():
        conn = sqlite3.connect('staff.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS staff(
                            id INTEGER PRIMARY KEY,
                            firstname TEXT NOT NULL, 
                            secondname TEXT NOT NULL, 
                            post TEXT NOT NULL
                           )''')
        conn.commit()
        conn.close()

    @staticmethod
    def search(sfname, ssname):
        conn = sqlite3.connect('staff.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM staff WHERE firstname = ? AND secondname = ?''', (sfname, ssname,))
        res = cursor.fetchone()
        conn.close()
        if res:
            return Staff(res[1], res[2], res[3]) 
        else:
            return None

    def save(self):
        conn = sqlite3.connect('staff.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO staff (firstname, secondname, post) VALUES (?, ?, ?)''',
                       (self.firstname, self.secondname, self.post))
        conn.commit()
        conn.close()

    @staticmethod
    def register():
        firstname = input("Имя:")
        secondname = input("Фамилия:")
        post = input("Должность:")
        new_staff = Staff(firstname, secondname, post)
        Staff.create_table() 
        new_staff.save()

    @staticmethod
    def entry():
        firstname = input("Имя:")
        secondname = input("Фамилия:")
        staff_entry = Staff.search(firstname, secondname)

        if staff_entry is not None:
            print("Вы вошли в склад")
        else:
            print("Вас нет")

while True:
    choice = input(" 1 - reg \n 2 - entry \n")
    if choice == "1":
        Staff.register()
    elif choice == "2":
        Staff.entry()
        goods.Goods.composition()
    else:
        break
