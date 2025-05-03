items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Сортуємо елементи за спаданням співвідношення калорій/ціна
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            chosen_items.append(name)
            total_cost += info["cost"]
            total_calories += info["calories"]

    return {
        "items": chosen_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    
    # dp[i][w] — максимальна калорійність при розгляді перших i предметів і бюджеті w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення dp-таблиці
    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибраних предметів
    w = budget
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            chosen_items.append(name)
            w -= info["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(items[name]["cost"] for name in chosen_items)

    return {
        "items": chosen_items[::-1],  
        "total_cost": total_cost,
        "total_calories": total_calories
    }

# Приклад 
budget = 100

print("Greedy algorithm result:")
print(greedy_algorithm(items, budget))

print("\nDynamic programming result:")
print(dynamic_programming(items, budget))