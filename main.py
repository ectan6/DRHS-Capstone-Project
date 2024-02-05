from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os 
import streamlit as st
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

st.title("Club Judging System!")

# login = st.button("Login", type="primary")

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.button('Login', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    user_type = st.selectbox(
        'I am a:',
        [None, 'skater', 'technical specialist', 'judge'],
        on_change=set_state, args=[2]
    )
    if user_type is None:
        set_state(1)

if st.session_state.stage >= 2:
    user = st.text_input('username', on_change=set_state, args=[3])

if st.session_state.stage >=3:
    password = st.text_input('password', on_change=set_state, args=[4])

if st.session_state.stage >= 4:
    st.write(f'Hello {user}!')
    st.button('Start Over', on_click=set_state, args=[0])

# st.dataframe(df)