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

# make fnctn w parameters -> one thing to update lots of stuff
def click_button(jump_id: str, spin_id: str, order_executed: int):
    # connect to the database
    with engine.connect() as conn:
        sql = "INSERT INTO main.score(jump_id) VALUES('3F')"
        conn.execute(text(sql))
        conn.commit()
        st.dataframe(pd.read_sql("select * from main.score", conn))        


# 3 big columns and then nest columns for jumps and spins
col1, col2, col3 = st.columns(3)

with col1:
    # nest jump columns in here
    st.write("jumps")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.write("toeloop")
    with c2:
        if st.button("1"):
            click_button("1T", "", 2)
    with c3: 
        if st.button("2"):
            click_button("1T","", 7)
    with c4:
        if st.button("3"):
            click_button("1T", "", 8)
    with c5:
        if st.button("4"):
            click_button("1T", "", 9)


with col2:
    st.write("completed elements table")
    # probably going to get rid of this dataframe??? and use the sql commands to pull the elements from the score table
    completed_elements = pd.DataFrame(
        {
            "element": ["Element"]
        }
    )
    st.dataframe(completed_elements)
    

with col3:
    st.write("spins and steps")
