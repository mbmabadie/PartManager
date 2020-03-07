import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, product text, customer text, part text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, product, customer, part, price):
        self.cur.execute("Insert Into parts values (NULL, ?, ?, ?, ?)",(product, customer, part, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("Delete from parts where id=?", (id,))
        self.conn.commit()
    
    def update(self, id, product, customer, part, price):
        self.cur.execute("UPDATE parts SET product = ?, customer = ?, part = ?, price = ? WHERE id = ?",
                        (product, customer, part, price, id))
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()

# db = Database('store.db')
# db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
# db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
# db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
# db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
# db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
# db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
# db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")   