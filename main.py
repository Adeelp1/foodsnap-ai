import os
import food
from nutrition import Nutrition


if __name__ == "__main__":
    print("type exit for exit")
    while True:
        path = input("Enter image path: ")
        if path == "exit":
            break
        if os.path.isfile(path):
            name = food.find_food(path)
            ntn = Nutrition()
            nutri = ntn.get_nutrition(name)
            cal, fat, carb, protien = nutri

            print(f"\nfood is a {name}\nNutrients per 100 grams : calories = {cal}, fat = {fat}g, carbs = {carb}g, protien = {protien}g\n")
        else:
            print("Enter a valid path")