import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox, simpledialog

def send_emails(sender_email, sender_password, subject, message, recipients):
    """
    Sends an email to multiple recipients with the provided subject and message.
    """
    smtp_server = "smtp.gmail.com"
    port = 465  # For SSL

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Log in to the server
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            
            for recipient in recipients:
                # Create the email
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = recipient
                msg["Subject"] = subject
                msg.attach(MIMEText(message, "plain"))

                # Send the email
                try:
                    server.sendmail(sender_email, recipient, msg.as_string())
                    print(f"Email sent to {recipient}")
                except Exception as e:
                    print(f"Failed to send email to {recipient}: {e}")
                    messagebox.showerror("Error", f"Failed to send email to {recipient}: {e}")
            messagebox.showinfo("Success", "Emails sent successfully!")
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Authentication Error", "Failed to log in. Check your email and password.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def on_send_button():
    """
    Callback for the send button to collect input and send emails.
    """
    sender_email = email_entry.get()
    sender_password = password_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    recipients = recipients_entry.get().split(",")

    if not sender_email or not sender_password or not recipients:
        messagebox.showerror("Input Error", "Please fill out all required fields.")
        return

    send_emails(sender_email, sender_password, subject, message, recipients)

# Set up the GUI
root = tk.Tk()
root.title("Email Sender")

tk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Subject:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
subject_entry = tk.Entry(root, width=30)
subject_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Message:").grid(row=3, column=0, padx=10, pady=5, sticky="ne")
message_text = tk.Text(root, height=10, width=30)
message_text.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Recipients (comma-separated):").grid(row=4, column=0, padx=10, pady=5, sticky="e")
recipients_entry = tk.Entry(root, width=30)
recipients_entry.grid(row=4, column=1, padx=10, pady=5)

send_button = tk.Button(root, text="Send Emails", command=on_send_button)
send_button.grid(row=5, column=1, pady=10)

root.mainloop()
