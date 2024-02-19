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
def click_button(program_id: int, element_id: str, counter: int):
    # connect to the database
    with engine.connect() as conn:
        # dataframe!!!
        old_df = pd.read_sql("select * from main.test_program", conn)
        old_df.loc[counter, :] = [program_id, element_id, counter]
        print(old_df)
        sql_call = old_df.to_sql('main.test_program', conn, if_exists='replace', index=False)
        print(sql_call)
        conn.commit()

st.title("jumps")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write("toeloop")
    # if button clicked inside here instead of session state
    # ex:
    if st.button("1"):
        click_button(8, "2S", 6)
        # st.dataframe(df)


# col1.write("toeloop")
# col2.button("1", on_click=click_button)
# col3.button("2", on_click=click_button)
# col4.button("3", on_click=click_button)
# col5.button("4", on_click=click_button)

# st.dataframe(df)

# if st.session_state.clicked:
#     df.loc[4,:] = [7, "3S", 4]

    # sql = "INSERT INTO main.test_program(program_id, element_1, counter) VALUES(10, '3F', 4)"
    # with engine.begin() as connection:
    #     connection.execute(sql)
    # st.dataframe(pd.read_sql("select * from main.test_program", engine.connect()))

    # df.to_sql('main.test_program', engine, if_exists='replace', index=False)

    # # printing the dataframe from pandas
    # st.dataframe(df)

    # #printing to see if the sql changed tho
    # st.dataframe(pd.read_sql("select * from main.test_program", engine.connect()))
    # # spoiler alert: it doesn't :(