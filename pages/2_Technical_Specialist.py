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
        sql = f"INSERT INTO main.score(jump_id) VALUES('{jump_id}')"
        conn.execute(text(sql))
        conn.commit()
        # st.dataframe(pd.read_sql("select * from main.score", conn))        


# 3 big columns and then nest columns for jumps and spins
col1, col2, col3 = st.columns(3)

with col1:
    # nest jump columns in here
    st.write("jumps")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.write("Toeloop")
        st.write("Salchow")
        st.write("Loop")
        st.write("Flip")
        st.write("Lutz")
        st.write("Axel")
        st.write("Euler")
    with c2:
        if st.button(label="1", key="1toe"):
            click_button("1T", "", 2)
        if st.button(label="1", key="1sal"):
            click_button("1S", "", 2)
        if st.button(label="1", key="1loop"):
            click_button("1Lo", "", 2)
        if st.button(label="1", key="1flip"):
            click_button("1F", "", 2)
        if st.button(label="1", key="1lz"):
            click_button("1Lz", "", 2)
        if st.button(label="1", key="1axel"):
            click_button("1A", "", 2)
        if st.button(label="1", key="1eu"):
            click_button("1Eu", "", 2)
    with c3: 
        if st.button(label="2", key="2toe"):
            click_button("2T", "", 2)
        if st.button(label="2", key="2sal"):
            click_button("2S", "", 2)
        if st.button(label="2", key="2loop"):
            click_button("2Lo", "", 2)
        if st.button(label="2", key="2flip"):
            click_button("2F", "", 2)
        if st.button(label="2", key="2lz"):
            click_button("2Lz", "", 2)
        if st.button(label="2", key="2axel"):
            click_button("2A", "", 2)
    with c4:
        if st.button(label="3", key="3toe"):
            click_button("3T", "", 2)
        if st.button(label="3", key="3sal"):
            click_button("3S", "", 2)
        if st.button(label="3", key="3loop"):
            click_button("3Lo", "", 2)
        if st.button(label="3", key="3flip"):
            click_button("3F", "", 2)
        if st.button(label="3", key="3lz"):
            click_button("3Lz", "", 2)
        if st.button(label="3", key="3axel"):
            click_button("3A", "", 2)
    with c5:
        if st.button(label="4", key="4toe"):
            click_button("4T", "", 2)
        if st.button(label="4", key="4sal"):
            click_button("4S", "", 2)
        if st.button(label="4", key="4loop"):
            click_button("4Lo", "", 2)
        if st.button(label="4", key="4flip"):
            click_button("4F", "", 2)
        if st.button(label="4", key="4lz"):
            click_button("4Lz", "", 2)
        if st.button(label="4", key="4axel"):
            click_button("4A", "", 2)


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
