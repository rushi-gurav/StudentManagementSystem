from tkinter import *
from add_student import add_student_window
from view_students import view_students_window
from update_student import update_student_window
from delete_student import delete_student_window
from database import setup_db

setup_db()

root = Tk()
root.title("S.M.S")
root.geometry("500x300+400+30")

f = ("Arial", 10, "bold")

lab_header = Label(root, text="Student Management System By Rushi", font=f)
lab_header.pack(pady=20)

btn_add = Button(root, text="Add Student", font=f, command=lambda: add_student_window(root), width=20)
btn_add.pack(pady=10)

btn_view = Button(root, text="View Students", font=f, command=view_students_window, width=20)
btn_view.pack(pady=10)

btn_update = Button(root, text="Update Student", font=f, command=lambda: update_student_window(root), width=20)
btn_update.pack(pady=10)

btn_delete = Button(root, text="Delete Student", font=f, command=lambda: delete_student_window(root), width=20)
btn_delete.pack(pady=10)

root.mainloop()
