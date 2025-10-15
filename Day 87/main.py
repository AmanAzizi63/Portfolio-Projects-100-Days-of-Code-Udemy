from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Brick
from ball import Ball


window = Screen()
window.bgcolor('black')
window.screensize(canvheight=600, canvwidth=800)
window.title('Breakout')

paddle = Paddle()
ball = Ball()


ball_dx = 5
ball_dy = 5

colors = ['red', 'green', 'yellow', 'orange']
bricks = []
start_y = 250
rows = 4
bricks_per_row = 8
brick_width = 100
start_x = -brick_width * bricks_per_row // 2 + brick_width // 2
speed = 1

ball.speed(speed=speed)

window.listen()
window.onkeypress(fun=paddle.moveLeft, key='a')
window.onkeypress(fun=paddle.moveRight, key='d')

for row in range(rows):
    color = colors[row % len(colors)]
    y = start_y - row * 50
    for col in range(bricks_per_row):
        brick = Brick()
        brick.color(color)
        x = start_x + col * brick_width
        brick.goto(x, y)
        bricks.append(brick)

ball.firstMove()

def gameloop():
    global speed, ball_dx, ball_dy

    x, y = ball.position()
    ball.goto(x + ball_dx, y + ball_dy)

    # Begrenzung oben
    if y + ball_dy > 300:
        ball_dy *= -1

    # Begrenzung unten
    if y + ball_dy < -300:
        ball_dy *= -1

    # Begrenzung rechts
    if x + ball_dx > 400:
        ball_dx *= -1

    # Begrenzung links
    if x + ball_dx < -400:
        ball_dx *= -1

    if ball.distance(paddle) < 50:
        ball_dy *= -1
        speed += 0.2
        ball.speed(speed)

    for brick in bricks:
        if ball.distance(brick) < 40 and brick.isvisible():
            brick.destroyBrick()
            ball_dy *= -1
            break  

    window.ontimer(gameloop, 20)
gameloop()



window.mainloop()