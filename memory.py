"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path("car.gif")

symbols = [
    'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X',
    'Y', 'Z', '1', '2',
    '3', '4', '5', '6'
]

tiles = symbols * 2

state = {"mark": None, "intentos": 0}
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color("black", "white")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state["mark"]
    state["intentos"] += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state["mark"] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state["mark"] = None

        if all(tile == False for tile in hide):
            print("You won")

            up()
            goto(-70,0)
            color('green')

            write("YOU WON", font=('Arial', 30, 'bold'))

            update()
            done()


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state["mark"]

    if mark is not None and hide[mark]:
        x, y = xy(mark)

        up()
        goto(x + 15, y + 10)

        color("black")

        write(tiles[mark], font=("Arial", 18, "bold"))

    up()
    goto(-195, 210)
    color("black")
    write(f"Intentos: {state['intentos']}", font=("Arial", 80, "normal"))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
