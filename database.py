import sqlite3

class MenuDatabase:
    def __init__(self, db_name="menu.db"):
        self.db_name = db_name
        self.create_tables()

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.connect()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            background_color TEXT,
            foreground_color TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS subcategories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            background_color TEXT,
            foreground_color TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subcategory_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            background_color TEXT,
            foreground_color TEXT,
            FOREIGN KEY (subcategory_id) REFERENCES subcategories(id)
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            euro REAL DEFAULT 1,
            dollar REAL DEFAULT 1,
            sterlin REAL DEFAULT 1)
                            """)
        
        self.cursor.execute("""
        INSERT OR IGNORE INTO exchange (id, euro, dollar, sterlin)
        VALUES (1, 1, 1, 1)
        """)
        self.conn.commit()
        self.close()

    def update_exchange(self, euro, dollar, sterlin):
        self.connect()

        self.cursor.execute("""
            UPDATE exchange
            SET euro = ?, dollar = ?, sterlin = ?
            WHERE id = 1
            """, (euro, dollar, sterlin))
        self.conn.commit()

        self.close()
        print("Updated Exchange Rates!")

    def get_exchange(self):
        self.connect()

        self.cursor.execute("""SELECT euro, dollar, sterlin FROM exchange WHERE id=1""")
        
        euro, dollar, sterlin = self.cursor.fetchone()
        self.close()
        return euro, dollar, sterlin

    def insert_category(self, name, background_color=None, foreground_color=None):
        self.connect()
        
        self.cursor.execute("""
            INSERT OR IGNORE INTO categories (name, background_color, foreground_color)
            VALUES (?, ?, ?)
        """, (name, background_color, foreground_color))
        self.conn.commit()
        self.cursor.execute("SELECT id FROM categories WHERE name = ?", (name,))
        
        self.close()
        return self.cursor.fetchone()[0]

    def insert_subcategory(self, category_name, subcategory_name, background_color=None, foreground_color=None):
        self.connect()

        category_id = self.insert_category(category_name)
        self.cursor.execute("""
            INSERT INTO subcategories (category_id, name, background_color, foreground_color)
            VALUES (?, ?, ?, ?)
        """, (category_id, subcategory_name, background_color, foreground_color))
        self.conn.commit()
        
        self.close()
        return self.cursor.lastrowid

    def insert_menu_item(self, subcategory_name, name, price, background_color=None, foreground_color=None):
        self.connect()

        self.cursor.execute("SELECT id FROM subcategories WHERE name = ?", (subcategory_name,))
        result = self.cursor.fetchone()
        if result:
            subcategory_id = result[0]
            self.cursor.execute("""
                INSERT INTO menu_items (subcategory_id, name, price, background_color, foreground_color)
                VALUES (?, ?, ?, ?, ?)
            """, (subcategory_id, name, price, background_color, foreground_color))
            self.conn.commit()
            
            self.close()
            return self.cursor.lastrowid
        else:
            self.close()
            raise ValueError(f"Subcategory '{subcategory_name}' not found.")
        

    def get_categories(self):
        self.connect()

        self.cursor.execute("SELECT name, background_color, foreground_color FROM categories")
        result = self.cursor.fetchall()
        
        self.close()
        return result

    def close(self):
        self.conn.close()
