from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3

def view_students_window():
	view_window = Toplevel()
	view_window.title("View Students")
	view_window.geometry("370x400+825+350")

	f = ("Arial", 15, "bold")

	Label(view_window, text="View Students", font=f).pack(pady=10)

	text_area = ScrolledText(view_window, width=30, height=10, font=("Arial", 12), wrap="word")
	text_area.pack(padx=10, pady=10)

	conn = sqlite3.connect("student_management.db")
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM students")
	rows = cursor.fetchall()
	conn.close()

	if rows:
		for row in rows:
			text_area.insert(END, f"Roll No: {row[0]}, Name: {row[1]}, Marks: [{row[2]}, {row[3]}, {row[4]}]\n")
	else:
		text_area.insert(END, "No student records found.")

	text_area.config(state="disabled")

	Button(view_window, text="Back", font=f, command=view_window.destroy).pack(pady=10)
