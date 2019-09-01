
from tkinter import *
from tkinter import messagebox
import os
import datetime
import time

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'information.txt')
bgimage_png = os.path.join(THIS_FOLDER, 'Material.png')

file = open(my_file,"r")
student_map = {}
std_list = []
counter = 0

for line in file:
    column = line.split(',')   
    student_id = column[0]
    student_name = column[1]
    student_map.update({student_id:student_name})

def put_to_list():
    # นับจำนวนคนที่มา
    global counter
    counter += 1
    count_label.config(text=counter)    #อัพเดท count_label

    # เก็บรหัสนิสิตใส่ list
    std_id = entry_field1.get()
    std_list.append(int(std_id))

    entry_field1.delete(0, 'end')       # clear entry field after button pressed

    return std_list

def sorted_list():
    return sorted(std_list)

def export_btn():

    this_time = datetime.datetime.now()
    #this_timestr = this_time.strftime('%B %d, %Y')

    #   create export txt file
    this_timestr_2 = this_time.strftime('%d_%m_%Y')
    this_timestr_2_txt = os.path.join(THIS_FOLDER, f'{this_timestr_2}.txt')

    fw = open(this_timestr_2_txt,"w")       # create the new txt file
    for item in sorted_list():
        fw.write(f'{item}\n')
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
    this_timestr = this_time.strftime('%H:%M:%S')
   
    collect_field_listbox.insert(0, f'{this_timestr} : {student_code} {std_name}\n')
    collect_field_listbox.place()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def onReturn(*args):
    return combine_funcs(phase_display(), put_to_list())

def update_clock():
    time_str = time.strftime('%H:%M:%S')
    time_label.configure(text=time_str)
    window.after(1000, update_clock)    # refresh

def update_date():
    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%d %B %Y')
    date_label.configure(text=this_timestr)
    window.after(1000, update_date)

""" ---------------------------------------------------------------------------------------------------------"""

HEIGHT = 450
WIDTH = 800

window = Tk()   # initiate gui

window.title("CPE Meeting")     # set the title

canvas = Canvas(window, height=HEIGHT, width=WIDTH)      # set the window size
canvas.pack()

window.resizable(width=False, height=False)     # fixed size window

frame = Frame(window, bg='#B2D7F2')
frame.place(relwidth=1, relheight=1)
'''
bg_image = PhotoImage(file=bgimage_png)
bg_image_label = Label(window, image=bg_image)
bg_image_label.place(relwidth=1, relheight=1)
'''
# --------- LABEL ---------
title = Label(window, text="ลงชื่อเข้าประชุม", font='EkkamaiStandard 20', fg="#0D1526", bg="#FFC1B2")
title.place(x=350,y=10)

date_label = Label(window, text="", font=18)
date_label.place(x=50, y=20)
update_date()

time_label = Label(window, text="", font=18)
time_label.place(x=50, y=50)
update_clock()

stdcode_entry_label = Label(window, text='รหัสนิสิต',font='THSarabunPSK 12')
stdcode_entry_label.place(x=320, y=72)

count_ppl_label = Label(window,text='จำนวนคนที่มา:', font='THSarabunPSK 12')
count_ppl_label.place(x=185, y=165)

count_label = Label(window, text="0", font=18)
count_label.place(x=185+100,y=165)

# --------- BUTTON ---------
SignIn_Btn = Button(text="ลงทะเบียน", bg="#40E0D0", command=combine_funcs(put_to_list,phase_display))
SignIn_Btn.place(x=435,y=110)

export_Btn = Button(text="Export student codes to text file", bg='#7FE5F0', command=export_btn)
export_Btn.place(x=320,y=400)

# --------- Entry field ---------
entry_field1 = Entry(bd=4)

entry_field1.bind("<Return>", onReturn)        # can press Enter key instead of clicking on btn1 -- Return means Enter key --

entry_field1.place(x=400, y=72)

# ---------- List Box & Scroll bar ---------
collect_field_listbox = Listbox(window, height=10, width=50, font='THSarabunPSK 12')
yscroll = Scrollbar(window, orient=VERTICAL, command=collect_field_listbox.yview)

collect_field_listbox.configure(yscrollcommand = yscroll.set)

collect_field_listbox.place(x=185, y=200)
yscroll.place(x=645, y=200, relheight=0.425)

# makes the frame appear on the screen
window.mainloop()