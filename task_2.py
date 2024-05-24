"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсіїНеобхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""
import turtle

def draw_pythagorean_tree(t, level, size, angle):
    if level == 0:
        return

    # Draw the square
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)

    # Draw the first subtree
    t.forward(size)
    t.left(angle)
    draw_pythagorean_tree(t, level - 1, size * 0.707, angle)
    t.right(angle)

    # Draw the second subtree
    t.backward(size)
    t.right(angle)
    t.forward(size)
    draw_pythagorean_tree(t, level - 1, size * 0.707, angle)
    t.left(angle)
    t.backward(size)


# Setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Pythagorean Tree Fractal")

t = turtle.Turtle()
t.speed(0)  # Fastest speed

# User input for recursion level
level = int(input("Enter the recursion level (e.g., 5): "))

# Set initial position and angle
t.penup()
t.goto(-200, -200)
t.pendown()
t.setheading(90)

# Draw the Pythagorean Tree fractal
draw_pythagorean_tree(t, level, 100, 45)

# Hide Turtle and display
t.hideturtle()
screen.mainloop()
