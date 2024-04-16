import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def generate_pdf(data):
    pdf_filename = "student_registration.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    
    # Define table data
    table_data = [["Field", "Value"]]
    for field, value in data.items():
        table_data.append([field, value])
    
    # Define table style
    table_style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                               ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                               ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                               ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
                               ('BOTTOMPADDING', (0,0), (-1,0), 12),
                               ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                               ('GRID', (0,0), (-1,-1), 1, colors.black)])
    
    # Create table
    student_table = Table(table_data)
    student_table.setStyle(table_style)
    
    # Build PDF document
    doc.build([student_table])
    
    messagebox.showinfo("PDF Generated", f"PDF saved as {pdf_filename}")

def submit_form():
    data = {
        "Name": name_entry.get(),
        "Age": age_entry.get(),
        "Grade": grade_entry.get()
        # Add more fields here as needed
    }
    
    # Validate data
    if not all(data.values()):
        messagebox.showerror("Error", "All fields are required.")
        return
    
    # Additional data validation (e.g., age as numeric)
    try:
        int(data["Age"])
    except ValueError:
        messagebox.showerror("Error", "Age must be a numeric value.")
        return
    
    # Generate PDF
    generate_pdf(data)

# Create GUI window
root = tk.Tk()
root.title("Student Registration Form")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Grade:").grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Entry fields
name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
grade_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)
grade_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
