import sqlite3

DB_NAME = 'shop.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            stars INTEGER DEFAULT 100,
            inventory TEXT DEFAULT ''
        )
    ''')
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute('INSERT INTO users (user_id, stars, inventory) VALUES (?, ?, ?)', (user_id, 100, ''))
        conn.commit()
        user = (user_id, 100, '')
    conn.close()
    return user

def buy_item(user_id, item_name, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT stars, inventory FROM users WHERE user_id = ?', (user_id,))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return False
    
    current_stars, inventory_str = row
    inventory = inventory_str.split(',') if inventory_str else []
    
    # Защита от дублей
    if item_name in inventory:
        conn.close()
        return 'already_has'
    
    if current_stars >= price:
        new_stars = current_stars - price
        inventory.append(item_name)
        new_inventory_str = ','.join(inventory)
        
        cursor.execute('UPDATE users SET stars = ?, inventory = ? WHERE user_id = ?', 
                       (new_stars, new_inventory_str, user_id))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def get_inventory(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT inventory FROM users WHERE user_id = ?', (user_id,))
    res = cursor.fetchone()
    conn.close()
    if res and res[0]:
        return res[0].split(',')
    return []

def get_rating(user_id):
    inv = get_inventory(user_id)
    stars = get_user(user_id)[1]
    return stars + (len(inv) * 10)
