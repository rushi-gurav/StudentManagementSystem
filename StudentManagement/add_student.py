from tkinter import *
from tkinter import messagebox
import sqlite3

def add_student_window(parent):
	def save_data():
		roll_no = roll_entry.get()
		name = name_entry.get()
		mark1 = mark1_entry.get()
		mark2 = mark2_entry.get()
		mark3 = mark3_entry.get()

		if not roll_no or not name or not mark1 or not mark2 or not mark3:
			messagebox.showerror("Error", "All fields are required!")
			return

		if not roll_no.isdigit():
			messagebox.showerror("Error", "Roll number must be a numeric value!")
			return

		if not name.isalpha():
			messagebox.showerror("Error", "Name must contain only alphabetic characters!")
			return

		if not (mark1.isdigit() and mark2.isdigit() and mark3.isdigit()):
			messagebox.showerror("Error", "Marks should be numeric values!")
			return

		if not (0 <= int(mark1) < 100 and 0 <= int(mark2) < 100 and 0 <= int(mark3) < 100):
			messagebox.showerror("Error", "Marks should be less than 100!")
			return

		try:
			conn = sqlite3.connect("student_management.db")
			cursor = conn.cursor()
			cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)",
						   (int(roll_no), name, int(mark1), int(mark2), int(mark3)))
			conn.commit()
			conn.close()
			messagebox.showinfo("Success", "Student added successfully!")
			add_window.destroy()
		except sqlite3.IntegrityError:
			messagebox.showerror("Error", "Roll number already exists!")
		except ValueError:
			messagebox.showerror("Error", "Invalid data type!")

	add_window = Toplevel(parent)
	add_window.title("Add Student")
	add_window.geometry("400x400+10+350")

	f = ("Arial", 10, "bold")

	Label(add_window, text="Add Student", font=("Arial", 20, "bold")).pack(pady=10)

	Label(add_window, text="Roll No:", font=f).place(x=50, y=80)
	roll_entry = Entry(add_window, font=f)
	roll_entry.place(x=200, y=80)

	Label(add_window, text="Name:", font=f).place(x=50, y=130)
	name_entry = Entry(add_window, font=f)
	name_entry.place(x=200, y=130)

	Label(add_window, text="Subject Mark 1:", font=f).place(x=50, y=180)
	mark1_entry = Entry(add_window, font=f)
	mark1_entry.place(x=200, y=180)

	Label(add_window, text="Subject Mark 2:", font=f).place(x=50, y=230)
	mark2_entry = Entry(add_window, font=f)
	mark2_entry.place(x=200, y=230)

	Label(add_window, text="Subject Mark 3:", font=f).place(x=50, y=280)
	mark3_entry = Entry(add_window, font=f)
	mark3_entry.place(x=200, y=280)

	Button(add_window, text="Save", font=f, command=save_data).place(x=100, y=340)
	Button(add_window, text="Back", font=f, command=add_window.destroy).place(x=250, y=340)
