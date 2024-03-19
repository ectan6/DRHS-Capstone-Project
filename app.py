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


# Function to initialize session state
def init_session_state():
    return {'changed_data': False}

# Retrieve or initialize session state
session_state = st.session_state.get('session_state', init_session_state())

# Function to get changed_data
def get_changed_data():
    return session_state['changed_data']

# Function to set changed_data
def set_changed_data(state: bool):
    session_state['changed_data'] = state