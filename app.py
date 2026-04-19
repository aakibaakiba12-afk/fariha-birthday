import streamlit as st
import time
import random
from datetime import datetime

# 1. Setting Birthday to May 3rd
now = datetime.now()
target_year = now.year
if now.month > 5 or (now.month == 5 and now.day >= 3):
    target_year = now.year + 1
birthday_date = datetime(target_year, 5, 3, 0, 0, 0)

# Page Setup
st.set_page_config(page_title="Happy Birthday Fariha!", page_icon="🎂", layout="centered")

# 2. Countdown Logic
def get_countdown():
    diff = birthday_date - datetime.now()
    if diff.total_seconds() > 0:
        days = diff.days
        hours, remainder = divmod(diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{days}d : {hours}h : {minutes}m : {seconds}s"
    else:
        return "IT'S YOUR DAY! 🎂"

# Display Countdown
st.markdown("<h2 style='text-align: center; color: #FF69B4;'>⏳ The Big Surprise In...</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; color: #4B0082;'>{get_countdown()}</h1>", unsafe_allow_html=True)

st.write("---")

# 3. Main Birthday Header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎈 Happy Birthday, Fariha! 🎈</h1>", unsafe_allow_html=True)

# 4. The "Special" Wish Button
if st.button('Click for a Surprise! 🎁'):
    st.balloons()
    st.snow()
    st.success("ami tore sobar theke alada bhabe wish korte chaisilammmm ellegia eta banaisiiiiiiiiiiiii")

st.write("---")

# 5. The Compliment/Prank Button (Your Requested Addition)
st.header("✨ A Little Message for You")
st.write("Click the button below to see what I think of you:")

# List of compliments and your funny prank
messages = [
    "You are amazing! ✨",
    "Tui ekta kutta! 🐶",
    "You have the best laugh! 😂",
    "Tui ekটা pagol! 🤪",
    "You make everything better! 🌸"
]

if st.button('Click for a Truth! 💡'):
    msg = random.choice(messages)
    if "kutta" in msg or "pagol" in msg:
        st.error(msg) # Red box for the prank
    else:
        st.info(msg) # Blue box for compliments

st.write("---")

# 6. Candle Blow Section-
st.header("🕯️ Blow the Candle")
candle = st.checkbox("Blow! (Click here)")

if candle:
    st.markdown("<h1 style='text-align: center;'>🥳 🎂 ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Phew! Make a wish, Fariha!</h2>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align: center;'>🕯️ 🎂</h1>", unsafe_allow_html=True)

st.write("---")

# 7. Heartfelt Message
with st.expander("💌 Read my heartfelt message"):
    st.write("""
    Dear Fariha,
    Today is all about you! I built this because you deserve something as unique as you are. 
    May your year be filled with success, laughter, and endless joy. 
    Happy Birthday, Fariha! 🎂🎉✨
    """)

st.caption("Made with ❤️ by Your Best Friend")
