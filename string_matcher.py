from __future__ import annotations

import re

import pandas as pd
import streamlit as st
from rapidfuzz import fuzz


def clean_string(text):
    if isinstance(text, str):
        text = text.lower()  # convert to lowercase
        text = re.sub(r"\W", " ", text)  # remove special characters
        text = " ".join(text.split())  # remove extra spaces
    else:
        text = ""  # if not a string (like NaN), replace with empty string
    return text


# App title
st.title("String Matcher")

# Get user input
sf_data = st.text_input("Enter First String")
portal_data = st.text_input("Enter Second String")

# Check if both inputs are provided
if sf_data and portal_data:
    sf_data = clean_string(sf_data)
    portal_data = clean_string(portal_data)

    match_score = fuzz.ratio(sf_data, portal_data)
    if match_score > 90:
        rating = "🟢"
    elif match_score > 60:
        rating = "🟡"
    else:
        rating = "🔴"

    message = f"{rating}  The match score is: {match_score:.1f}%"
else:
    message = "Please enter data in both text fields."

st.write(message)
