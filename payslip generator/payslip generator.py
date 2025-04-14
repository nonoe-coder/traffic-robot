import pandas as pd
import smtplib
from fpdf import FPDF
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

data = {
    "Employee ID": ["001", "002", "003", "004", "005"],
    "Name": ["Nomsa Sibanda", "Welma Kayanga", "Tafadzwa Kanhohodza", "Kirsty Matyukira", "Lorraine Thom"],
    "Email": ["snomsa2301@gmail.com", "welmakayanga7@gmail.com", "kanhohodza5369@gmail.com", "kirstyservie03@gmail.com", "lorrainethom93@gmail.com"],
    "Basic Salary": [400, 400, 400, 400, 400],
    "Allowances": [150, 80, 58, 92, 68],
    "Taxi Deduction": [20, 22, 25, 20, 18],
    "NSSA Deduction": [18, 18, 20, 18, 19],
    "Bank Acount": [1234567890, 9876543210, 1234567890, 1234567890, 1234567890],
}


df = pd.DataFrame(data)

sender_email = "starlisy7@gmail.com"
sender_password = "eoji olom dxjn duuc" 


for index, row in df.iterrows():
    employee_id = row['Employee ID']
    name = row['Name']
    email = row['Email']
    basic_salary = row['Basic Salary']
    allowances = row['Allowances']
    taxi_deduction = row['Taxi Deduction']
    nssa_deduction = row['NSSA Deduction']
    bank_account = row['Bank Acount']

   
    net_salary = basic_salary + allowances - taxi_deduction - nssa_deduction

    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Payslip", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Employee ID: {employee_id}", ln=True)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Bank Account: {bank_account}", ln=True)
    pdf.cell(200, 10, txt=f"Basic Salary: ${basic_salary}", ln=True)
    pdf.cell(200, 10, txt=f"Allowances: ${allowances}", ln=True)
    pdf.cell(200, 10, txt=f"Taxi Deduction: ${taxi_deduction}", ln=True)
    pdf.cell(200, 10, txt=f"NSSA Deduction: ${nssa_deduction}", ln=True)
    pdf.cell(200, 10, txt=f"Net Salary: ${net_salary}", ln=True)

   
    pdf_filename = f"Payslip_{employee_id}.pdf"
    pdf.output(pdf_filename)

   
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = f"Payslip for {name}"

   
    body = f"""
    Dear {name},

    Please find attached your payslip for this month.

    Best regards,
One Century 
    """
    msg.attach(MIMEText(body, 'plain'))

    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
        msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        print(f"Email sent to {email} with payslip attached.")
    except Exception as e:
        print(f"Failed to send email to {email}. Error: {e}")

   
    print(f"Payslip sent to {name} ({email})")
    print("Enjoy your day!")