from sys import stdout
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Biodata')
root.geometry('300x500')
root.configure(bg='#d4deec')


def register():
	stud_name = name_entry.get()
	stud_age = age_entry.get()
	stud_skills = skills_entry.get('1.0', 'end-1c')
	stud_email = email_entry.get()

	message_error = f'Please complete the information'
	if len(stud_name) == 0:
		messagebox.showerror('Error', message_error)
	elif len(stud_age) == 0:
		messagebox.showerror('Error', message_error)
	elif len(stud_skills) == 0:
		messagebox.showerror('Error', message_error)
	elif len(stud_email) == 0:
		messagebox.showerror('Error', message_error)
	

	message = f'Registration sucessful, {stud_name}, {stud_age}, yrs old,  {stud_skills}, {stud_email}, from the department'
	messagebox.showinfo("Registration Success", message)



def print_check(checker, cb):
	print('you just clicked', cb)
	print(checker.get())






#NAME
name = Label(root, text='Name', font=('Courier',10), bg='#d4deec')
name.grid(row=0, column=0)

name_entry = Entry(root,  font=('Courier', 11))
name_entry.grid(row=0, column=1, pady=5)

#AGE
age = Label(root, text='Age', font=('Courier', 11), bg='#d4deec')
age.grid(row=1, column=0)

age_entry = Entry(root,  font=('Courier', 11))
age_entry.grid(row=1, column=1)

#Gender
gender = Label(root, text='Gender', font=('Courier', 11), bg='#d4deec')
gender.grid(row=2, column=0)


sex_var = StringVar()
sex_var.set(" ")
male_radio = Radiobutton(root, text='Male', variable=sex_var, value='Male', bg='#d4deec')
female_radio = Radiobutton(root, text='Female', variable=sex_var, value='Female', bg='#d4deec')

male_radio.grid(row=2, column=1, sticky=W)
female_radio.grid(row=2, column=1, sticky=E)



#ADDRESS
address = Label(root, text='Address', font=('Courier', 11), bg='#d4deec')
address.grid(row=3, column=0)

address_description = Text(root, width=23, height=1)
address_description.grid(row=3, column=1, ipady=15)

#SKILLS
skills = Label(root, text='Skills', font=('Courier', 11), bg='#d4deec')
skills.grid(row=4, column=0)

skills_entry = Text(root, width=23, height=1)
skills_entry.grid(row=4, column=1, ipady=15, pady=5)


#EMAIL
email = Label(root, text='Email', font=('Courier', 11), bg='#d4deec')
email.grid(row=5, column=0)

email_entry= Entry(root,  font=('Courier', 11))
email_entry.grid(row=5, column=1, pady=5)


#PHONE
phone = Label(root, text='Phone', font=('Courier', 11), bg='#d4deec')
phone.grid(row=6, column=0)

phone_entry = Entry(root,  font=('Courier', 11))
phone_entry.grid(row=6, column=1,  pady=5)


#EXPERIENCE
experience = Label(root, text='Experience', font=('Courier', 11), bg='#d4deec')
experience.grid(row=7, column=0)

experience_entry = Text(root, width=20, height=1)
experience_entry.grid(row=7, column=1, ipadx=10, ipady=20, pady=5)


#HOBBIES
hobbies = Label(root, text='Hobbies', font=('Courier', 11), bg='#d4deec')
hobbies.grid(row=8, column=0)

selected_hobbies = []

hobbie= IntVar()
travel = Checkbutton(root, text='Travel', font=('Courier', 10), variable = hobbie, command=lambda:print_check(hobbie, 'Travel'), bg='#d4deec')
travel.grid(row=9, column=1,sticky=W)

hobbie1= IntVar()
music = Checkbutton(root, text='Music', font=('Courier', 10), variable = hobbie1, command=lambda:print_check(hobbie1, 'Music'), bg='#d4deec')
music.grid(row=10, column=1,sticky=W)

hobbie2= IntVar()
sports = Checkbutton(root, text='Sports', font=('Courier', 10), variable = hobbie2, command=lambda:print_check(hobbie2, 'Sports'), bg='#d4deec')
sports.grid(row=11, column=1,sticky=W)

hobbie3= IntVar()
reading = Checkbutton(root, text='Reading', font=('Courier', 10), variable = hobbie3, command=lambda:print_check(hobbie3, 'Reading'), bg='#d4deec')
reading.grid(row=12, column=1,sticky=W)

# REGISTER BUTTON 
register_btn = Button(root, text='Register', font=('Courier', 10), command=lambda:register())
register_btn.grid(row=13, column=1, pady=30, sticky=W)

root.mainloop()