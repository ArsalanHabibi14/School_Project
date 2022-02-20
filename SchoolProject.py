import sqlite3
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


# ============================ DataBase Works =======================
class CRUD:
    @classmethod
    def Create(cls, Facultiy, Name, FatherName, ID):
        connection = sqlite3.connect("./Student.db")
        cur = connection.cursor()
        cur.execute(f"INSERT INTO {Facultiy} VALUES(?,?,?);", (ID, Name, FatherName))

        connection.commit()
        connection.close()

    @classmethod
    def Update(cls, Facultiy, Name, FatherName, ID):
        connection = sqlite3.connect("./Student.db")
        cur = connection.cursor()
        cur.execute(
            f"UPDATE {Facultiy} SET id = {ID} , Name = '{Name}' , Father = '{FatherName}' WHERE id = {ID} OR Name = '{Name}';")

        connection.commit()
        connection.close()

    @classmethod
    def Delete(cls, Facultiy, id, Name):
        connection = sqlite3.connect("./Student.db")
        cur = connection.cursor()
        cur.execute(f"DELETE FROM {Facultiy} WHERE id = ? OR Name = ?;", (id, Name))

        connection.commit()
        connection.close()


# ================================== Tkinter Works ==========================
root = Tk()

root.geometry("500x400")
TabControll = ttk.Notebook(root)


# =================================== Create Tab ========================
class Tab1:
    def __init__(self):
        self.tab1 = ttk.Frame(TabControll)
        TabControll.add(self.tab1, text="اصلی")

        # ===================== Functions ===================
        def Add_commnad():

            if self.Number.get() == 1:
                CRUD.Create("Electricity", self.e1.get(), self.e2.get(), self.e3.get())
            elif self.Number.get() == 2:
                CRUD.Create("Building", self.e1.get(), self.e2.get(), self.e3.get())
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)

        # ===================== Labels and Entries ===================
        self.e1 = Entry(self.tab1)
        self.e1.place(x=260, y=20)

        self.l1 = Label(self.tab1, text=": نام ")
        self.l1.place(x=400, y=20)

        self.e2 = Entry(self.tab1)
        self.e2.place(x=260, y=60)

        self.l2 = Label(self.tab1, text=": نام پدر")
        self.l2.place(x=400, y=60)

        self.e3 = Entry(self.tab1)
        self.e3.place(x=260, y=100)

        self.l3 = Label(self.tab1, text=": آی دی نمبر ")
        self.l3.place(x=400, y=100)

        # =========================== Buttons ======================
        self.Number = IntVar()

        self.rb1 = Radiobutton(self.tab1, text="برق ", variable=self.Number, value=1)
        self.rb1.place(x=170, y=20)

        self.rb2 = Radiobutton(self.tab1, text="ساختمان ", variable=self.Number, value=2)
        self.rb2.place(x=170, y=60)

        self.btn = Button(self.tab1, text="اضافه", command=Add_commnad)
        self.btn.place(x=170, y=100)

        self.btn.configure(bg='#A4A4A4')


openTab1 = Tab1()


# ================================= Search Tab =====================
class Tab2:
    def __init__(self):
        self.tab2 = ttk.Frame(TabControll)
        TabControll.add(self.tab2, text="جستجو")

        # ================== Functions =====================
        def fill_list(book):
            for s in book:
                self.list1.insert(END, s)

        def Search_command():
            self.list1.delete(0, END)
            connection = sqlite3.connect("./Student.db")
            cur = connection.cursor()
            if self.Number.get() == 1:
                sql = """
                    SELECT * FROM Electricity WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            elif self.Number.get() == 2:
                sql = """
                    SELECT * FROM Building WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            connection.commit()
            connection.close()

        # ================== Entries and Labels =====================
        self.e1 = Entry(self.tab2)
        self.e1.place(x=260, y=20)

        self.l1 = Label(self.tab2, text=": نام ")
        self.l1.place(x=400, y=20)

        self.e2 = Entry(self.tab2)
        self.e2.place(x=260, y=60)

        self.l2 = Label(self.tab2, text=": آی دی نمبر")
        self.l2.place(x=400, y=60)

        self.l3 = Label(self.tab2, text="آی دی نمبر")
        self.l3.place(x=160, y=30)

        self.l4 = Label(self.tab2, text="نام")
        self.l4.place(x=100, y=30)

        self.l5 = Label(self.tab2, text="نام پدر")
        self.l5.place(x=20, y=30)

        self.list1 = Listbox(self.tab2, width=35, y=10)
        self.list1.place(x=10, y=50)

        self.Number = IntVar()
        self.rb1 = Radiobutton(self.tab2, text="برق", variable=self.Number, value=1)
        self.rb1.place(x=320, y=100)

        self.rb1 = Radiobutton(self.tab2, text="ساختمان", variable=self.Number, value=2)
        self.rb1.place(x=320, y=140)

        self.btn1 = Button(self.tab2, text="جستجو", command=Search_command)
        self.btn1.place(x=260, y=100)

        self.btn1.configure(bg='#A4A4A4')


