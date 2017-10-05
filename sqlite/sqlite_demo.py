import sqlite3

connection = sqlite3.connect("wizard_db.db")
cursor = connection.cursor() # Location being pointed to

# cursor.execute("some SQL string", (a tuple with the data))

# Write data
##############################
# cursor.execute("INSERT INTO wizards (name, age, hat_color, height) VALUES (?, ?, ?, ?)", ("Dumbledore", 66, "white", 6))

# connection.commit()
##############################

# Read data
##############################
cursor.execute("SELECT * FROM wizards")
rows = cursor.fetchall()

print(rows)
##############################
