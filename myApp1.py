
from tkinter import *
from tkinter import messagebox
import os
import datetime
import time

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'information.txt')

file = open(my_file,"r")
student_map = {}


for line in file:
    column = line.split(',')   
    student_id = column[0]
    student_name = column[1]
    student_map.update({student_id:student_name})

def add_counter():
    global counter
    counter += 1
    count_label.config(text=counter)    #อัพเดท count_label
    return counter

def decrease_counter():
    global counter
    counter -= 1
    count_label.config(text=counter)
    return counter

def put_to_list():

    add_counter()
    # เก็บรหัสนิสิตใส่ list
    std_id = entry_field1.get()
    try:
        std_list.append(int(std_id))
    except Exception as e:
        print(e)
    else:
        print(std_list)
        entry_field1.delete(0, 'end')
        return std_list

def sorted_list():
    return sorted(list(set(std_list)))

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
    
    elif id_found is False:
        messagebox.showwarning(title='WARNING', message='ไม่พบรหัสนิสิต กรุณากรอกใหม่อีกครั้ง')
        entry_field1.delete(0, 'end')

    elif int(entry_field1.get()) in std_list:
        messagebox.showwarning(title='WARNING', message='รหัสนิสิตนี้ได้ลงทะเบียนแล้ว กรุณากรอกใหม่')
        entry_field1.delete(0, 'end')

    else:
        stdcode = entry_field1.get()
        name = student_map[stdcode]
        messagebox.showinfo(title='Information', message=f'สวัสดี {name}')
        phase_display()
        put_to_list()
        return stdcode

def studentName():
    stdcode = entry_field1.get()
    try:
        name = student_map[stdcode]
    except Exception as e:
        print(e)
    else:
        return name

def phase_display():
    student_code = int(entry_field1.get())
    std_name = studentName()

    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%H:%M:%S')
   
    collect_field_listbox.insert(END, f'{this_timestr} : {student_code} {std_name}')
    collect_field_listbox.place()

def delete_listbox():
    MsgMox = messagebox.askokcancel(title='!!!', message='คุณต้องการลบชื่อที่เลือกใช่หรือไม่')
    if MsgMox is True:
        
        selected_std = collect_field_listbox.curselection()
        selected_std = int(selected_std[0])
        collect_field_listbox.delete(selected_std)

        print(f"delete at index {selected_std}")
        std_list.pop(selected_std)
        print(std_list)
        decrease_counter()
    else:
        pass
    
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def onReturn(*args):
    return phase_generator()

def update_clock():
    time_str = time.strftime('%H:%M:%S')
    time_label.configure(text=time_str)
    window.after(1000, update_clock)    # refresh

def update_date():
    this_time = datetime.datetime.now()
    this_timestr = this_time.strftime('%d %B %Y')
    date_label.configure(text=this_timestr)
    window.after(1000, update_date)

def Result(*args):
    return search_Button()

def search_Button():
    entry_get = search_entry.get()
    if int(entry_get) in std_list:
        s_result_label.config(text='รหัสนิสิตนี้ได้ลงทะเบียนแล้ว', fg='green')
        s_entry_label.config(text=entry_get, fg='green')
    else:
        s_result_label.config(text='รหัสนิสิตนี้ยังไม่ได้ลงทะเบียน', fg='red')
        s_entry_label.config(text=entry_get, fg='red')
    search_entry.delete(0, 'end')

def on_mousewheel(*args):
    return collect_field_listbox.yview

""" ---------------------------------------------------------------------------------------------------------"""
std_list = []
counter = 0

HEIGHT = 450
WIDTH = 800

window = Tk()   # initiate gui

window.title("CPE Meeting")     # set the title

canvas = Canvas(window, height=HEIGHT, width=WIDTH)      # set the window size
canvas.pack()

window.resizable(width=False, height=False)     # fixed size window

frame = Frame(window, bg='#B2D7F2')
frame.place(relwidth=1, relheight=1)

# --------- LABEL ---------
title = Label(window, text="Sign-In", font='EkkamaiStandard 20 bold', fg="#0D1526", bg='#B2D7F2')
title.place(x=350,y=15)

date_label = Label(window, text="", font=18, bg='#B2D7F2')
date_label.place(x=50, y=20)
update_date()

time_label = Label(window, text="", font=18, bg='#B2D7F2')
time_label.place(x=50, y=50)
update_clock()

stdcode_entry_label = Label(window, text='รหัสนิสิต',font='THSarabunPSK 12', bg='#B2D7F2')
stdcode_entry_label.place(x=290, y=72)

count_ppl_label = Label(window,text='จำนวนคนที่มา', font='THSarabunPSK 12', bg='#B2D7F2')
count_ppl_label.place(x=185, y=165)

count_label = Label(window, text="0", font=18, bg='#B2D7F2')
count_label.place(x=185+100,y=165)

search_label = Label(window, text='ค้นหารหัสนิสิตที่ลงทะเบียนแล้ว', font='THSarabunPSK 12', bg='#B2D7F2')
search_label.place(x=600,y=10)

s_entry_label = Label(window, text='', font='THSarabunPSK 12', bg='#B2D7F2', fg='red')
s_entry_label.place(x=655, y=110)

s_result_label = Label(window, text='', font='THSarabunPSK 12', bg='#B2D7F2')
s_result_label.place(x=615,y=130)

# --------- BUTTON ---------
SignIn_Btn = Button(text="ลงทะเบียน", bg="#40E0D0", command=phase_generator)
SignIn_Btn.place(x=405,y=110)

search_Btn = Button(text='Search', command=search_Button)
search_Btn.place(x=668, y=75)

delete_Btn = Button(text='Delete', bg='#950028', fg='white', command=delete_listbox)
delete_Btn.place(x=670, y=200)

export_Btn = Button(text="Export student codes to text file", bg='#7FE5F0', command=export_btn)
export_Btn.place(x=320,y=400)

# --------- Entry field ---------
entry_field1 = Entry(bd=4)
entry_field1.bind("<Return>", onReturn)        # can press Enter key instead of clicking on btn1 -- Return means Enter key --
entry_field1.place(x=370, y=72)

search_entry = Entry(bd=4)
search_entry.bind("<Return>", Result)
search_entry.place(x=625,y=40)

# ---------- List Box & Scroll bar ---------
collect_field_listbox = Listbox(window, height=10, width=50, font='THSarabunPSK 12')
yscroll = Scrollbar(window, orient=VERTICAL, command=collect_field_listbox.yview)

collect_field_listbox.configure(yscrollcommand = yscroll.set)

yscroll.bind("<MouseWheel>", on_mousewheel)

collect_field_listbox.place(x=185, y=200)
yscroll.place(x=645, y=200, relheight=0.425)

# makes the frame appear on the screen
window.mainloop()