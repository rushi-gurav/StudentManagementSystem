from tkinter import *
from tkinter import messagebox
import sqlite3

def delete_student_window(parent):
    def delete_data():
        roll_no = ent_roll.get()

        if not roll_no:
            messagebox.showerror("Error", "Roll number is required!")
            return

        conn = sqlite3.connect("student_management.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE roll_no=?", (int(roll_no),))
        conn.commit()
        conn.close()

        if cursor.rowcount == 0:
            messagebox.showerror("Error", "Roll number not found!")
        else:
            messagebox.showinfo("Success", "Student deleted successfully!")
            delete_window.destroy()

    delete_window = Toplevel(parent)
    delete_window.title("Delete Student")
    delete_window.geometry("300x400+1190+350")

    f = ("Arial", 16, "bold")

    lab_header = Label(delete_window, text="Delete Student", font=("Arial", 10, "bold"))
    lab_header.pack(pady=20)

    lab_roll = Label(delete_window, text="Enter Roll No:", font=f)
    lab_roll.pack(pady=10)

    ent_roll = Entry(delete_window, font=f)
    ent_roll.pack(pady=10)

    btn_delete = Button(delete_window, text="Delete", font=f, command=delete_data)
    btn_delete.pack(pady=10)

    btn_back = Button(delete_window, text="Back", font=f, command=delete_window.destroy)
    btn_back.pack(pady=5)
