import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        feedback.append("✅ Strong Password!")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")

    return feedback

def generate_strong_password():
    import random
    import string
    # Generate a random password with 12 characters, including uppercase, lowercase, digits, and special characters
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit App
st.title("Password Strength Meter 🔒")

# Input field for password
password = st.text_input("Enter your password:", type="password")

# Check password strength
if password:
    feedback = check_password_strength(password)
    for message in feedback:
        st.write(message)

# Password Generator
st.write("---")
st.subheader("Need a strong password?")
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.write(f"🔐 Your strong password: `{strong_password}`")

# Blacklist common passwords
common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
if password.lower() in common_passwords:
    st.error("⚠️ This password is too common and insecure. Please choose a stronger one.")
