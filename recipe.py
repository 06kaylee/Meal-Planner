# dictionary with regular recipes and ingredients
# dictionary with categories for each meal (chicken, fish, etc)
# randomly selected based on: havent had that meal in a couple weeks, no back to back meals of same category, cant have same category more than twice per week, etc
# store in db?

# select option for if you want to go out to eat (how many times per week?)
# money/savings tracker? total the amount that the ingredients will cost. factor that into how much you want to spend on food per week
import pprint
import re
import collections
import random
import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import recipe_db as db



def read_recipes(file):
    """ Reads in a saved_recipes.txt and stores the recipes in a dictionary."""
    recipes = collections.defaultdict(dict)
    with open("saved_recipes.txt", mode = 'r') as recipe_file:
        for line in recipe_file:
            # separate the name and cuisine type from the ingredient list
            recipe_info, ingredients_str = line.split("-", 1)
            # separates the recipe name and the cuisine type into capturing groups
            info_search = re.search(r'^([^\(]+)\((\w+)\)', recipe_info)
            if info_search:
                recipe_name, category = info_search.group(1).strip(), info_search.group(2).strip()
            ingredients = ingredients_str.split(",")
            ingredients = [ingredient.strip() for ingredient in ingredients]
            recipes[recipe_name]['Category'] = category
            recipes[recipe_name]['Ingredients'] = ingredients
    return recipes

    
def adjust_options(options):
    chosen_options = []
    for option, bool_value in options.items():
        change_option = input(f"'{option}' is set to {bool_value}. Would you like to change it? (y/n) ")
        if change_option.lower() == 'y' and bool_value == False:
            chosen_options.append(option)
    return chosen_options


def generate_pdf(random_week):
    report = SimpleDocTemplate('weekly_meals.pdf')
    styles = getSampleStyleSheet()
    title = Paragraph('Weekly Meals', styles['h1'])
    recipes_str = ""
    for day, value in random_week.items():
        recipe_name = value[0];..;
        ingredients = ", ".join([ingredient for ingredient in ingredients_list])
        recipes_str += f"{recipe_name}: {ingredients} <br /> <br />"
    info = Paragraph(recipes_str, styles['BodyText'])
    empty_line = Spacer(1, 20)
    report.build([title, empty_line, info, empty_line])


def main():
    database = ":memory:"

    sql_create_recipes_table = """CREATE TABLE IF NOT EXISTS recipes (
                                        id integer PRIMARY KEY,
                                        name text,
                                        category text,
                                        ingredients text
                                );"""
    conn = db.create_connection(database)

    all_options = {
        "Takeout": False
    }


    chosen_options = adjust_options(all_options)

    
    if conn is not None:
        db.create_table(conn, sql_create_recipes_table)
        recipes = dict(read_recipes("saved_recipes.txt"))
        for name, info in recipes.items():
            category = info['Category']
            ingredients_list = info['Ingredients']
            ingredients_str = ", ".join([ingredient for ingredient in ingredients_list])
            db.insert_recipe(conn, (name, category, ingredients_str))
        recipes = db.select_random_week(conn, chosen_options)
        for recipe in recipes:
            print(recipe)
        conn.close()
    else:
        print("Cannot create connection to database.")
            

    

if __name__ == "__main__":
    main()
    


# To do:
# Clean up functions and all that 
    # 3. Scrape for new recipes (reorganize project files?)
    # 4. GUI
        # a. tabs for: randomly select from db (has tags that the user can choose from), manually select from db, search for new recipes
        # b. place to look at previous weeks?
        # c. Walmart availability
        # d. Money tracker thing

# change read recipes so that its comma separated. maybe use pandas then
    
