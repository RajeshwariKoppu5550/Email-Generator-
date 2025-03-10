import google.generativeai as genai
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Initialize Gemini API with API Key
api_key = "AIzaSyCM8q3l-l0_2EZEQjNn9OZL13VCL867Bws"  # Store securely in environment variables
genai.configure(api_key=api_key)

class MLBackend:
    def __init__(self):
        """Initialize Gemini API model"""
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

    def generate_email(self, user_prompt="Write me a professional email"):
        """Generate an email using Gemini AI"""
        try:
            response = self.model.generate_content(user_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating email: {str(e)}"

    def send_email(self, to_email, subject, body):
        """Send an email using SMTP (Gmail)"""
        sender_email = "prashanthpathigari@gmail.com"  # Replace with your email
        sender_password = "kkmi qsmc abyi waau"  # Use an app password or SMTP password
        
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            server.quit()
            return "Email sent successfully!"
        except Exception as e:
            return f"Failed to send email: {str(e)}"
