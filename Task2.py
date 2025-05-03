import turtle
import math

def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    # Намалювати квадрат (стовбур або гілка)
    for _ in range(4):
        t.forward(length)
        t.left(90)

    # Зберегти поточне положення і напрямок
    x, y = t.pos()
    angle = t.heading()

    # Піднятися на верх квадрату
    t.forward(length)
    t.left(45)

    # Ліва гілка
    t.save_heading = t.heading()
    left_length = length * math.cos(math.radians(45))
    draw_pythagoras_tree(t, left_length, level - 1)

    # Повернутися до вершини квадрата і повернутися вправо
    t.setheading(angle)
    t.goto(x, y)
    t.forward(length)
    t.right(45)

    # Права гілка
    right_length = length * math.sin(math.radians(45))
    draw_pythagoras_tree(t, right_length, level - 1)

def main():
    level = int(input("Введіть рівень рекурсії (наприклад, 6): "))

    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Фрактал: Дерево Піфагора")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-50, -250)
    t.pendown()
    t.left(90)  # Повернути вгору

    draw_pythagoras_tree(t, 100, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
