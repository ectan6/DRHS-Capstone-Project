import streamlit as st
from menu import menu_with_redirect
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os

menu_with_redirect()

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}")


# GOE is calculated in database: kick out lowest and highest scores, then average the rest
# for now, the goe is just the 1 judge's score

st.title("Results for " + st.session_state.competition_name + ", program " + str(st.session_state.program_id))

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.write("Name")
    st.write("")
    st.write(st.session_state.user_name)
with c2:
    st.write("Total Segment Score")

with c3:
    st.write("Total Element Score")
    
with c4:
    st.write("Total Program Component Score (Factored)")

with c5:
    st.write("Total Deductions")

st.divider()
# dataframe = pd.DataFrame({'Element': [], 'Base Value': [], 'GOE': [], 'Score': []})
# WAITTTT MAYBE i can just (when inserting into score database) insert into readable_elment and then we r chilling
