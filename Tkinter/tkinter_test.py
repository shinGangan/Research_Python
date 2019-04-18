#------------------------------------------------------------
#   coding:utf-8
#------------------------------------------------------------
#	Updata History
#	November  10 23:00, 2018 (Sat) by S.Iwamaru
#------------------------------------------------------------
#
#	PythonでTkinterを実験
#		tkinter_test.py
#	
#------------------------------------------------------------
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Frame Test")

frame1 = ttk.Frame(
	root,
	height=200,
	width=300,
	relief="sunken",	#  3D効果の設定
	borderwidth=5
)
frame1.grid()

root.mainloop()