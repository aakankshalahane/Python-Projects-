import smtplib

sender = "your email"
password = "password"
receiver = input("Receiver email: ")
msg = "Subject: Hello from Python\n\nThis is an automated email."

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
print("Email sent successfully!")
