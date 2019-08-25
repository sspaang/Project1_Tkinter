import tkinter as tk

window = tk.Tk()
window.title("Greetings")
window.geometry("300x400")

label1 = tk.Label(text="Hello ______")
label1.grid(column=0, row=0)

label2 = tk.Label(text="Thanks to join the meeting!")
label2.grid(column=0, row=1)

window.mainloop()