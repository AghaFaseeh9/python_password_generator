import streamlit as st
import random
import string


def generate_password(length, use_digits, use_special_character):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_special_character:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))


def check_password_strength(password):
    length_score = len(password) >= 12
    digit_score = any(char.isdigit() for char in password)
    special_score = any(char in string.punctuation for char in password)

    strength = sum([length_score, digit_score, special_score])

    if strength == 3:
        return "🟢 Strong"
    elif strength == 2:
        return "🟠 Medium"
    else:
        return "🔴 Weak"


st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔐 Password Generator")

length = st.slider(
    "🔢 Select the Length of Your Password", min_value=4, max_value=32, value=12
)
use_digits = st.checkbox("🔢 Include Numbers")
use_special_character = st.checkbox("🔣 Include Special Characters")

if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special_character)
    password_strength = check_password_strength(password)

    st.success(f"Generated Password: {password}")
    st.write(f"🔍 Strength: {password_strength}")

    st.code(password, language="text")
    st.button("📋 Copy to Clipboard", on_click=st.write, args=(password,))
