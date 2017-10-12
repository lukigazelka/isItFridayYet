from tkinter import *
from tkinter import messagebox
from datetime import datetime
	
	#
	# Check if it is friday logic starts here
	#
	
isItFridayAnswer = "Nope."

def isItFriday():
	today = datetime.today().weekday()
	if(today == 4):
		messagebox.showinfo("Is it Friday yet?", "Yup.")
	elif(today==3):
		messagebox.showinfo("Is it Friday yet?", "Almost.")
	else:
		messagebox.showinfo("Is it Friday yet?", "Nope.")
	#
	# End of check
	#
	
	#
	# GUI part starts here
	#

root = Tk()
root.resizable(0,0)
root.title("Is it Friday Yet?")

isItFridayButton = Button(root, text="Is it Friday Yet?", height=5, width=20, command=isItFriday)
isItFridayButton.pack()

mainloop()
	
	#
	# End of GUI part
	#