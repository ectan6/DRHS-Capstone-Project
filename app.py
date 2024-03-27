import streamlit as st
from menu import menu
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()
import os

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(
    f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}"
)

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

# Create a list of available users given a competition
comp = st.selectbox("Select a competition", ["comp1", "comp2", "comp3"])
comp_id = comp[4:5]
print(comp_id)

# Call to DB
with engine.connect() as conn:
    st.session_state.available_users = pd.read_sql(f"SELECT p.user_id, u.first_name, u.last_name FROM programs p join users on users.id = programs.user_id u WHERE p.competition_id = {comp}", conn)
    st.session_state.available_users = pd.DataFrame(
        {
            "user_id": [1, 2],
            "first_name": ["John", "Jane"],
            "last_name": ["Doe", "Doe"],
        }
    )
# st.session_state.available_users = sql("SELECT p.user_id, u.first_name, u.last_name FROM programs p join users on users.id = programs.user_id u WHERE p.competition_id = st.session_state.competition_id")
st.write("select a user to judge")
user_dict = st.selectbox(
    "Select a user: ",
    st.session_state.available_users,
    format_func=lambda x: x["first_name"] + " " + x["last_name"],
)


menu()  # render dynamic menu

if "changed_data" not in st.session_state:
    st.session_state.changed_data = False

if "available_users" not in st.session_state:
    st.session_state.available_users = [{"user_id": 1, "first_name": "John", "last_name": "Doe"}, {"user_id": 2, "first_name": "Jane", "last_name": "Doe"}]

# setting the user_id
if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "user_index" not in st.session_state:
    st.session_state.user_index = None
# program_id is a bigserial in the programs table - might need to change this
if "program_id" not in st.session_state:
    st.session_state.program_id = 1


print("Session state from app.py ", st.session_state.to_dict())
