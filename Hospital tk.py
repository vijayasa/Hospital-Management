import tkinter as tk
from tkinter import ttk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("700x550")
root.configure(bg="#f2f2f2")

# ---------------- STYLE ----------------
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 10), padding=6)
style.configure("Header.TLabel", font=("Arial", 18, "bold"))

# ---------------- MAIN FRAME ----------------
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky="nsew")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# ---------------- HEADER ----------------
header = ttk.Label(
    main_frame,
    text="Hospital Management System",
    style="Header.TLabel"
)
header.grid(row=0, column=0, columnspan=4, pady=15)

# ---------------- FORM FRAME ----------------
form_frame = ttk.Frame(main_frame, padding=10)
form_frame.grid(row=1, column=0, columnspan=4, sticky="w")

ttk.Label(form_frame, text="Patient ID").grid(row=0, column=0, sticky="w", pady=5)
entry_id = ttk.Entry(form_frame, width=25)
entry_id.grid(row=0, column=1, pady=5, padx=10)

ttk.Label(form_frame, text="Patient Name").grid(row=1, column=0, sticky="w", pady=5)
entry_name = ttk.Entry(form_frame, width=25)
entry_name.grid(row=1, column=1, pady=5, padx=10)

ttk.Label(form_frame, text="Age").grid(row=2, column=0, sticky="w", pady=5)
entry_age = ttk.Entry(form_frame, width=25)
entry_age.grid(row=2, column=1, pady=5, padx=10)

ttk.Label(form_frame, text="Disease").grid(row=3, column=0, sticky="w", pady=5)
entry_disease = ttk.Entry(form_frame, width=25)
entry_disease.grid(row=3, column=1, pady=5, padx=10)

# ---------------- BUTTON FRAME ----------------
button_frame = ttk.Frame(main_frame, padding=10)
button_frame.grid(row=2, column=0, columnspan=4)

# ---------------- STATUS LABEL ----------------
status = tk.StringVar()
status.set("Ready")

status_label = ttk.Label(
    main_frame,
    textvariable=status,
    foreground="blue"
)
status_label.grid(row=4, column=0, columnspan=4, pady=10)

# ---------------- OUTPUT AREA ----------------
output = tk.Text(
    main_frame,
    height=12,
    width=80,
    borderwidth=1,
    relief="solid"
)
output.grid(row=3, column=0, columnspan=4, pady=10)

# ---------------- FUNCTION LOGIC ----------------
patients = []   # temporary storage (list of dictionaries)

def add_patient():
    pid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    disease = entry_disease.get()

    if not pid or not name or not age or not disease:
        status.set("Error: All fields are required")
        return

    for p in patients:
        if p["id"] == pid:
            status.set("Error: Patient ID already exists")
            return

    patients.append({
        "id": pid,
        "name": name,
        "age": age,
        "disease": disease
    })

    status.set("Patient registered successfully")
    clear_entries()

def view_patients():
    output.delete("1.0", tk.END)

    if not patients:
        output.insert(tk.END, "No patient records found\n")
        return

    output.insert(tk.END, "ID\tName\tAge\tDisease\n")
    output.insert(tk.END, "-"*50 + "\n")

    for p in patients:
        output.insert(
            tk.END,
            f"{p['id']}\t{p['name']}\t{p['age']}\t{p['disease']}\n"
        )

    status.set("Displayed all patient records")

def search_patient():
    pid = entry_id.get()
    output.delete("1.0", tk.END)

    for p in patients:
        if p["id"] == pid:
            output.insert(tk.END, f"Patient ID : {p['id']}\n")
            output.insert(tk.END, f"Name       : {p['name']}\n")
            output.insert(tk.END, f"Age        : {p['age']}\n")
            output.insert(tk.END, f"Disease    : {p['disease']}\n")
            status.set("Patient found")
            return

    status.set("Patient not found")

def delete_patient():
    pid = entry_id.get()

    for p in patients:
        if p["id"] == pid:
            patients.remove(p)
            output.delete("1.0", tk.END)
            status.set("Patient record deleted")
            return

    status.set("Patient not found")

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_disease.delete(0, tk.END)

# ---------------- BUTTONS ----------------
ttk.Button(button_frame, text="Add Patient", command=add_patient)\
    .grid(row=0, column=0, padx=6)

ttk.Button(button_frame, text="View Patients", command=view_patients)\
    .grid(row=0, column=1, padx=6)

ttk.Button(button_frame, text="Search Patient", command=search_patient)\
    .grid(row=0, column=2, padx=6)

ttk.Button(button_frame, text="Delete Patient", command=delete_patient)\
    .grid(row=0, column=3, padx=6)

ttk.Button(button_frame, text="Clear", command=clear_entries)\
    .grid(row=0, column=4, padx=6)

# ---------------- RUN APP ----------------
root.mainloop()