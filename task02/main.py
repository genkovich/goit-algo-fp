import matplotlib.pyplot as plt
import numpy as np


def draw_branch(x, y, angle, length, depth):
    if depth == 0:
        return

    # Обчислюємо нові координати для кінця гілки
    x_new = x + length * np.cos(angle)
    y_new = y + length * np.sin(angle)

    # Малюємо гілку
    plt.plot([x, x_new], [y, y_new], color='brown', lw=2)

    # Викликаємо рекурсивно для лівої та правої гілок
    draw_branch(x_new, y_new, angle + np.pi / 6, length * 0.7, depth - 1)  # ліва гілка
    draw_branch(x_new, y_new, angle - np.pi / 6, length * 0.7, depth - 1)  # права гілка


def main():
    # Налаштування вікна для малювання
    plt.figure(figsize=(8, 8))
    plt.axis('off')

    # Запит у користувача рівня рекурсії
    depth = int(input("Введіть рівень рекурсії (глибину): "))

    # Малюємо початкову гілку
    draw_branch(0, 0, np.pi / 2, 1, depth)

    # Відображення результату
    plt.show()


if __name__ == "__main__":
    main()
