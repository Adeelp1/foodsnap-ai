import os
import food
from nutrition import Nutrition


if __name__ == "__main__":
    print("type exit for exit")
    while True:
        path = input("Enter image path: ")
        if path == "exit": break
        if not os.path.isfile(path):
            print("Enter a valid path")
            continue
        weight = float(input("Please enter the weight of the food (in grams): "))

        name = food.find_food(path)
        ntn = Nutrition()
        nutri = ntn.get_nutrition(name, weight)
        cal, fat, carb, protien = nutri

        print(f"\nfood is a {name}\nNutrients : calories = {cal}, fat = {fat}g, carbs = {carb}g, protien = {protien}g\n")