"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

# importa las herramientas para generar posiciones que sean aleatorias y controlar el juego
from random import randrange, sample, choice
from turtle import *

# importa las funciones para dibujar cuadrados y manejar posiciones
from freegames import square, vector

# establece los 5 colores que puede usar el juego, sin incluir el rojo
colors = ['blue', 'green', 'purple', 'orange', 'pink']

# elige dos colores diferentes al azar para la serpiente y la comida
snake_color, food_color = sample(colors, 2)

# establece la posición inicial de la comida, la serpiente y su dirección
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    # cambia la dirección en la que se va a mover la serpiente
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    # revisa que la cabeza de la serpiente siga dentro de los límites del juego
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """
    Mueve la comida un paso aleatorio sin salir del tablero.
    """

    # elige una dirección aleatoria para mover la comida
    directions = [(10, 0), (-10, 0), (0, 10), (0, -10)]
    dx, dy = choice(directions)

    # calcula la nueva posición de la comida
    new_x = food.x + dx
    new_y = food.y + dy

    # revisa que la comida siga dentro del tablero antes de moverla
    if inside(vector(new_x, new_y)):
        food.x = new_x
        food.y = new_y

    # programa el siguiente movimiento de la comida
    ontimer(move_food, 2000)


def move():
    """Move snake forward one segment."""
    # copia la posición de la cabeza y la mueve en la dirección indicada
    head = snake[-1].copy()
    head.move(aim)

    # revisa si la serpiente salió del área o chocó con su propio cuerpo
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    # agrega la nueva posición de la cabeza a la serpiente
    snake.append(head)

    # revisa si la serpiente comió la comida
    if head == food:
        # muestra el tamaño de la serpiente y genera una nueva comida
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        # elimina la última parte para mantener el mismo tamaño
        snake.pop(0)

    # limpia la pantalla para volver a dibujar todo
    clear()

    # dibuja cada parte del cuerpo de la serpiente con su color aleatorio
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # dibuja la comida con un color diferente al de la serpiente
    square(food.x, food.y, 9, food_color)
    update()

    # vuelve a ejecutar el movimiento después de 100 milisegundos
    ontimer(move, 100)


# configura el tamaño y la posición de la ventana del juego
setup(420, 420, 370, 0)

# oculta la tortuga y evita que la pantalla se actualice automáticamente
hideturtle()
tracer(False)

# activa los controles del teclado para mover la serpiente
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# inicia el movimiento de la serpiente y mantiene abierta la ventana
move()

# inicia el movimiento periódico de la comida
move_food()

done()