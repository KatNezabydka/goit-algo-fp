"""
Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та
алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність.
Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
"""


def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, item_info = item_list[i - 1]
        cost = item_info['cost']
        calories = item_info['calories']

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item_name, _ = item_list[i - 1]
            selected_items.append(item_name)
            b -= items[item_name]['cost']

    selected_items.reverse()

    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")

selected_items, total_calories = dynamic_programming(items, budget)
print(f"Selected items: {selected_items}")
print(f"Total calories: {total_calories}")
