```python
"""cannon, hitting targets with projectiles

exercises
1. keep score by counting target hits
2. vary the effect of gravity
3. apply gravity to the targets
4. change the speed of the ball
"""

# se importan las herramientas que se van a usar
from random import randrange
from turtle import *
from freegames import vector

# se crean la pelota, su velocidad y la lista de objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """responder al clic de la pantalla"""
    # si la pelota no está en la pantalla se puede disparar
    if not inside(ball):
        ball.x = -200
        ball.y = -200

        # se calcula la velocidad del disparo dependiendo del clic
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """revisar si un objeto está dentro de la pantalla"""
    # se comprueba que sus coordenadas estén dentro de los límites
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """dibujar la pelota y los objetivos"""
    # se limpia la pantalla para volver a dibujar todo
    clear()

    # se dibujan todos los objetivos de color azul
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    # se dibuja la pelota roja si sigue dentro de la pantalla
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # se actualiza la pantalla para mostrar los cambios
    update()


def move():
    """mover la pelota y los objetivos"""
    # de vez en cuando aparece un nuevo objetivo en la pantalla
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    # los objetivos se mueven poco a poco hacia la izquierda
    for target in targets:
        target.x -= 0.5

    # si la pelota está en pantalla se aplica la gravedad
    if inside(ball):
        speed.y -= 0.35

        # se mueve la pelota según su velocidad
        ball.move(speed)

    # se hace una copia de los objetivos para revisarlos
    dupe = targets.copy()
    targets.clear()

    # se conservan los objetivos que no han sido golpeados
    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    # se dibuja otra vez el juego
    draw()

    # si algún objetivo sale de la pantalla se detiene el movimiento
    for target in targets:
        if not inside(target):
            return

    # se vuelve a ejecutar move después de 50 milisegundos
    ontimer(move, 50)


# se configura el tamaño y la posición de la ventana
setup(420, 420, 370, 0)

# se oculta el cursor de la tortuga
hideturtle()

# se levanta el lápiz para que no dibuje al moverse
up()

# se desactiva la actualización automática de la pantalla
tracer(False)

# se conecta el clic del mouse con la función tap
onscreenclick(tap)

# se inicia el movimiento del juego
move()

# se mantiene abierta la ventana
done()
```