import streamlit as st
from utils.loader import load_data

st.set_page_config(page_title="MediLog", layout="wide")

st.title("🏥 MediLog")

df = load_data()

st.write(df)