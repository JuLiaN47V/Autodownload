#!/usr/bin/python3

from tkinter import *
top = Tk()

top.geometry("200x350")

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
		Hoch = Input + 34.7
		HochBild = Hoch - 0.3
		HochText = Hoch + 0.4
		Count = Input + 3
		f.close()
		
		f = open("CompressonCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 10
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1

	elif List == "Web":
		f = open("WebCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 34.7
		Count = Input + 3
		f.close()
		
		f = open("WebCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 24
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
	
	elif List == "Video":
		f = open("VideoCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 34.7
		Count = Input + 3
		f.close()
		
		f = open("VideoCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 36.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Imaging":
		f = open("ImagingCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 34.7
		Count = Input + 3
		f.close()
		
		f = open("ImagingCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 49.3
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Audio":
		f = open("AudioCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 34.7
		Count = Input + 3
		f.close()
		
		f = open("AudioCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 64.9
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Developer":
		f = open("DeveloperCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 34.7
		Count = Input + 3
		f.close()
		
		f = open("DeveloperCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 79.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Text":
		f = open("TextCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 85
		Count = Input + 3
		f.close()
		
		f = open("TextCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 9.2
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Gaming":
		f = open("GamingCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 85
		Count = Input + 3
		f.close()
		
		f = open("GamingCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 23.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Security":
		f = open("SecurityCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 85
		Count = Input + 3
		f.close()
		
		f = open("SecurityCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 39.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Messaging":
		f = open("MessagingCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 85
		Count = Input + 3
		f.close()
		
		f = open("MessagingCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 56.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
		
	elif List == "Others":
		f = open("OthersCount.txt", "r")
		Input = int(f.read())
		Hoch = Input + 85
		Count = Input + 3
		f.close()
		
		f = open("OthersCount.txt", "w")
		f.write(str(Count))
		f.close()
		LeftBox = 76.5
		LeftText = LeftBox + 2
		LeftBild = LeftText - 3.1
	
	
	c = open("index.html", "a")
	c.write("\n<style type='text/css'>\nhtml, body {\nwidth: 100%;\nheight: 100%;\n}\nbody {\nbackground-color: transparent;\ntransform-style: preserve-3d;\n}\n." + name + " {\nposition: absolute;\nfloat: left;\nwidth: 2%;\nheight: 2%;\nleft: " + str(LeftBox) + "%;\ntop: " + str(Hoch) +"%;\n}\n." + name + "Text{\nposition: absolute;\nleft: "+ str(LeftText) +"%;\ntop: " + str(HochText) + "%;\nfont-family: Georgia;\n}\n." + name + "Bild {\nposition: absolute;\nwidth: 1.5%;\nheight: 3%;\nleft: "+ str(LeftBild) +"%;\n top: " + str(HochBild) + "%;\n}\n</style>\n\n<body class=\"htmlNoPages\">\n<p class=\""+ name +"Text\">"+ name +"</p>\n<img src=\""+ name +".jpg\" class=\""+ name +"Bild\">\n</body>\n")
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
	file_contents.insert(224, "<input type=\"checkbox\" name=\""+ name +"\" value=\"1\" class=\""+ name +"\">\n")
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

	

Lb1 = Listbox(top, height=11, width=12)
Lb1.insert(1, "Compresson")
Lb1.insert(2, "Web")
Lb1.insert(3, "Video")
Lb1.insert(4, "Imaging")
Lb1.insert(5, "Audio")
Lb1.insert(6, "Developer")
Lb1.insert(7, "Text")
Lb1.insert(8, "Gaming")
Lb1.insert(9, "Security")
Lb1.insert(10, "Messaging")
Lb1.insert(11, "Others")
Lb1.pack()


buttonCommit=Button(top,height=1, width=10, text="commit", command=lambda: retrieve_input())
buttonCommit.pack()

top.mainloop()



