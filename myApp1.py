
from tkinter import *
from tkinter import messagebox
import os
import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'information.txt')
result_txt = os.path.join(THIS_FOLDER, 'result.txt')

file = open(my_file,"r")
student_map = {}
std_list = []

for line in file:
    column = line.split(',')   
    student_id = column[0]
    student_name = column[1]
    student_map.update({student_id:student_name})

def retrieve_input():
    inputValue = collecct_stdcode_field.get("1.0","end-1c")
    return inputValue

def export_btn():
    stdList = []
    stdList.append(retrieve_input())
    stdList.sort()

    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%B %d, %Y')

    fw = open(result_txt,"w")
    for item in stdList:
        fw.write(f'{this_timestr}\n{item}')
    fw.close()

    export_btn_display()

def export_btn_display():
    messagebox.showinfo(title="Information", message="Export ไฟล์เรียบร้อย")

def phase_generator():

    if len(entry_field1.get()) == 0:
        messagebox.showwarning(title='WARNING', message='กรุณาพิมพ์รหัสนิสิต')

    stdcode = entry_field1.get()
    name = student_map[stdcode]

    messagebox.showinfo(title='Information', message=f'สวัสดี {name}')
    return stdcode

def studentName():
    stdcode = entry_field1.get()
    name = student_map[stdcode]
    return name

def phase_display():
    student_code = phase_generator()
    std_name = studentName()

    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%B %d, %Y %H:%M:%S')

    text_field.insert('1.0', f'({this_timestr}): {std_name}\n')
    text_field.place()

    collecct_stdcode_field.insert('1.0', f'{student_code}\n')
    collecct_stdcode_field.place()

    entry_field1.delete(0, 'end')       # clear entry field after button pressed


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

window = Tk()   # initiate gui

window.title("Meeting")     # set the title

window.geometry("800x450")      # set the window size
window.resizable(width=False, height=False)     # fixed size window

# --------- LABEL ---------
title = Label(text="ลงทะเบียนประชุม", font=30, fg="#0D1526", bg="#FFC1B2")
title.place(x=320,y=10)

stdcodelabel = Label(text='รหัสนิสิต',font=18)
stdcodelabel.place(x=300, y=70)

label1 = Label(text='รหัสนิสิต', font=18)
label1.place(x=598, y=165)

# --------- BUTTON ---------
btn1 = Button(text="ลงทะเบียน", bg="#40E0D0", command=combine_funcs(phase_display, retrieve_input))
btn1.place(x=435,y=120)

btn2 = Button(text="Export student codes to text file", bg='#7FE5F0', command=export_btn)
btn2.place(x=320,y=380)

# --------- Entry field ---------
entry_field1 = Entry(bd=4)
entry_field1.place(x=400, y=72)


# --------- Text field ---------
text_field = Text(master=window, height=10, width=60)
text_field.place(x=100,y=200)

collecct_stdcode_field = Text(master=window, height=10, width=8)
collecct_stdcode_field.place(x=600,y=200)


# makes the frame appear on the screen
window.mainloop()