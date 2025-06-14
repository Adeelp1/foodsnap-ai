import sys
import food
from nutrition import Nutrition


if __name__ == "__main__":
    image = sys.argv[1]

    name = food.find_food(image)
    obj = Nutrition()
    nutri = obj.get_nutrition(name)
    cal, fat, carb, protien = nutri

    print(f"food is a {name} and its nutritions are : calories = {cal}, fat = {fat}, carbs = {carb}, protien = {protien}")