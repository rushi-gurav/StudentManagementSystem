from tkinter import *
from tkinter import messagebox
import sqlite3

def update_student_window(parent):
	def update_data():
		roll_no = roll_entry.get()
		name = name_entry.get()
		mark1 = mark1_entry.get()
		mark2 = mark2_entry.get()
		mark3 = mark3_entry.get()

		if not roll_no or not name or not mark1 or not mark2 or not mark3:
			messagebox.showerror("Error", "All fields are required!")
			return

		try:
			conn = sqlite3.connect("student_management.db")
			cursor = conn.cursor()
			cursor.execute(
				"UPDATE students SET name=?, sub_mark1=?, sub_mark2=?, sub_mark3=? WHERE roll_no=?",
				(name, int(mark1), int(mark2), int(mark3), int(roll_no)),
			)
			conn.commit()
			conn.close()

			if cursor.rowcount == 0:
				messagebox.showerror("Error", "Roll number not found!")
			else:
				messagebox.showinfo("Success", "Student updated successfully!")
				update_window.destroy()
		except ValueError:
			messagebox.showerror("Error", "Invalid data type!")

	update_window = Toplevel(parent)
	update_window.title("Update Student")
	update_window.geometry("400x400+420+350")

	f = ("Arial", 10, "bold")

	Label(update_window, text="Update Student", font=("Arial", 20, "bold")).pack(pady=10)

	Label(update_window, text="Roll No:", font=f).place(x=50, y=80)
	roll_entry = Entry(update_window, font=f)
	roll_entry.place(x=200, y=80)

	Label(update_window, text="Name:", font=f).place(x=50, y=130)
	name_entry = Entry(update_window, font=f)
	name_entry.place(x=200, y=130)

	Label(update_window, text="Subject Mark 1:", font=f).place(x=50, y=180)
	mark1_entry = Entry(update_window, font=f)
	mark1_entry.place(x=210, y=180)

	Label(update_window, text="Subject Mark 2:", font=f).place(x=50, y=230)
	mark2_entry = Entry(update_window, font=f)
	mark2_entry.place(x=210, y=230)

	Label(update_window, text="Subject Mark 3:", font=f).place(x=50, y=280)
	mark3_entry = Entry(update_window, font=f)
	mark3_entry.place(x=210, y=280)

	Button(update_window, text="Update", font=f, command=update_data).place(x=100, y=340)
	Button(update_window, text="Back", font=f, command=update_window.destroy).place(x=250, y=340)
