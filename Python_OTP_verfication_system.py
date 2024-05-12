import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def otp_generator():
    global otp
    otp = ''.join([str(random.randint(0,9)) for _ in range(6)])

def otp_sender():
    otp_generator()
    email = email_entry.get()   #receiver's email address taken from user 
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 #587 — this is the port for encrypted email transmissions using SMTP Secure (SMTPS)
    sender_email = 'youremailhere.com'
    sender_password = 'your password here'  #enter normal email password or app password

    #Email details
    subject = 'OTP Verification'
    message = 'Test OTP: '+str(otp)

    #MIME(Multipurpose Internet Mail Extensions) text
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain')) #create a MIMEText object 

    #Connect to SMTP server and send the mail
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() #upgrade to a secure communication using TLS mode.
    server.login(sender_email, sender_password)
    try:
        server.sendmail(sender_email, email, msg.as_string()) #add try catch block for invalid email addresses
    except: 
        tk.messagebox.showerror("Error", "Invalid email address. Please enter a valid email address")

def otp_validator():
    entered_otp = entry.get()
    if len(entered_otp) != 6 or not entered_otp.isdigit(): #checking for a 6 digit OTP
        tk.messagebox.showerror("Error", "Please enter a valid 6-digit OTP.")
    else:
        if entered_otp == otp:
            tk.messagebox.showinfo("Success", "OTP matched! Access granted.")
        else:
            tk.messagebox.showerror("Error", "Incorrect OTP. Access denied.")

#clear function to clear the text box
def clear():
    entry.delete(0, tk.END)

#Create the main OTP verification window
root = tk.Tk()
root.title("OTP Generation System")
root.geometry("400x200")
root.resizable(False,False)
Mail_label = tk.Label(root, text="Enter the email id:")
email_entry = tk.Entry(root, width=20)
generate_button = tk.Button(root, text="Generate OTP", command=otp_sender)
validate_button = tk.Button(root, text="Validate OTP", command=otp_validator)
clear_button = tk.Button(root, text="Clear", command=clear)
entry = tk.Entry(root, width=20)
otp_label = tk.Label(root, text="Enter the otp:")

# Place widgets on the window
Mail_label.grid(row=0, column=0, padx=10, pady=10)
generate_button.grid(row=2, column=0, padx=10, pady=10)
otp_label.grid(row=1, column=0, padx=10, pady=10)
entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
validate_button.grid(row=2, column=1, padx=10, pady=10)
clear_button.grid(row=2, column=2, padx=10, pady=10)
email_entry.grid(row=0, column=1, padx=10, pady=10)

#default value for global otp variable
otp = ''.join([str(random.randint(0,9)) for _ in range(6)])
root.mainloop()