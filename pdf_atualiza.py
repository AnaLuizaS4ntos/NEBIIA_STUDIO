import sqlite3

# Conecta no banco
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

try:
    # O comando mágico que cria a coluna que está faltando
    cursor.execute("ALTER TABLE roteiros ADD COLUMN pdf TEXT")
    print("SUCESSO! Coluna 'pdf' criada.")
except sqlite3.OperationalError as e:
    # Se der erro, ele avisa o porquê (provavelmente se já existir)
    print(f"Aviso: {e}")

conn.commit()
conn.close()