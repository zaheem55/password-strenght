import streamlit as st
import re

st.set_page_config("Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate Password Strength Checker! 👋
Use this simple tool to check the strength of your password and get suggestions on How to make it stronger. 
            we  will give you helpful tips to create a **Strong Password** 🔐 """)

password = st.text_input("Enter your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌Password Should be at least 8 characters long.")
        
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lower case characters")

    if re.search(r'/d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")

    if re.search(r'[!@#$%&]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%&).")
    if score == 4:
        feedback.append("✅Your Passwod is strong!")
    elif score == 3:
        feedback.append("🟡Your Password is medium streagth. it could be stroger")
    else:
        feedback.append("🔴Your Password is weak. please make a stronger.")

    if feedback:
        st.markdown("## Improvments Suggestion")
        for tip in feedback:
            st.write(tip)
else:
    st.info("please enter your password to get started.")