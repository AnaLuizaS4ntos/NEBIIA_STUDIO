import sqlite3

# Conecta no seu banco atual
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

try:
    # Tenta adicionar a coluna 'pdf'. 
    # Se ela já existir, vai dar erro e cair no 'except', o que é bom (proteção).
    cursor.execute("ALTER TABLE roteiros ADD COLUMN pdf TEXT")
    print("Sucesso! Coluna de PDF criada.")
except sqlite3.OperationalError:
    print("Aviso: A coluna PDF já existia ou o banco está trancado.")

conn.commit()
conn.close()