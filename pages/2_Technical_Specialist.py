import streamlit as st
from menu import menu_with_redirect
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os 
import pandas as pd

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}")


# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("tech specialist screen")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")


# connect to the database and printing connection successful if connected
with engine.connect() as conn:
    print("Connection successful")
    # dataframe!!!
    df = pd.read_sql("select * from main.test_program", conn)

st.dataframe(df)

# with engine.begin() as connection:
    
df.loc[3,:] = [6, "2Lo", 3]

st.dataframe(df)

st.title("jumps")
col1, col2, col3, col4, col5 = st.columns(5)
col1.write("toeloop")
col2.button("1")
col3.button("2")
col4.button("3")
col5.button("4")

