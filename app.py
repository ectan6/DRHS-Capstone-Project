import streamlit as st
from menu import menu

if "role" not in st.session_state:
    st.session_state.role = None

# initialize role
st.session_state._role = st.session_state.role
def set_role():
    st.session_state.role = st.session_state._role

# selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)

menu() # render dynamic menu