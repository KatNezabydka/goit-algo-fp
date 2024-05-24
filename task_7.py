"""
Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел,
 які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел,
 які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
"""
import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll_sum = roll1 + roll2
        sums_count[roll_sum] += 1

    probabilities = {s: count / num_rolls for s, count in sums_count.items()}

    return probabilities


def plot_probabilities(probabilities, theoretical_probabilities):
    sums = list(probabilities.keys())
    values = list(probabilities.values())
    theoretical_values = list(theoretical_probabilities.values())

    plt.figure(figsize=(10, 6))
    plt.bar(sums, values, alpha=0.6, label='Monte Carlo Simulation')
    plt.plot(sums, theoretical_values, 'ro-', label='Theoretical Probabilities')
    plt.xlabel('Sum of Dice Rolls')
    plt.ylabel('Probability')
    plt.title('Probability Distribution of Sums from Rolling Two Dice')
    plt.legend()
    plt.grid(True)
    plt.show()


theoretical_probabilities = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36
}

num_rolls = 1000000
probabilities = simulate_dice_rolls(num_rolls)

for sum_, prob in probabilities.items():
    print(
        f'Sum: {sum_}, Simulated Probability: {prob:.5f}, Theoretical Probability: {theoretical_probabilities[sum_]:.5f}')

plot_probabilities(probabilities, theoretical_probabilities)
