import time
import streamlit as st


def show_progress(duration=3, width=20):
    progress_bar = st.progress(0)
    for i in range(width + 1):
        percent = int((i / width) * 100)
        progress_bar.progress(percent)
        time.sleep(duration / width)


def get_zodiac(month, day):
    month = month.lower()
    if (month == "december" and day >= 22) or (month == "january" and day <= 19):
        return "Capricorn"
    elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
        return "Aquarius"
    elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
        return "Pisces"
    elif (month == "march" and day >= 21) or (month == "april" and day <= 19):
        return "Aries"
    elif (month == "april" and day >= 20) or (month == "may" and day <= 20):
        return "Taurus"
    elif (month == "may" and day >= 21) or (month == "june" and day <= 20):
        return "Gemini"
    elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
        return "Cancer"
    elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
        return "Leo"
    elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
        return "Virgo"
    elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
        return "Libra"
    elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
        return "Scorpio"
    elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
        return "Sagittarius"
    return "Unknown"


def is_valid_date(month, day):
    month = month.lower()
    max_days = {
        "january": 31, "february": 28, "march": 31, "april": 30,
        "may": 31, "june": 30, "july": 31, "august": 31,
        "september": 30, "october": 31, "november": 30, "december": 31
    }

    if month not in max_days:
        return False

    if month == "february" and day == 29:
        year = st.number_input("Enter year (for February 29 validation): ", min_value=1900, max_value=2100)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False
    return 1 <= day <= max_days[month]


# Streamlit UI
st.title("Zodiac Finder")
st.markdown("Discover your astrological sign based on your birth date.")

# Get user input
name = st.text_input("Enter your name:")

if name:  # Only proceed if name is entered
    birth_month = st.selectbox(
        "Select your birth month:",
        ["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"]
    )

    birth_day = st.number_input("Enter your birth day (1-31):", min_value=1, max_value=31)

    if st.button("Find My Zodiac Sign"):
        if is_valid_date(birth_month, birth_day):
            st.success(f"Valid date: {birth_month}, {birth_day}")
            show_progress()
            zodiac_sign = get_zodiac(birth_month, birth_day)
            st.balloons()
            st.success(f"Hello, **{name}**! Your zodiac sign is: **{zodiac_sign}**")
        else:
            st.error(f"Invalid date: {birth_month}, {birth_day} does not exist.")