def get_price_for_one_unit(type_of_food, price_in_leva):
    price_in_stotinki = price_in_leva * 100

    if type_of_food == 'Kilogram' or type_of_food == 'Liter':
        price_for_one_unit = price_in_stotinki / 1000
        return price_for_one_unit
    return price_in_stotinki


def increase_value_by_percent(value, percentage):
    if not percentage == 0:
        value_to_add = value * (percentage / 100)
        increased_value = value + value_to_add
        return increased_value
    return 0


def calculate_price(recipe_increase_percentage, ingredients):
    final = 0
    for el in ingredients:
        el_price_per_type = el.ingredient.price_per_type
        el_type = el.ingredient.type
        el_amount = el.amount

        price_for_smallest_piece = get_price_for_one_unit(el_type, el_price_per_type)
        el_final_price = float(el_amount) * float(price_for_smallest_piece)
        final += el_final_price
    end_price = final / 100
    increased_end_price = increase_value_by_percent(end_price, recipe_increase_percentage)
    return end_price, increased_end_price
