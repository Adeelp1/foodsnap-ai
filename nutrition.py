import sqlite3

class Nutrition:
    def __init__(self):
        self.conn = sqlite3.connect("database/nutrition.db")
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()

    def get_nutrition(self, name):
        self.cursor.execute("SELECT calories, fat, carbs, protien FROM nutrition_info WHERE food_name = ?", (name,))
        nutri = self.cursor.fetchall()

        return nutri[0]