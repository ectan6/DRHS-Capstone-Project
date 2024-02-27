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


st.title("jumps")
# 3 big columns and then nest columns for jumps and spins
col1, col2, col3 = st.columns(3)
# widths in px
column_widths = [125, 100, 100, 100, 100, 300]
# trying to make the columns with the buttons skinnier...
column_styling = [
    f"max-width: {width}px;"
    for width in column_widths
]
column_styling = ";".join(column_styling)
st.markdown(f"<style>.reportview-container .main .block-container{{flex: 1;}} .column-widget.stHorizontal{{{column_styling}}}</style>", unsafe_allow_html=True)

with col1:
    # nest jump columns in here
    st.write("toeloop")

with col2:
    # if button clicked inside here instead of session state
    # ex:
    if st.button("1"):
        click_button("1T", "", 2)

with col3:
    if st.button("2"):
        click_button("1T","", 7)

with col4:
    if st.button("3"):
        click_button("1T", "", 8)

with col5:
    if st.button("4"):
        click_button("1T", "", 9)

with col6:
    completed_elements = pd.DataFrame(
        {
            "element": ["Element"]
        }
    )
    st.dataframe(completed_elements)