from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title('Registration Form')
root.geometry('650x850')
root.configure(bg='#d4deec')



def register():
	stud_name = entry.get()
	stud_age = age_var.get()
	stud_sex = sex_var.get()
	stud_course = course_var.get()
	stud_year = year_var.get()
	stud_subjects = selected_course

	message = f'Registration sucessful, {stud_name}, {stud_age}, yrs old, {stud_sex}, {stud_course}, {stud_year}, from IT department'
	messagebox.showinfo("Registration Success", message)

def test_print(any_var):
    print(any_var)

label = Label(root, text='Registration Form', justify='center', font=('Courier',15), bg='#d4deec')
label.grid(columnspan=10, pady=40)

# NAME
name =Label(root, text='Name:', justify='center', font=('Courier', 15), bg='#d4deec')
name.grid(row=2, column=0, ipadx=15, padx=5)

entry = Entry(root, justify='center', font=('Courier', 15))
entry.grid(row=2, column=1, ipadx=50, ipady=5, sticky=W)

# AGE
age = Label(root, text='Age:', font=('Courier', 15), bg='#d4deec')
age.grid(row=3, column=0, pady=10)

age_var = StringVar()
age_list = [11, 12, 13, 14, 15, 16, 17, 18 ,19, 20, 21]
age_combo = ttk.Combobox(root, values = age_list, textvariable = age_var, font=('Courier', 15))
age_combo.grid(row=3, column=1, ipadx=10, ipady=5, pady=15, sticky=W)

# SEX
sex = Label(root, text='Sex:', font=('Courier', 15), bg='#d4deec')
sex.grid(row=4, column=0)

sex_var = StringVar()
male_radio = Radiobutton(root, text='Male', variable = sex_var, value='Male', font=('Courier', 15), bg='#d4deec')
male_radio.grid(row=4, column=1, sticky=W)

female_radio = Radiobutton(root, text='Female', variable = sex_var, value='Female', font=('Courier', 15), bg='#d4deec')
female_radio.grid(row=5, column=1, sticky=W)


#SUBJECT
def print_check(checker, cb):
	print('you just clicked', cb)
	print(checker.get())

selected_course = []

subject = Label(root, text='Subject:', font=('Courier', 15), bg='#d4deec')
subject.grid(row=6, column=0)

course1= StringVar()
subject1 = Checkbutton(root, text='Programming', font=('Courier', 13), variable = course1, command=lambda:print_check(course1, 'Programming'), bg='#d4deec')
subject1.grid(row=6, column=1,sticky=W, ipady=5)

course2= StringVar()
subject2 = Checkbutton(root, text='Physics', font=('Courier', 13), variable = course2, command=lambda:print_check(course2, 'Physics'), bg='#d4deec')
subject2.grid(row=6, column=1,sticky=E)

course3= StringVar()
subject3 = Checkbutton(root, text='Data Analytics', font=('Courier', 13), variable = course3, command=lambda:print_check(course3, 'Data Analytics'), bg='#d4deec')
subject3.grid(row=7, column=1,  sticky=W)

course4= StringVar()
subject4 = Checkbutton(root, text='Calculus', font=('Courier', 13), variable = course4, command=lambda:print_check(course4, 'Calculus'), bg='#d4deec')
subject4.grid(row=7, column=1, pady=10, sticky=E)

course5= StringVar()
subject5 = Checkbutton(root, text='Data Visualization', font=('Courier', 12), variable = course5, command=lambda:print_check(course5, 'Data Visualization'), bg='#d4deec')
subject5.grid(row=8, column=1, sticky=W)

course6= StringVar()
subject6 = Checkbutton(root, text='Physical E', font=('Courier', 12), variable = course6, command=lambda:print_check(course6, 'Physical Education'), bg='#d4deec')
subject6.grid(row=8, column=1, pady=10, sticky=E)




# COURSE
course = Label(root, text='Course:', font=('Courier', 15), bg='#d4deec')
course.grid(row=9, column=0)

course_var = StringVar()
course_list = ['BSIT', 'BSE', 'BSA', 'BSAIS', 'BTVTED']
course_combo = ttk.Combobox(root, width=22, font=('Courier', 13), value=course_list, textvariable = course_var)
course_combo.grid(row=9, column=1, ipadx = 50, ipady = 5, pady=15, sticky=W)


# YEAR
year = Label(root, text='Year:', font=('Courier', 15), bg='#d4deec')
year.grid(row=10, column=0)

year_var = StringVar()
year_list = ['First Year', 'Second Year', 'Third Year', 'Fourth Year']
year_combo = ttk.Combobox(root, values = year_list, textvariable = year_var, font=('Courier', 15))
year_combo.grid(row=10, column=1, ipadx=40, pady=10, ipady=5, sticky=W)



# DESCRIPTION
description = Label(root, text='Description: ', font=('Courier', 15), bg='#d4deec')
description.grid(row=11, column=0, padx=15)

description_entry = Entry(root, font=('Courier', 15))
description_entry.grid(row=11, column=1, ipadx=50, ipady=80, pady=15, sticky=W)


register_btn = Button(root, text='Register', font=('Courier', 15), command=lambda:register())
register_btn.grid(row=12, column=1, pady=30, sticky=W)

root.mainloop()