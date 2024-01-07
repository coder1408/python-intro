import turtle
import threading

turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)
turtle.Screen().bgcolor('black')
t.pensize(2)

def draw_petal():
    for j in range(9):
        for k in range(2):
            t.pencolor((255, 255, 255))
            t.circle(40 + i * 5, 90)
            t.forward(100)
            t.left(90)
        t.left(45)

threads = []
for i in range(20):
    thread = threading.Thread(target=draw_petal)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

turtle.done()
