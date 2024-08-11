items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    item_list = [{'name': name, **details} for name, details in items.items()]
    sorted_items = sorted(item_list, key=lambda item: item['calories'] / item['cost'], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item in sorted_items:
        if remaining_budget >= item['cost']:
            chosen_items.append(item['name'])
            total_calories += item['calories']
            remaining_budget -= item['cost']

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    num_items = len(items)

    dp_table = [[0 for x in range(budget + 1)] for y in range(num_items + 1)]

    # Наповнення таблиці
    for i in range(1, num_items + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        for w in range(budget + 1):
            if cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - cost] + calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    chosen_items = []
    w = budget
    for i in range(num_items, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            w -= items[item_names[i - 1]]['cost']

    return dp_table[num_items][budget], budget - w, chosen_items


if __name__ == '__main__':
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy Algorithm Result:", greedy_result)
    print("Dynamic Programming Result:", dp_result)
