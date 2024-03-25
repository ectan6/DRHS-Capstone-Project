import streamlit as st
from menu import menu
import pandas as pd


if "role" not in st.session_state:
    st.session_state.role = None

# initialize role
st.session_state._role = st.session_state.role


def set_role():
    st.session_state.role = st.session_state._role


c1, c2 = st.columns(2)
with c1:
    st.title("Club Judging System")
with c2:
    # st.image(r"...\DRHS-Capstone-Project\logo.png")
    st.image("logo.png", width=280)

# selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)

menu()  # render dynamic menu

if "changed_data" not in st.session_state:
    st.session_state.changed_data = False

# setting the user_id
if "user_id" not in st.session_state:
    st.session_state.user_id = 1
# program_id is a bigserial in the programs table - might need to change this
if "program_id" not in st.session_state:
    st.session_state.program_id = 1


print("Session state from app.py ", st.session_state.to_dict())
