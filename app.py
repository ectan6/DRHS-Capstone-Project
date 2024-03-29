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
st.session_state.competition_name = comp
comp_id = comp[4:5]
st.session_state.competition_id = int(comp_id)

# Call to DB
with engine.connect() as conn:
    query = f"""
        SELECT p.user_id, u.first_name, u.last_name 
        FROM main.programs p 
        JOIN main.users u ON u.user_id = p.user_id 
        WHERE p.competition_id = {int(comp_id)}
    """
    total_available_users = pd.read_sql(query, conn)
    print(total_available_users)
    # get rid of duplicate users
    st.session_state.available_users = pd.DataFrame(columns=["user_id", "first_name", "last_name"])
    for id in total_available_users["user_id"]:
        if id not in st.session_state.available_users["user_id"]:
            st.session_state.available_users.loc[len(st.session_state.available_users.index)] = [id,total_available_users.loc[total_available_users["user_id"] == id, "first_name"].values[0], total_available_users.loc[total_available_users["user_id"] == id, "last_name"].values[0]]

user_list = st.session_state.available_users.to_dict(orient="records")
user_dict = st.selectbox(
    "Select a competitor: ",
    user_list,
    format_func=lambda x: x["first_name"] + " " + x["last_name"],
)
st.session_state.user_id = user_dict["user_id"]
st.session_state.user_name = user_dict["first_name"] + " " + user_dict["last_name"]
print(st.session_state.user_name)

with engine.connect() as conn:
    query2 = f"""
        SELECT program_id
        FROM main.programs
        WHERE competition_id = {int(comp_id)} and user_id = {st.session_state.user_id}
    """
    program_id_list = pd.read_sql(query2, conn)
    print(program_id_list)

# add program selector here
st.session_state.program_id = st.selectbox("Select a program: ", program_id_list)

menu()  # render dynamic menu

if "changed_data" not in st.session_state:
    st.session_state.changed_data = False

if "available_users" not in st.session_state:
    st.session_state.available_users = [{"user_id": 1, "first_name": "John", "last_name": "Doe"}, {"user_id": 2, "first_name": "Jane", "last_name": "Doe"}]

# setting the user_id
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user_name" not in st.session_state:
    st.session_state.user_name = None

if "user_index" not in st.session_state:
    st.session_state.user_index = None
# program_id is a bigserial in the programs table - might need to change this
if "program_id" not in st.session_state:
    st.session_state.program_id = None
if "competition_id" not in st.session_state:
    st.session_state.competition_id = None
if "competition_name" not in st.session_state:
    st.session_state.competition_name = None


print("Session state from app.py ", st.session_state.to_dict())
