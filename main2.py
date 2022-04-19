import os

cook_book = dict()

def add_cook_book(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            dish_name = line.strip()
            counter = int(file.readline())
            temp_list = []
            for item in range(counter):
                ingredient_name, quantity, measure = file.readline().split("|")
                temp_list.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "measure": measure.strip()}
                )
                cook_book[dish_name] = temp_list
            file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_person = dict()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient["ingredient_name"] in cook_book_person:
                    cook_book_person[ingredient["ingredient_name"]]["quantity"] \
                        += int(ingredient["quantity"]) * person_count
                else:
                    temp = {"quantity": int(ingredient["quantity"]) * person_count, "measure": ingredient["measure"]}
                    cook_book_person[ingredient["ingredient_name"]] = temp
    return cook_book_person


add_cook_book("recipes.txt")

print(get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2))

