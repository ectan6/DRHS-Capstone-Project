import streamlit as st
from menu import menu


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

menu() # render dynamic menu


if 'changed_data' not in st.session_state:
    st.session_state.changed_data = False

def get_changed_data():
    return st.session_state.changed_data

def set_changed_data(state: bool):
    st.session_state.changed_data = state