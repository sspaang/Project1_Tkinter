
from tkinter import *
from tkinter import messagebox
import os
import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'information.txt')
result_txt = os.path.join(THIS_FOLDER, 'result.txt')
bgimage_png = os.path.join(THIS_FOLDER, 'Material.png')

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

    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%B %d, %Y')

    #   create export txt file
    this_timestr_2 = this_time.strftime('%d_%m_%Y')
    this_timestr_2_txt = os.path.join(THIS_FOLDER, f'{this_timestr_2}.txt')

    fw = open(this_timestr_2_txt,"w")       # create the new txt file
    for item in stdList:
        fw.write(f'{this_timestr}\n{item}')
    fw.close()

    export_btn_display()

def export_btn_display():
    messagebox.showinfo(title="Information", message="Export ไฟล์เรียบร้อย")

def phase_generator():
    id_found = entry_field1.get() in student_map        # return True and False

    if len(entry_field1.get()) == 0:
        messagebox.showwarning(title='WARNING', message='กรุณาพิมพ์รหัสนิสิต')
    
    elif id_found == False:
        messagebox.showwarning(title='WARNING', message='ไม่พบรหัสนิสิต กรุณากรอกใหม่อีกครั้ง')
        entry_field1.delete(0, 'end')
    else:
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

    text_field.configure(state='normal')
    text_field.insert('1.0', f'({this_timestr}): {std_name}\n')
    text_field.place()
    text_field.configure(state='disable')   # disable to type anything into text box

    collecct_stdcode_field.configure(state='normal')
    collecct_stdcode_field.insert('1.0', f'{student_code}\n')
    collecct_stdcode_field.place()
    collecct_stdcode_field.configure(state='disable')

    entry_field1.delete(0, 'end')       # clear entry field after button pressed

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


HEIGHT = 450
WIDTH = 800

window = Tk()   # initiate gui

window.title("Meeting")     # set the title

canvas = Canvas(window, height=HEIGHT, width=WIDTH)      # set the window size
canvas.pack()
window.resizable(width=False, height=False)     # fixed size window

frame = Frame(window, bg='blue')
frame.place(relwidth=1, relheight=1)

bg_image = PhotoImage(file=bgimage_png)
bg_image_label = Label(window, image=bg_image)
bg_image_label.place(relwidth=1, relheight=1)

# --------- LABEL ---------
title = Label(text="Meeting Sign-In", font='times 20', fg="#0D1526", bg="#FFC1B2")
title.place(x=330,y=10)

stdcodelabel = Label(text='รหัสนิสิต',font=18)
stdcodelabel.place(x=300, y=70)

label1 = Label(text='รหัสนิสิต', font=18)
label1.place(x=598, y=165)

# --------- BUTTON ---------
btn1 = Button(text="ลงทะเบียน", bg="#40E0D0", command=combine_funcs(phase_display, retrieve_input))
btn1.place(x=435,y=120)

btn1.invoke()       # can press Enter key instead of clicking on btn1
window.bind('<Return>', lambda event=None: btn1.invoke())

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