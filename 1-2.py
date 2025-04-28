# 1 задание
file='recipes.txt'

cook_book={}
with open ('recipes.txt', encoding='utf-8') as f:
    while True:
        dish = f.readline().strip()
        if not dish:
            break

        ingridients=[]
        ingridientsome=int(f.readline())
        for i in range(ingridientsome):
            ingridientline=f.readline().strip()
            name, quantity, measure=ingridientline.split('|')
            ingridients.append({
                'name': name.strip(),
                'quantity': quantity.strip(),
                'measure': measure.strip()

            })
        cook_book[dish]=ingridients
        f.readline()
print(cook_book)


# 2 задание

def get_shop_list_by_dishes(dishes, person_count):
    needed_ingredients = {}

    for dish in dishes:
        if dish not in cook_book:
            print(f'Блюда "{dish}" нет в книге рецептов.')
            continue  

        for ingredient in cook_book[dish]:
            name = ingredient['name']
            quantity = int(ingredient['quantity']) * person_count
            measure = ingredient['measure']

            if name in needed_ingredients:
                needed_ingredients[name]['quantity'] += quantity
            else:
                needed_ingredients[name] = {
                    'measure': measure,
                    'quantity': quantity
                }

    return needed_ingredients
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


