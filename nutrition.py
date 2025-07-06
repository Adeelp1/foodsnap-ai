import sqlite3
from config import DB_PATH

class Nutrition:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()

    def get_nutrition(self, name, weight) -> list:
        self.cursor.execute("SELECT calories, fat, carbs, protien FROM nutrition_info WHERE food_name = ?", (name,))
        nutri = self.cursor.fetchall()
        nutrition_info = self.calculate_calories(nutri[0], weight)

        return nutrition_info
    
    def calculate_calories(self, nutri_info, weight) -> list:
        factor = weight/100
        nutrition_result = []

        for i in range(len(nutri_info)):
            nutrition_result.append(nutri_info[i] * factor)

        return nutrition_result