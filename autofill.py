# import csv
# from fpdf import FPDF
# import os

# def read_csv_data(csv_path):
#     with open(csv_path, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         data = [row for row in reader]
#     return data

# def save_to_pdf(student_data):
#     class PDF(FPDF):
#         def header(self):
#             self.set_font('Arial', 'B', 12)
#             self.cell(0, 10, 'Registration Form', 0, 1, 'C')

#         def footer(self):
#             self.set_y(-15)
#             self.set_font('Arial', 'I', 8)
#             self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

#     pdf = PDF()
#     pdf.add_page()
#     pdf.set_font('Arial', '', 12)

#     for key, value in student_data.items():
#         pdf.cell(0, 10, f'{key}: {value}', 0, 1)

#     pdf_output_path = os.path.join("processed", f"{student_data['Full_Name']}_registration.pdf")
#     pdf.output(pdf_output_path)

#     return pdf_output_path


from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from pymongo import MongoClient

def save_to_pdf(student_data):
    file_path = f"processed/{student_data['Full_Name']}_registration.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    
    # Logo and title
    c.drawImage("uploads/image.png", 50, height - 100, width=100, height=50)  
    c.setFont("Helvetica-Bold", 24)
    c.drawString(200, height - 70, "Registration Form")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 90, "NAST COLLEGE")

    # Personal Information
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 130, "Personal Information")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 150, f"Full Name: {student_data.get('Full_Name', '')}")
    c.drawString(50, height - 170, f"Address: {student_data.get('City', '')}")
    c.drawString(50, height - 190, f"Date of Birth: {student_data.get('Date_of_Birth', '')}")
    c.drawString(50, height - 210, f"Previous School Name: {student_data.get('School_Name', '')}")

    # Education Status
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 240, "Education Status")
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 260, f"SEE Exam Year: {student_data.get('Exam_Year', '')}")
    c.drawString(50, height - 280, f"Symbol No: {student_data.get('Symbol_No', '')}")
    c.drawString(50, height - 300, f"Year of Completion: {student_data.get('Date_of_Issue', '')}")
    c.drawString(50, height - 320, f"Grade Point Average (GPA): {student_data.get('GPA', '')}")

    # Subjects and Grades
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 350, "Subjects and Grades")
    c.setFont("Helvetica", 12)
    subjects = ["Nepali", "English", "Maths", "Science", "Social", "Opt_I_Mathematics", "Opt_II_Science"]
    y = height - 370
    for subject in subjects:
        grade = student_data.get(subject, '')
        c.drawString(50, y, f"{subject}: {grade}")
        y -= 20

    c.save()
    return file_path

def read_csv_data(csv_path):
    import csv
    data = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def save_to_database(student_data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["college_registration"]
    collection = db["students"]
    
    symbol_no = student_data.get("Symbol_No")
    existing_student = collection.find_one({"Symbol_No": symbol_no})
    
    if existing_student:
        collection.update_one({"Symbol_No": symbol_no}, {"$set": student_data})
    else:
        collection.insert_one(student_data)

def update_student_data(student_data):
    save_to_database(student_data)
