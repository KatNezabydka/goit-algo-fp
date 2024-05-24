"""
Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”.
Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
"""
import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        t.forward(length)
        t.backward(length)
    else:
        t.forward(length)
        t.left(45)
        draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
        t.right(90)
        draw_pythagoras_tree(t, length / math.sqrt(2), level - 1)
        t.left(45)
        t.backward(length)

screen = turtle.Screen()
screen.title("Pythagoras Tree")

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, -200)
t.pendown()
t.left(90)

level = int(screen.textinput("Pythagoras Tree", "Enter the level of recursion:"))

draw_pythagoras_tree(t, 100, level)

screen.mainloop()

