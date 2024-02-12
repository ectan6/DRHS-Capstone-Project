import streamlit as st
from menu import menu
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os 
import pandas as pd


postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/club_judging_system")

# connect to the database and printing connection successful if connected
with engine.connect() as conn:
    print("Connection successful")
    # sql_text = text("select * from main.test")
    # result = conn.execute(sql_text)
    # rows = result.fetchall()
    # dataframe!!!
    df = pd.read_sql("select * from main.test", conn)
    # print(rows)

# st.dataframe(df)

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