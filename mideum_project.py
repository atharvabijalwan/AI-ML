import tkinter as tk
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DB_FILE = "student_records.csv"

#  ATHARVA BIJALWAN (B5): filter logic
def get_filtered_data(name, subject=None):
    if not os.path.isfile(DB_FILE):
        return None
    
    df = pd.read_csv(DB_FILE)
    # Filter by Name (Case-insensitive)
    student_df = df[df['Student'].str.contains(name, case=False, na=False)]
    
    if student_df.empty:
        return None
    
    # If a subject is specified, filter further
    if subject and subject.strip() != "":
        student_df = student_df[student_df['Subject'].str.contains(subject, case=False, na=False)]
    
    return student_df


def generate_visuals():
    name = ent_name.get().strip()
    subject = ent_subject.get().strip()

    if not name:
        messagebox.showwarning("Input Error", "Please enter a Student Name to analyze!")
        return

    data = get_filtered_data(name, subject)

    if data is None or data.empty:
        messagebox.showerror("Not Found", f"No records found for '{name}'" + (f" in '{subject}'" if subject else ""))
        return

    plt.figure(figsize=(10, 6))

    if subject:
        # case  A: Specific Subject Trend (Line Graph)
        marks = np.array(data['Marks'])
        plt.plot(marks, marker='o', color='darkorange', linewidth=3, label=f"{subject} Trend")
        plt.title(f"Improvement Trend for {name} in {subject}", fontsize=14)
        plt.ylabel("Marks")
        plt.xlabel("Attempts / Tests")
        plt.grid(True, linestyle='--', alpha=0.6)
    else:
        # case B: All Subjects Overview (Bar Chart)
        # We group by subject in case there are multiple entries for the same subject
        avg_data = data.groupby('Subject')['Marks'].mean()
        subjects = avg_data.index
        marks = avg_data.values
        
        colors = plt.cm.Paired(np.linspace(0, 1, len(subjects)))
        plt.bar(subjects, marks, color=colors, edgecolor='black')
        plt.title(f"Academic Overview: {name}", fontsize=14)
        plt.ylabel("Average Marks")
        plt.xlabel("Subjects")

    plt.tight_layout()
    plt.show()


def save_entry():
    name, subj, mrks = ent_name.get(), ent_subject.get(), ent_marks.get()
    if not (name and subj and mrks):
        messagebox.showwarning("Error", "Fill Name, Subject, and Marks to save!")
        return
    try:
        new_row = pd.DataFrame([[name, subj, float(mrks)]], columns=['Student', 'Subject', 'Marks'])
        header = not os.path.isfile(DB_FILE)
        new_row.to_csv(DB_FILE, mode='a', index=False, header=header)
        messagebox.showinfo("Success", f"Data for {name} saved!")
    except: 
        messagebox.showerror("Error", "Marks must be a number")

root = tk.Tk()
root.title("Advanced Student Analyzer")
root.geometry("450x500")

tk.Label(root, text="STUDENT ANALYTICS SYSTEM", font=('Arial', 14, 'bold')).pack(pady=20)

tk.Label(root, text="Search/Input Name:").pack()
ent_name = tk.Entry(root, width=30); ent_name.pack(pady=5)

tk.Label(root, text="Subject :").pack()
ent_subject = tk.Entry(root, width=30); ent_subject.pack(pady=5)

tk.Label(root, text="Marks :").pack()
ent_marks = tk.Entry(root, width=30); ent_marks.pack(pady=5)

tk.Button(root, text="SAVE NEW RECORD", command=save_entry, bg="#4CAF50", fg="white", width=25).pack(pady=15)
tk.Button(root, text="ANALYZE STUDENT", command=generate_visuals, bg="#2196F3", fg="white", width=25).pack()

tk.Label(root, text="Note: Input Name + Subject for Improvement Line Graph\nInput Name only for Subject Bar Chart", font=('Arial', 8), fg="gray").pack(pady=20)

root.mainloop()