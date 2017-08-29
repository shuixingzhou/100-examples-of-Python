#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：画图，学用circle画圆形。
'''
if __name__ == '__main__':
    from Tkinter import *
 
    canvas = Canvas(width=800, height=600, bg='yellow')  
    canvas.pack(expand=YES, fill=BOTH)                
    k = 1
    j = 1
    for i in range(0,26):
        canvas.create_oval(310 - k,250 - k,310 + k,250 + k, width=1)
        k += j
        j += 0.3
 
    mainloop()

if __name__ == '__main__':
    import turtle
    turtle.title("画圆")
    turtle.setup(800,600,0,0)
    pen=turtle.Turtle()
    pen.color("yellow")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(1)
    pen.circle(100)