openTab2 = Tab2()


# ========================= Third Tab ==========================
class Tab3:
    def __init__(self):
        # ================== Functions =====================

        def fill_list(book):
            for s in book:
                self.list1.insert(END, s)

        def get_selected_row(event):
            global selected
            if len(self.list1.curselection()) > 0:
                index = self.list1.curselection()[0]
                selected = self.list1.get(index)

        def Update():
            window = Tk()
            window.geometry("400x300")

            try:
                def MainUpdate():
                    if self.Number.get() == 1:
                        CRUD.Update("Electricity", self.newe.get(), self.newe2.get(), self.newe3.get())
                    elif self.Number.get() == 2:
                        CRUD.Update("Building", self.newe.get(), self.newe2.get(), self.newe3.get())
                    Search_command()
                    self.newe.delete(0, END)
                    self.newe2.delete(0, END)
                    self.newe3.delete(0, END)

                    self.newe.insert(END, selected[1])
                    self.newe2.insert(END, selected[2])
                    self.newe3.insert(END, selected[0])

                    window.destroy()

                self.newl = Label(window, text=": نام")
                self.newl.place(x=290, y=10)

                self.newe = Entry(window)
                self.newe.place(x=150, y=10)
                self.newe.insert(END, selected[1])

                self.newl2 = Label(window, text=": نام پدر")
                self.newl2.place(x=290, y=90)

                self.newe2 = Entry(window)
                self.newe2.place(x=150, y=90)
                self.newe2.insert(END, selected[2])

                self.newl3 = Label(window, text=": آی دی نمبر")
                self.newl3.place(x=290, y=170)

                self.newe3 = Entry(window)
                self.newe3.place(x=150, y=170)
                self.newe3.insert(END, selected[0])

                self.newbtn = Button(window, text="آپدیت", command=MainUpdate)
                self.newbtn.place(x=160, y=240)
                self.newbtn.configure(bg='#A4A4A4')
            except:
                window.destroy()
                tkinter.messagebox.showwarning("None Value",
                                               "You should select a student that time you can update it ")
            window.mainloop()

        def Search_command():
            self.list1.delete(0, END)
            connection = sqlite3.connect("./Student.db")
            cur = connection.cursor()
            if self.Number.get() == 1:
                sql = """
                    SELECT * FROM Electricity WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            elif self.Number.get() == 2:
                sql = """
                    SELECT * FROM Building WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            connection.commit()
            connection.close()

        # ================== Entries and Labels =====================
        self.tab3 = ttk.Frame(TabControll)
        TabControll.add(self.tab3, text="آپدیت")

        self.e1 = Entry(self.tab3)
        self.e1.place(x=260, y=20)

        self.l1 = Label(self.tab3, text=": نام ")
        self.l1.place(x=400, y=20)

        self.e2 = Entry(self.tab3)
        self.e2.place(x=260, y=60)

        self.l2 = Label(self.tab3, text=": آی دی نمبر")
        self.l2.place(x=400, y=60)

        self.l3 = Label(self.tab3, text="آی دی نمبر")
        self.l3.place(x=160, y=30)

        self.l4 = Label(self.tab3, text="نام")
        self.l4.place(x=100, y=30)

        self.l5 = Label(self.tab3, text="نام پدر")
        self.l5.place(x=20, y=30)

        self.list1 = Listbox(self.tab3, width=35, y=10)
        self.list1.place(x=10, y=50)
        self.list1.bind("<<ListboxSelect>>", get_selected_row)

        self.Number = IntVar()
        self.rb1 = Radiobutton(self.tab3, text="برق", variable=self.Number, value=1)
        self.rb1.place(x=320, y=100)

        self.rb1 = Radiobutton(self.tab3, text="ساختمان", variable=self.Number, value=2)
        self.rb1.place(x=320, y=140)

        self.btn1 = Button(self.tab3, text="جستجو", command=Search_command)
        self.btn1.place(x=260, y=100)

        self.btn1.configure(bg='#A4A4A4')
        self.btn2 = Button(self.tab3, text="آپدیت", command=Update)
        self.btn2.place(x=260, y=150)
        self.btn2.configure(bg='#A4A4A4')


