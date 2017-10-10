import sqlite3

class WizardsDB:

    def __init__(self):
        self.connection = sqlite3.connext("wizard_db.db")
        self.cursor = self.connection.cursor()

    def createWizard(self, name, age, hat_color, height):
        self.cursor.execute("INSERT INTO wizards (name, age, hat_color, height) VALUES (?, ?, ?, ?)", (name, age, hat_color, height))
        self.connection.commit()

    def getWizards(self):
        self.cursor.execute("SELECT * FROM wizards")
        self.rows = curesor.fetchall()
        return rows
