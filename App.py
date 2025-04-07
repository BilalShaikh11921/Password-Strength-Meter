import streamlit as st
import re
import random
import string

# Password Strength Criterea
# ✅ Be at least 8 characters long
# ✅ Contain uppercase & lowercase letters
# ✅ Include at least one digit (0-9)
# ✅ Have one special character (!@#$%^&*)

def pass_generator():
    lowerD = string.ascii_lowercase
    uppeD = string.ascii_uppercase
    digitD = string.digits
    symbolsD = string.punctuation
    combine = lowerD + uppeD + digitD + symbolsD
    x = random.sample(combine, 8)
    new_pass = "".join(x)
    return new_pass

st.set_page_config(page_title="Password Strength Meter", page_icon= "")

st.title("Password Strength Meter")

password = st.text_input("Enter your password", type="password")

score = 0

feedback = []

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Password should be at least 8 characters long")
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else: 
        feedback.append("⚠️ Password should contain both upper and lowercase characters")
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least 1 digit")
    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("⚠️ Password should contain at least 1 special character (!@#$%&*).")
    if score == 4:
        feedback.append("✅ Your password is strong.")
    elif score == 3:
        feedback.append("🟡 Your password is moderate. It could be stronger.")
        st.markdown("Suggested Password for you: " + pass_generator())
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")
        st.markdown("Suggested Password for you: " + pass_generator())
    if feedback:
        st.markdown("## Improvement Suggestions!")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password")
