import turtle as trtl

#draws a curve left 90 degrees
trtl.pendown()
for i in range(6):
  trtl.forward(10)
  trtl.left(15)
trtl.penup()

def draw_axes():
  trtl.goto(0,0)
  trtl.pendown()
  trtl.forward(100)
  trtl.backward(200)
  trtl.forward(100)
  trtl.left(90)
  trtl.forward(100)
  trtl.backward(200)
  trtl.pendown()
  trtl.goto(0,0)

draw_axes()

