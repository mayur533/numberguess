import tkinter as tk
import ttkbootstrap as ttk
import random
from tkinter import messagebox

# Create the root window
root = tk.Tk()
root.geometry("400x400")
root.title("Number Guessing Game")

# Set ttkbootstrap theme to 'journal'
style = ttk.Style(theme="darkly")
# Initialize All variables 
count=1
options = ["Easy 1-25","Easy 1-25" ,"Medium 1-50", "Hard 1-100"]
selected = tk.StringVar()
selected.set(options[0])
var=tk.StringVar()
def on_enter(event, text2, text_entry, button2, var, num):  # Event handler for Enter key
        ifwin(text2, text_entry, button2, var, num)
def onclick(event,text1,option,button1,selected):
        gamescreen(text1,option,button1,selected)
def homescreen():
	
	text1 = ttk.Label(root, text="Select The Level", font="Calibri 20 bold")
	option = ttk.OptionMenu(root, selected, *options)
	button1 = ttk.Button(root, text="Start", style="success.TButton",command=lambda choice=selected: gamescreen(text1,option,button1,selected))
	
	text1.pack(pady=40)
	option.pack(pady=30)
	button1.pack(pady=20)
	root.bind("<Return>", lambda event: onclick(event,text1,option,button1,selected))
	
	
def gamescreen(a,b,c,selected):
	destroyhome(a,b,c)
	if selected.get()=="Easy 1-25":
		choice=25
	elif selected.get()=="Medium 1-50":
		choice=50
	elif selected.get()=="Hard 1-100":
		choice=100
	text2 = ttk.Label(root, text="Guess the Number ", font="Calibri 24 bold")
	text_entry=ttk.Entry(root,textvariable=var,font="Calibri 14 bold")
	
	num=random.randint(1,choice)
	button2=ttk.Button(root, text="Start", style="success.TButton",command=lambda : ifwin(text2,text_entry,button2,var,num))
	text2.pack(pady=40)
	text_entry.pack(pady=30)
	button2.pack(pady=20)
	text_entry.bind("<Return>", lambda event: on_enter(event, text2, text_entry, button2, var, num))
	
def destroyhome(text1,option,button1):
	text1.destroy()
	option.destroy()
	button1.destroy()

def destroygame(text2,text_entry,button2):
	text2.destroy()
	text_entry.destroy()
	button2.destroy()

def ifwin(a,b,c,var,num):
	global count
	try:
		val = int(var.get())
	except ValueError:
		messagebox.showerror("Invalid Input", "Please enter a valid number.", parent=root)
		var.set('')
		return
	winner=["Congratulations! You've guessed the correct number!","You're a mind reader! That's the right number!","You've got it! You're really good at this!"]
	less=["Try again! The number you're looking for is smaller.","Oops, that's not it. The number is smaller than your guess.","Getting warmer! But the actual number is smaller."]
	big=["Keep guessing! The number you're looking for is bigger.","Close, but not quite. The number is bigger than what you guessed.","You're on the right track! Try a bigger number."]
	
	if val==num :
		messagebox.showinfo("Winner", f"{random.choice(winner)}",parent=root)
		var.set("")
		count=0
		reset(a,b,c)
	elif val>num and 5-count!=0:
		messagebox.showinfo("Winner", f"{random.choice(less)}\n {5-count} Chances Left ",parent=root)
		var.set("")
		b.focus_set()
	elif val<num and 5-count!=0:
		messagebox.showinfo("Winner", f"{random.choice(big)}\n {5-count} Chances Left",parent=root)
		var.set("")
		b.focus_set()
	count+=1
	if count>5 :
		messagebox.showinfo("Lost", f"You Lost",parent=root)
		var.set("")
		count=0
		reset(a,b,c)
def reset(a,b,c):
	ans = messagebox.askquestion("Confirm", "Want To Try Again?")
	if ans == "yes":
		destroygame(a,b,c)
		homescreen()
	else:
		root.destroy()
		
	
homescreen()
root.mainloop()





 





