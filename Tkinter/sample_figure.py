#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#	Updata History
#	November  10 23:00, 2018 (Sat) by S.Iwamaru
#------------------------------------------------------------
#
#	絵を描画
#		tkinter_test.py
#	
#------------------------------------------------------------
from tkinter import *

root = Tk()
root.title("This is a tkinter sample")
root.geometry("300x200")

canvas = Canvas(root, width=300, height=200)
canvas.create_rectangle(10, 10, 30, 60, fill="yellow")
canvas.place(x=0, y=0)

root.mainloop()