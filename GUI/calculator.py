from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('600x800')
root.configure(bg='#d4deec')
               
num_input = Entry(root, font=("Courier", 30), width = 20, bd=6, relief=tk.SUNKEN, justify=RIGHT)
num_input.pack(ipadx=20, ipady=60, pady=25)

def display_num(number):
    old_text = num_input.get()
    num_input.delete(0, END)
    num_input.insert(0, old_text + number)
    print(old_text + number)

def select_operator(operator):
    global firstnum 
    firstnum = num_input.get()
    global opr
    opr = operator
    print(operator)
    num_input.delete(0, END)

def equalFunction():
    secondnum = num_input.get()
    global answer
    
    if opr == "+":
        answer = float(firstnum) + float(secondnum) 
    elif opr == "-":
         answer = float(firstnum) - float(secondnum)
    elif opr == "x":
         answer = float(firstnum) * float(secondnum)
    elif opr == "/":
         answer = float(firstnum) // float(secondnum)
    print(answer)
    num_input.delete(0, END)
    num_input.insert(END, answer)

def clear():
    print("Clear", clear)
    num_input.delete(0, END)

number = Button(root,text='1', height=7, width = 11, fg='black', bg='#f6f8fb', font=('Courier', 10), command = lambda:display_num('1'))
number1 = Button(root, text='2',height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('2'))
number2 = Button(root, text='3', height=7, width = 11,fg='black', bg='#f6f8fb', font=('Courier', 10),command = lambda:display_num('3'))
plus = Button(root, text='+', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('+'))
minus = Button(root, text='-', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('-'))
number5 = Button(root, text='4', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('4'))
number6 = Button(root, text='5', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('5'))
number7 = Button(root, text='6', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10), command = lambda:display_num('6'))
number8 = Button(root, text='x', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('x'))
number9 = Button(root, text='/', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('/'))
number10 = Button(root, text='7', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('7'))
number11 = Button(root, text='8', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('8'))
number12 = Button(root, text='9', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('9'))
number13 = Button(root, text='=', height=15, width = 26, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('='))
dot = Button(root, text='.', height=7, width=11,fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('.'))
zero = Button(root, text='0',height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('0'))
cee = Button(root, text='C', height=7, width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:display_num('C'))

plus = Button(root, text='+', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:select_operator('+'))
minus = Button(root, text='-', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:select_operator('-'))
number8 = Button(root, text='x', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:select_operator('x'))
number9 = Button(root, text='/', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:select_operator('/'))
number13 = Button(root, text='=', height=15,width = 26, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:equalFunction())
cee = Button(root, text='C', height=7,width = 11, fg='black', bg='#f6f8fb',font=('Courier', 10),command = lambda:clear())



number.place(x = 30, y = 230)
number1.place(x = 135, y = 230)
number2.place(x = 245, y = 230)
plus.place(x = 360, y = 230)
minus.place(x = 473, y = 230)
number5.place(x = 30, y = 367)
number6.place(x = 135, y = 367)
number7.place(x = 245, y = 367)
number8.place(x = 360, y = 367)
number9.place(x = 473, y = 367)
number10.place(x = 30, y = 504)
number11.place(x = 135, y = 504)
number12.place(x = 245, y = 504)
number13.place(x = 360, y = 504)
dot.place(x = 30, y = 641)
zero.place(x = 135, y = 641)
cee.place(x = 245, y = 641)


root.mainloop()