openTab3 = Tab3()


# ========================================= Second Tab ================
class Tab4:
    def __init__(self):
        self.tab4 = ttk.Frame(TabControll)
        TabControll.add(self.tab4, text="حذف")

        # ======================= Functions ===================

        def fill_list(book):
            for s in book:
                self.list1.insert(END, s)

        def get_selected_row(event):
            global selected
            if len(self.list1.curselection()) > 0:
                index = self.list1.curselection()[0]
                selected = self.list1.get(index)

        def Search_command():
            self.list1.delete(0, END)
            connection = sqlite3.connect("./Student.db")
            cur = connection.cursor()
            if self.Number.get() == 1:
                sql = """
                    SELECT * FROM Electricity WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            elif self.Number.get() == 2:
                sql = """
                    SELECT * FROM Building WHERE id = ? OR Name = ?
                """
                cur.execute(sql, (self.e2.get(), self.e1.get()))
                fill_list(cur)
            connection.commit()
            connection.close()

        def Delete():
            if self.Number.get() == 1:
                CRUD.Delete("Electricity", selected[0], selected[1])
            elif self.Number.get() == 2:
                CRUD.Delete("Building", selected[0], selected[1])
            self.list1.delete(0, END)

        # ================== Entries and Labels =====================
        self.e1 = Entry(self.tab4)
        self.e1.place(x=260, y=20)

        self.l1 = Label(self.tab4, text=": نام ")
        self.l1.place(x=400, y=20)

        self.e2 = Entry(self.tab4)
        self.e2.place(x=260, y=60)

        self.l2 = Label(self.tab4, text=": آی دی نمبر")
        self.l2.place(x=400, y=60)

        self.l3 = Label(self.tab4, text="آی دی نمبر")
        self.l3.place(x=160, y=30)

        self.l4 = Label(self.tab4, text="نام")
        self.l4.place(x=100, y=30)

        self.l5 = Label(self.tab4, text="نام پدر")
        self.l5.place(x=20, y=30)

        self.list1 = Listbox(self.tab4, width=35, y=10)
        self.list1.place(x=10, y=50)
        self.list1.bind("<<ListboxSelect>>", get_selected_row)

        self.Number = IntVar()
        self.rb1 = Radiobutton(self.tab4, text="برق", variable=self.Number, value=1)
        self.rb1.place(x=320, y=100)

        self.rb1 = Radiobutton(self.tab4, text="ساختمان", variable=self.Number, value=2)
        self.rb1.place(x=320, y=140)

        self.btn1 = Button(self.tab4, text="جستجو", command=Search_command)
        self.btn1.place(x=260, y=100)
        self.btn1.configure(bg='#A4A4A4')

        self.btn2 = Button(self.tab4, text="حذف", command=Delete)
        self.btn2.place(x=260, y=150)
        self.btn2.configure(bg='#A4A4A4')


openTab4 = Tab4()

TabControll.pack(expand=1, fill="both")

root.mainloop()
