'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Trip Program
Version 1 .0
This is my trip program
The user can input their country, description, month, and transport for their vacation.
They can then save this and view info about the program
'''

# Ammaar Siddiqui
# Advanced Computer Programming
# 10/16/18

from tkinter import *
from tkinter import ttk


class App():
    def __init__(self, root, *args):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_all)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.close_window)
        menubar.add_cascade(label="File", menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about_top)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)

        content = Frame(root)
        self.country_label = Label(content, text="Country")
        self.lbox = Listbox(content, height=10, exportselection=FALSE)
        for c in ['Australia', 'The Bahamas', 'Barbados', 'Belgium', 'Belize', 'Brazil', 'Cambodia', 'Cameroon',
                  'Chile', 'Costa Rica', 'Denamrk', 'Ecuador', 'Egypt', 'Fiji', 'France', 'Germany', 'Guatemala',
                  'Haiti', 'Honduras', 'Japan', 'Laos', 'Madagascar', 'Mexico', 'Morocco', 'New Zealand', 'Peru',
                  'Spain', 'Switzerland', 'Turkey', 'United States', 'United Kingdom', 'Vatican City']:
            self.lbox.insert(END, c)
        self.scroll = ttk.Scrollbar(content, orient=VERTICAL, command=self.lbox.yview)
        self.lbox.configure(yscrollcommand=self.scroll.set)
        self.descrip_label = Label(content, text="Description")
        self.descrip_box = Text(content, width=10, height=10, wrap=WORD)
        self.month_label = Label(content, text="Month")
        self.month_spin = Spinbox(content, textvariable=month,
                                  values=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                          'September', 'October', 'November', 'December'], state='readonly', wrap=True)
        self.travel_label = Label(content, text="Travel Type")
        self.travel_cbox = ttk.Combobox(content, values=['Air', 'Train', 'Car', 'Bus'], textvariable=travel,
                                        state='readonly')
        travel.set("Method of Travel")
        self.travel_cbox.bind('<FocusIn>', self.defocus)
        self.error_label = Label(content, text="")

        grip_frame = Frame(root)
        self.grip = ttk.Sizegrip(grip_frame).grid(column=999, row=999, sticky='nsew')
        self.submit = Button(content, text="Submit", command=self.save_all)
        self.clear = Button(content, text="Clear", command=self.clear_all)
        grip_frame.grid(column=999, row=999)
        content.grid(column=0, row=0)
        self.country_label.grid(column=0, row=0)
        self.lbox.grid(column=0, row=1, rowspan=5)
        self.scroll.grid(column=1, row=1, rowspan=5, sticky='ns', padx=(0, 20))
        self.descrip_label.grid(column=2, row=0, padx=(0, 20))
        self.descrip_box.grid(column=2, row=1, rowspan=5, padx=(0, 20))
        self.travel_label.grid(column=3, row=0)
        self.travel_cbox.grid(column=3, row=1)
        self.month_label.grid(column=3, row=2)
        self.month_spin.grid(column=3, row=3)
        self.submit.grid(column=3, row=4)
        self.clear.grid(column=3, row=5)
        self.error_label.grid(column=3, row=6)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        grip_frame.columnconfigure(999, weight=1)
        grip_frame.rowconfigure(999, weight=1)

        root.protocol("WM_DELETE_WINDOW", self.close_window)

    def about_top(self):
        explain = Toplevel(root)
        explain.title("About Program")
        explain.geometry("300x100")
        explain.resizable(width=False, height=False)
        about_label = Label(explain, text=("Trip Program" + "\n" + "Version 1.0" + "\n" + "Ammaar Siddiqui"))
        about_label.pack()
        button = Button(explain, text="Close", command=explain.destroy)
        button.pack()


    def close_window(self):
        confirm = Toplevel(root)
        confirm.title("Confirm Close")
        confirm.geometry("300x100")
        confirm.resizable(width=False, height=False)
        explain_label = Label(confirm, text="Are you sure you want to exit")
        explain_label.pack()
        spacer_label2 = Label(confirm, text="")
        spacer_label2.pack()
        button_frame = Frame(confirm)
        button_frame.pack()
        yes = Button(button_frame, text="Yes", command=root.destroy)
        yes.pack(side=LEFT)
        spacer_label3 = Label(button_frame, text="")
        spacer_label3.pack(side=LEFT)
        no = Button(button_frame, text="No", command=confirm.destroy)
        no.pack(side=LEFT)

    def clear_all(self):
        travel.set('Method of Travel')
        self.lbox.bind(self.lbox.selection_clear(0, END))
        self.descrip_box.delete("1.0", END)
        month.set("January")
        self.error_label.config(text="")

    def defocus(self, event):
        event.widget.master.focus_set()

    def save_all(self):
        check=True
        self.error_label.config(text="")
        values = [self.lbox.get(idx) for idx in self.lbox.curselection()]
        travel_type = travel.get()
        input = self.descrip_box.get("1.0", END)
        input = input.replace("\n", "*")
        input=input.replace(" ", "^")
        for x in input:
            if x!="*" and x!="^":
                check=False
        if values == [] or travel_type == "Method of Travel" or check:
            self.error_label.config(text="Error")
        else:
            file = open("trip_details.txt", "a")
            file.write(values[0] + "|||" + travel_type + "|||" + month.get() + "|||" + input + "\n")
            file.close()
            travel.set('Method of Travel')
            self.lbox.bind(self.lbox.selection_clear(0, END))
            self.descrip_box.delete("1.0", END)
            month.set("January")
            self.error_label.config(text="Successfully Saved")


root = Tk()
descrip = StringVar()
travel = StringVar()
month = StringVar()
descrip = StringVar()
app = App(root, month, travel, descrip)
root.title("Travel Log")
root.geometry("450x250")
root.minsize(450, 250)
root.mainloop()
root.destroy()