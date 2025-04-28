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
            barcode TEXT NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock REAL NOT NULL,
            total_sold REAL NOT NULL,
            no_stock TEXT NOT NULL,
            last_added TEXT NOT NULL,
            first_added TEXT NOT NULL,
            notes TEXT NOT NULL,
            background_color TEXT NOT NULL,
            foreground_color TEXT NOT NULL,
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

    def get_categories(self):
        self.connect()

        self.cursor.execute("SELECT id, name, background_color, foreground_color FROM categories")
        result = self.cursor.fetchall()
        
        self.close()
        return result
    
    def get_subcat_from_cat(self, cat_id):
        self.connect()

        self.cursor.execute("SELECT name FROM subcategories WHERE category_id = ?", (cat_id,))
        result = self.cursor.fetchall()
        
        self.close()
        return result
    
    def get_menu_items(self):
        self.connect()
        
        query = """
        SELECT 
            menu_items.barcode,
            categories.name AS category_name,
            subcategories.name AS subcategory_name,
            menu_items.name,
            menu_items.price,
            menu_items.stock,
            menu_items.total_sold,
            menu_items.no_stock,
            menu_items.last_added,
            menu_items.firt_added,
            menu_items.notes,
            menu_items.background_color,
            menu_items.foreground_color

        FROM menu_items
        JOIN subcategories ON menu_items.subcategory_id = subcategories.id
        JOIN categories ON subcategories.category_id = categories.id
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.close()
        return result
    
    def get_specific_menu_item(self, barcode):
        self.connect()
        query = """
        SELECT 
            menu_items.barcode,
            categories.name AS category_name,
            subcategories.name AS subcategory_name,
            menu_items.name,
            menu_items.price,
            menu_items.stock,
            menu_items.total_sold,
            menu_items.no_stock,
            menu_items.last_added,
            menu_items.firt_added,
            menu_items.notes,
            menu_items.background_color,
            menu_items.foreground_color

        FROM menu_items
        JOIN subcategories ON menu_items.subcategory_id = subcategories.id
        JOIN categories ON subcategories.category_id = categories.id
        WHERE menu_items.barcode = ?
        """
        self.cursor.execute(query, (barcode,))
        result = self.cursor.fetchone()
        self.close()
        return result
    
    def insert_new_menu_item(self, data):
        """Data is given in dict format, processed here and uploaded to db."""
        self.connect()

        self.cursor.execute("""
            SELECT id FROM categories WHERE name = ?
        """, (data['cat'],))
        category_id = self.cursor.fetchone()[0]

        self.cursor.execute("""
            SELECT id FROM subcategories WHERE name = ? AND category_id = ?
        """, (data['subcat'], category_id))
        subcategory_id = self.cursor.fetchone()[0]

        # Step 3: Insert menu item into the 'menu_items' table
        self.cursor.execute("""
            INSERT INTO menu_items 
            (subcategory_id, barcode, name, price, stock, total_sold, no_stock, last_added, firt_added, notes, background_color, foreground_color) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            subcategory_id,
            data['barcode'],
            data['name'],
            float(data['price']),
            float(data['stock']),
            0.0,  # Assuming `total_sold` is initially 0
            'Yes' if data['no-stock'] else 'No',  # Converting boolean to string
            '2025-04-28',  # Use current timestamp or a placeholder for 'last_added'
            '2025-04-28',  # Use current timestamp or a placeholder for 'first_added'
            data['notes'],
            data['bg_color'],
            data['fg_color']
        ))
        self.conn.commit()
        print("Uploaded sucessfully")
        self.close()
    
    def get_barcode(self, barcode):
        self.connect()

        query = """SELECT barcode FROM menu_items WHERE barcode = ?"""
        self.cursor.execute(query, (barcode,))
        result = self.cursor.fetchall()
        self.close()
        return result
    
    def update_menu_item(self, data):
        """
        Update a menu item in the database using barcode as the key.
        `data` should be a dictionary containing the fields to update.
        """
        self.connect()
        self.cursor.execute("""
            UPDATE menu_items
            SET
                name = ?,
                price = ?,
                stock = ?,
                notes = ?,
                no_stock = ?,
                background_color = ?,
                foreground_color = ?,
                last_added = ?
            WHERE barcode = ?
        """, (
            data['name'],
            data['price'],
            data['stock'],
            data.get('notes', ''),
            'Yes' if data.get('no-stock', False) else 'No',
            data.get('bg_color', '#FFFFFF'),
            data.get('fg_color', '#000000'),
            '2025-04-28',  # Example: you should use current timestamp
            data['barcode']
        ))

        self.conn.commit()
        self.close()
            
    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = MenuDatabase()

    print(db.get_specific_menu_item("12313131231"))