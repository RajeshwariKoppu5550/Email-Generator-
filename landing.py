import streamlit as st
import base64

# Function to add custom CSS for 3D effect
def add_custom_css():
    st.markdown(
        """
        <style>
        .card {
            width: 300px;
            height: 400px;
            background: linear-gradient(135deg, #f3f3f3, #e0e0e0);
            border-radius: 15px;
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
            transition: transform 0.2s;
            text-align: center;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        .card:hover {
            transform: perspective(1000px) rotateY(10deg) rotateX(10deg);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Display the 3D Card
def display_3d_card():
    st.markdown(
        """
        <div class="card">
            <h2>Make things float in air</h2>
            <p>Hover over this card to unleash the power of CSS perspective.</p>
            <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&auto=format&fit=crop" width="250" style="border-radius: 10px;"/>
            <br><br>
            <button style="padding: 10px; background: black; color: white; border: none; border-radius: 5px;">Try Now →</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Streamlit App
def main():
    st.title("AI Email Generator - 3D Card Demo")
    add_custom_css()
    display_3d_card()
    
    # Add input section for email generation
    st.subheader("Generate an AI-powered Email")
    email_type = st.selectbox("Select email type", ["Professional", "Casual", "Apology", "Invitation"])
    recipient = st.text_input("Recipient Name")
    email_content = st.text_area("Message")

    if st.button("Generate Email"):
        st.success(f"Generated Email:\n\nDear {recipient},\n\n{email_content}\n\nBest Regards,")

if __name__ == "__main__":
    main()
