import pandas as pd
from fpdf import FPDF
import smtplib
from email.message import EmailMessage
import os

EMAIL_ADDRESS = "snomsa2301@gmail.com"
EMAIL_PASSWORD = "reignmusimhi0524"

# Load Excel file
try:
    df = pd.read_excel('payslip employees.xlsx', header=0)  # Ensure the first row is treated as header
    print("Excel file loaded successfully.")
except Exception as e:
    print(f"Error loading Excel file: {e}")
    exit(1)

# Print original column names to check for issues
print("Original columns:", df.columns)

# Clean the column names (strip spaces and lowercase them)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Cleaned columns:", df.columns)

# Check for missing data
required_columns = ['first_name', 'last_name', 'email', 'position', 'basic_salary', 'allowances', 'deductions']
missing_data = df[required_columns].isnull().any(axis=1)

if missing_data.any():
    print("Warning: There are missing values in the data.")
    print(df[missing_data])

# Ensure numeric columns are properly converted
df['basic_salary'] = pd.to_numeric(df['basic_salary'], errors='coerce')
df['allowances'] = pd.to_numeric(df['allowances'], errors='coerce')
df['deductions'] = pd.to_numeric(df['deductions'], errors='coerce')

# Generate PDF
def create_payslip(emp):
    try:
        net_salary = emp["basic_salary"] + emp["allowances"] - emp["deductions"]
        filename = f"{emp['first_name']}_Payslip.pdf"

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, f"Payslip for {emp['first_name']} {emp['last_name']}", ln=True)
        pdf.cell(200, 10, f"Pay Period: {emp['pay_period']}", ln=True)
        pdf.cell(200, 10, f"Position: {emp['position']}", ln=True)
        pdf.cell(200, 10, f"Basic Salary: ${emp['basic_salary']}", ln=True)
        pdf.cell(200, 10, f"Allowances: ${emp['allowances']}", ln=True)
        pdf.cell(200, 10, f"Deductions: ${emp['deductions']}", ln=True)
        pdf.cell(200, 10, f"Net Salary: ${net_salary}", ln=True)

        pdf.output(filename)
        print(f"PDF Created: {filename}")
        return filename
    except Exception as e:
        print(f"Error creating payslip for {emp['first_name']}: {e}")
        return None

# Send Email
def send_email(emp, filename):
    try:
        if not filename:
            print("No file to send")
            return
        msg = EmailMessage()
        msg["Subject"] = "Your Payslip"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = emp["email"]
        msg.set_content(f"Hello {emp['first_name']},\n\nAttached is your payslip for {emp['pay_period']}.")

        with open(filename, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=filename)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"Sent email to {emp['email']}")
    except Exception as e:
        print(f"Error sending email to {emp['email']}: {e}")

# Process each employee
for _, emp in df.iterrows():
    payslip_file = create_payslip(emp)
    if payslip_file:
        send_email(emp, payslip_file)
        os.remove(payslip_file)  # optional, delete PDF after sending email
        print(f"Sent payslip to {emp['email']}")
    else:
        print(f"Failed to create payslip for {emp['first_name']}")
