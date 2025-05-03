import random
import matplotlib
matplotlib.use('Agg')  # Використовуємо backend без GUI

import matplotlib.pyplot as plt

# Функція для симуляції кидків кубиків
def simulate_dice_rolls(num_rolls):
    outcomes = {i: 0 for i in range(2, 13)}
    for _ in range(num_rolls):
        roll = random.randint(1, 6) + random.randint(1, 6)
        outcomes[roll] += 1
    for key in outcomes:
        outcomes[key] /= num_rolls
    return outcomes

# Функція для побудови графіка
def plot_probabilities(simulated, analytical, filename):
    sums = list(simulated.keys())
    simulated_probs = [simulated[sum_] for sum_ in sums]
    analytical_probs = [analytical[sum_] for sum_ in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, simulated_probs, alpha=0.7, label='Монте-Карло')
    plt.plot(sums, analytical_probs, 'ro-', label='Аналітичні')
    plt.xlabel('Сума на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Монте-Карло vs Аналітика)')
    plt.legend()
    plt.grid(True)
    plt.xticks(sums)
    plt.savefig(filename)  # Збереження у файл
    plt.close()

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Основний виклик
num_rolls = 100000
simulated_outcomes = simulate_dice_rolls(num_rolls)
plot_probabilities(simulated_outcomes, analytical_probabilities, "dice_simulation.png")