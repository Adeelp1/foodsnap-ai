import sqlite3
from config import DB_PATH

class Nutrition:
    def __init__(self) -> None:
        """
        Establish a connection to the SQLite database.
        """
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
    
    def __del__(self) -> None:
        """
        Close the established database connection.
        """
        self.cursor.close()

    def get_nutrition(self, name: str, weight: float) -> list[float]:
        """
        Retrieve nutrition information from the database.

        Args:
            name (str): Name of the food item.
            weight (float): Weight of the food in grams.
        
        Returns:
            list[float]: A list containing nutritional values:
                [calories, fat, carbs, protein]
        """
        self.cursor.execute("SELECT calories, fat, carbs, protien FROM nutrition_info WHERE food_name = ?", (name,))
        nutri = self.cursor.fetchall()
        nutrition_info = self.calculate_calories(nutri[0], weight)

        return nutrition_info
    
    def calculate_calories(self, nutri_info: tuple[float, float, float, float], weight: float) -> list[float]:
        """
        Calculate the nutritional values based on the given weight.

        Args:
            nutri_info (tuple[float, float, float, float]): Nutritional values per 100g retrieved from the database, in the order:
                (calories, fat, carbs, protein).
            weight (float): Weight of the food in grams.
        
        Returns:
            list[float]: Scaled nutritional values based on the given weight:
                [calories, fat, carbs, protein]
        """
        factor = weight/100
        nutrition_result = []

        for i in range(len(nutri_info)):
            nutrition_result.append(nutri_info[i] * factor)

        return nutrition_result