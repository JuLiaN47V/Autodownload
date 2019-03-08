#!/usr/bin/python3

from tkinter import *
top = Tk()

top.geometry("200x300")

CProgram = Label(top,text = 'chocolatey Programmname')
CProgram.pack()





def retrieve_input():
	Program = textBox.get("1.0","end-1c")
	List = Lb1.get("active")
	name = NamenFeld.get("1.0","end-1c")
	print(Program)
	if List == "Compresson":
		f = open("CompressonCount.txt", "r")
		Input = int(f.read())
		Hoch = Input * 25
		Hoch = Hoch + 297
		Count = Input + 1
		f.close()
		
		f = open("CompressonCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 515
		LeftText = LeftBox + 35
		LeftBild = LeftText + 42

	elif List == "Web":
		f = open("WebCount.txt", "r")
		Input = int(f.read())
		Hoch = Input * 25
		Hoch = Hoch + 297
		Count = Input + 1
		f.close()
		
		f = open("WebCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 100
		LeftText = LeftBox + 35
		LeftBild = LeftText - 45
		
	
	
	c = open("index.html", "a")
	c.write("\n<style type='text/css'>\nhtml, body {\nwidth: 100%;\nheight: 100%;\nmargin: 0px;\n}\nbody {\nbackground-color: transparent;\ntransform: perspective(1400px) matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1);\ntransform-style: preserve-3d;\n}\n." + name + " {\nposition: absolute;\nfloat: left;\nmargin: 0 0 0 17px;\nwidth: 15px;\nheight: 15px;\nleft: " + str(LeftBox) + "px;\ntop: " + str(Hoch) +"px;\n}\n." + name + "Text{\nposition: absolute;\nleft: "+ str(LeftText) +"px;\ntop: " + str(Hoch) + "px;\nfont-family: Georgia;\n}\n." + name + "Bild {\nposition: absolute;\nwidth: 15px;\nheight: 15px;\ntransform-origin: 21.5px 22.5961px 0px;\nleft: "+ str(LeftBild) +"px;\n top: " + str(Hoch) + "px;\n}\n</style>\n\n<body class=\"htmlNoPages\">\n<p class=\""+ name +"Text\">"+ name +"</p>\n<img src=\""+ name +".jpg\" class=\""+ name +"Bild\">\n</body>\n")
	c.close()
	
	with open('Download.php', 'r') as f:
		file_contents = f.readlines()

	print(file_contents)
	file_contents.insert(3, "\nif ($_POST[\'"+ name +"\'] == \'1\') {\n    $"+ name +" = \"choco install "+ Program +" -y --Force\";}\n")
	print(file_contents)

	with open('Download.php', 'w') as f:
		f.writelines(file_contents)
		
	with open('index.html', 'r') as f:
		file_contents = f.readlines()

	print(file_contents)
	file_contents.insert(198, "    <input type=\"checkbox\" name=\""+ name +"\" value=\"1\" class=\""+ name +"\">\n")
	print(file_contents)

	with open('index.html', 'w') as f:
		f.writelines(file_contents)
	
	
	with open('Download.php', 'r') as f:
		file_contents = f.readlines()

	print(file_contents)
	file_contents.insert(200, "$"+ name +"")
	print(file_contents)

	with open('Download.php', 'w') as f:
		f.writelines(file_contents)








































textBox=Text(top, height=1, width=20)
textBox.pack()

CProgram = Label(top,text = 'Anzeige Name')
CProgram.pack()

NamenFeld=Text(top, height=1, width=20)
NamenFeld.pack()

Kategorie = Label(top,text = 'Kategorie')
Kategorie.pack()

	

Lb1 = Listbox(top, height=5, width=10)
Lb1.insert(1, "Compresson")
Lb1.insert(2, "Web")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()


buttonCommit=Button(top,height=1, width=10, text="commit", command=lambda: retrieve_input())
buttonCommit.pack()

top.mainloop()



