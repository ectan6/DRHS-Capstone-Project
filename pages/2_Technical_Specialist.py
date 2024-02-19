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

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.title("jumps")
col1, col2, col3, col4, col5 = st.columns(5)
col1.write("toeloop")
# b1 = st.button("1")
# b2 = st.button("2")
# b3 = st.button("3")
# b4 = st.button("4")
col2.button("1", on_click=click_button)
col3.button("2", on_click=click_button)
col4.button("3", on_click=click_button)
col5.button("4", on_click=click_button)

if st.session_state.clicked:
    # df.loc[4,:] = [7, "3S", 4]
    sql = "INSERT INTO main.test_program(program_id, element_1, counter) VALUES(10, '3F', 4)"
    with engine.begin() as connection:
        connection.execute(sql)
    st.dataframe(pd.read_sql("select * from main.test_program", engine.connect()))


# update the table with the new info (using df.loc)
# df.to_sql('main.test_program', engine, if_exists='replace')

# with engine.connect() as conn:
#     print("Connection successful")
#     # dataframe!!!
#     df = pd.read_sql("select * from main.test_program", conn)

