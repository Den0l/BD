import sqlite3


class Goods:
    def __init__(self, name, price, type):
        self.name = name 
        self.price = price
        self.type = type

    @staticmethod
    def create_table():
        conn = sqlite3.connect('goods.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS goods(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL, 
                            price INTEGER, 
                            type TEXT NOT NULL
                           )''')
        conn.commit()
        conn.close()

    @staticmethod
    def search(name):
        conn = sqlite3.connect('goods.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM goods WHERE name = ?''', (name,))
        res = cursor.fetchone()
        conn.close()
        if res:
            return Goods(res[1], res[2], res[3])
        else:
            return None

    def save(self):
        conn = sqlite3.connect('goods.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO goods (name, price, type) VALUES (?, ?, ?)''',
                       (self.name, self.price, self.type))
        conn.commit()
        conn.close()

    @staticmethod
    def add():
        name = input("Название:")
        price = input("Цена:")
        type = input("Тип товара:")
        new_goods = Goods(name, price, type)
        Goods.create_table()
        new_goods.save()

    @staticmethod
    def copies():
        name = input("Имя:")
        goods_search = Goods.search(name)

        if goods_search is not None:
            print("Такой товар уже есть")
        else:
            print("Такого товара нет на складе")

    @staticmethod
    def composition():
        while True:
            choice = input(" 1 - Add \n 2 - Search \n")
            if choice == "1":
                Goods.add()
            elif choice == "2":
                Goods.copies()
            else:
                break

