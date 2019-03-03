#!/usr/bin/python3

from tkinter import *
top = Tk()

top.geometry("200x300")

CProgram = Label(top,text = 'chocolatey Programmname')
CProgram.pack()

r = 0
Zeile1Height = 300


def retrieve_input():
	Program = textBox.get("1.0","end-1c")
	List = Lb1.get("active")
	print(Program)
	
	
	if List == "C":
		(r) = open("CompressonCount.txt", "r")
		Count = r + 1
		r.close()

		Hoch = 300 * Count
		w = open("CompressonCount.txt", "W")
		w.write(Count)
		w.close()
	
	
		f = open("css.txt", "w")
		f.write("<style type='text/css'>\nhtml, body {\nwidth: 100%;\nheight: 100%;\nmargin: 0px;\n}\nbody {\nbackground-color: transparent;\ntransform: perspective(1400px) matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);\ntransform-style: preserve-3d;\n}\n.",List," {\nposition: absolute;\nfloat: left;\nmargin: 0 0 0 17px;\nwidth: 20px;\nheight: 20px;\nleft: 515px;\ntop: ",Hoch,"px;\n}\n.",List,"Text{\nposition: absolute;\nleft: 555px;\ntop: ",Hoch,"px;\nfont-family: Georgia;\n}\n.",List,"Bild {\nposition: absolute;\nwidth: 25px;\nheight: 25px;\ntransform-origin: 21.5px 22.5961px 0px;\nleft: 609px;\n top: ",Hoch,"px;\n}\n</style>")
		f.close()
	
	
	
	
	
	
	









































textBox=Text(top, height=1, width=20)
textBox.pack()

Kategorie = Label(top,text = 'Kategorie')
Kategorie.pack()

	

Lb1 = Listbox(top, height=5, width=10)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()


buttonCommit=Button(top,height=1, width=10, text="commit", command=lambda: retrieve_input())
buttonCommit.pack()

top.mainloop()



