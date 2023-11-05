import os
from pprint import pprint


def cook_book_read():
    cook_book = {}
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read().split('\n\n')
        for dish in data:
            dish = dish.split('\n')
            dish_name = dish[0]
            all_ingredient = []
            for ingredient in dish[2:]:
                ingredient = ingredient.strip()
                if ingredient:
                    ingredient_name, quantity, measure = ingredient.split('|')
                    ingredient = {
                        'ingredient_name': ingredient_name.strip(),
                        'quantity': int(quantity),
                        'measure': measure.strip()
                    }
                    all_ingredient.append(ingredient)
            cook_book[dish_name] = all_ingredient
    return cook_book

cook_book = cook_book_read()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_list = {}
    for dish_name in dishes:
        for ingredient in cook_book[dish_name]:
            if ingredient['ingredient_name'] not in ingredient_list:
                ingredient_list[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
            else:
                ingredient_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return ingredient_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))