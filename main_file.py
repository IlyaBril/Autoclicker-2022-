from tkinter import *
from tkinter import ttk
from Log_Read import execute
from write_to_file import write_to, stop, start

root = Tk()
root.title("Автоматизатор")
#root.rowconfigure(0, minsize=150, weight=1)
#root.columnconfigure(0, minsize=300, weight=1)

menu = Menu(root)
new_item = Menu(menu)  
new_item.add_command(label='Новый')  
new_item.add_separator()  
new_item.add_command(label='Изменить')  
menu.add_cascade(label='Файл', menu=new_item)  


main_frame = ttk.Frame(root).grid()


content = ttk.Frame(main_frame, borderwidth=3, relief="ridge", width=200, height=100)
content.grid(column=1, row=0, columnspan=3, rowspan=5, sticky=(N))

Button_Start = ttk.Button(main_frame, text="Start", command=execute).grid(column=0, row=0)
Button_Record = ttk.Button(main_frame, text="Record", command=start).grid(column=0, row=1)
Button_Stop = ttk.Button(main_frame, text="Stop", command=stop).grid(column=0, row=2, sticky=(E,W))
#Button_Edit = ttk.Button(main_frame, text="Edit", command=root.destroy).grid(column=0, row=3, sticky=(E,W))
Button_Exit = ttk.Button(main_frame, text="Exit", command=root.destroy).grid(column=0, row=4, sticky=(E,W))

root.config(menu=menu)
root.mainloop()



