import turtle
import math
import time

# ตั้งค่าหน้าจอ
screen = turtle.Screen()
screen.bgcolor("lightpink")
screen.title("Valentine's Envelope")

# วาดซองจดหมาย
envelope = turtle.Turtle()
envelope.speed(3)
envelope.penup()
envelope.goto(-100, -50)
envelope.pendown()
envelope.color("red")
envelope.begin_fill()
for _ in range(2):
    envelope.forward(200)
    envelope.left(90)
    envelope.forward(100)
    envelope.left(90)
envelope.end_fill()

# วาดฝาซอง
envelope.color("darkred")
envelope.begin_fill()
envelope.goto(-100, 50)
envelope.goto(0, 100)
envelope.goto(100, 50)
envelope.goto(-100, 50)
envelope.end_fill()

# เตรียม Turtle สำหรับหัวใจ
heart = turtle.Turtle()
heart.speed(0)
heart.color("red")
heart.hideturtle()

# ฟังก์ชันวาดหัวใจ
def draw_heart():
    heart.penup()
    heart.goto(0, -100)
    heart.pendown()
    
    for i in range(600):
        k = i / 50
        x = 15 * math.sin(k)**3 * 15
        y = (12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)) * 15
        heart.goto(x, y)
        heart.pendown()
    
    heart.hideturtle()

# ฟังก์ชันเมื่อคลิกซองจดหมาย
def on_click(x, y):
    if -100 < x < 100 and -50 < y < 50:
        draw_heart()

# ตรวจจับการคลิก
screen.onclick(on_click)

turtle.done()
