import streamlit as st
import google.generativeai as genai
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configure Gemini API
API_KEY = "AIzaSyC9jiFO8kV33gYyE7GzpxrFcu1EFrwsAR0"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Set Streamlit page config
st.set_page_config(page_title="AI Email Generator", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body, .stApp {
            background: linear-gradient(to right, #1c1c3c, #3a1c3c);
            color: white;
        }
        .title-text{
            text-align: center;
        }
        .stButton > button {
            background-color: #ff6600 !important;
            color: white !important;
            font-size: 18px !important;
            padding: 10px !important;
            border-radius: 10px !important;
            margin-top: 20px !important;
        }
        .stButton > button:hover {
            background-color: #ff4500 !important;
        }
        .feature-block, .feature-item {
            padding: 20px;
            border-radius: 15px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 3px 3px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
            color: white;
        }
        .start-button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .feature-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-bottom: 20px;
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(to right, #1c1c3c, #3a1c3c);
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.markdown("<h1 class='title-text'>📩 AI-Powered Email Personalization</h1>", unsafe_allow_html=True)
st.markdown("<h5 class='title-text'>Transform your email communication with AI. Create perfectly personalized emails in seconds.</h5>", unsafe_allow_html=True)

# Features Section
st.markdown(
    """
    <div class="feature-grid">
        <div class="feature-item">
            <h3>🚀 AI-Powered Automation</h3>
            <p>Generate professional emails instantly with advanced AI algorithms.</p>
        </div>
        <div class="feature-item">
            <h3>📩 Personalized Email Suggestions</h3>
            <p>Get AI-generated emails tailored to your specific needs.</p>
        </div>
        <div class="feature-item">
            <h3>⚡ Instant Delivery</h3>
            <p>Send emails directly from our platform with just one click.</p>
        </div>
        <div class="feature-item">
            <h3>🎨 User-Friendly Interface</h3>
            <p>Our easy-to-use platform ensures a seamless experience.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Feature Block for "Get Started" Button
st.markdown(
    """
    <div class="feature-block" style="margin-bottom: 20px;">
        <h3>🚀 Get Started</h3>
        <p>Click below to begin generating AI-powered emails instantly.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar State Management
if "show_sidebar" not in st.session_state:
    st.session_state["show_sidebar"] = False

# "Get Started" Button
st.markdown('<div class="start-button-container">', unsafe_allow_html=True)
if st.button("🚀 Get Started"):
    st.session_state["show_sidebar"] = True
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar Form (Only visible after clicking "Get Started")
if st.session_state["show_sidebar"]:
    with st.sidebar:
        st.header("📝 Generate Your Email")
        emails = st.text_area("Recipient Emails (comma-separated)", key="emails_input")
        sendermail = st.text_input("Your Name", key="sender_name_input")
        prompt = st.text_area("Describe the Email Content", key="email_content_input")  # Unique key added

        if st.button("✨ Generate Email"):
            with st.spinner("⏳ Generating Email..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-pro-latest")
                    response = model.generate_content(
                        f"Write a professional email from {sendermail} to multiple recipients about: {prompt}"
                    )
                    st.session_state['generated_email'] = response.text.strip()
                except Exception as e:
                    st.session_state['generated_email'] = f"❌ Error: {str(e)}"

# Email Sending Function
# Email Sending Function
def sendmail(content, receiver_emails):
    sender_email = "prashanthpathigari@gmail.com"  # Replace with your email
    sender_password = "osbs bxuf izct ehsa"  # Replace with your Gmail App Password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)  # Correctly setting multiple recipients
    msg['Subject'] = "AI-Generated Email"
    msg.attach(MIMEText(content, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        
        server.sendmail(sender_email, receiver_emails, msg.as_string())  # Send to all recipients at once

        server.quit()
        st.success("✅ Emails sent successfully!")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# Send Email Button Logic
if 'generated_email' in st.session_state:
    st.markdown("## 📩 Generated Email:")
    st.code(st.session_state['generated_email'], language="text")

    if st.button("📧 Send Email"):
        email_list = [email.strip() for email in emails.split(",") if email.strip()]
        sendmail(st.session_state['generated_email'], email_list)
