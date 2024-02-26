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
def click_button(score_id: int, jump_id: str, spin_id: str, order_executed: int):
    # connect to the database
    with engine.connect() as conn:
        # dataframe!!!
        old_df = pd.read_sql("select * from main.score", conn)
        d = {"score_id": [score_id], "jump_id": [jump_id], "spin_id": [spin_id], "order_executed": [order_executed]}
        temp_df = pd.DataFrame(data=d)   
        new_df = pd.concat([old_df, temp_df])
        print(new_df)
        sql_call = new_df.to_sql(name='score', schema='main', con=conn, if_exists='replace', index=False)
        print(sql_call)
        conn.commit()


st.title("jumps")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write("toeloop")

with col2:
    # if button clicked inside here instead of session state
    # ex:
    if st.button("1"):
        click_button(2, "1T", "", 2)

with col3:
    if st.button("2"):
        click_button(15, "1T","", 7)

with col4:
    if st.button("3"):
        click_button(44, "1T", "", 8)

with col5:
    if st.button("4"):
        click_button(55, "1T", "", 9)

# with col6:
#     df_completed_elements = pd.DataFrame(
#         {
#             "element": "Element"
#         }
#     )
#     st.dataframe(df_completed_elements)