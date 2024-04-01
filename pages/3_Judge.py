import streamlit as st
from menu import menu_with_redirect
# from apscheduler.schedulers.background import BackgroundScheduler

# from app import get_changed_data
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
import os

menu_with_redirect()

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(
    f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}"
)

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()
st.title("judge screen")

st.write("Juding for", st.session_state.user_name)
st.write("Program: ", st.session_state.program_id)

c1, c2 = st.columns(2)


with c1:
    st.write("Completed Program Elements")

    # df = st.dataframe(pd.DataFrame({'Element': []}))
    data = pd.DataFrame({'Element': []})
                 
    if st.session_state.changed_data:
        # Connect to the DB and read in a score for the user_id and program_id
        print("Getting an update from the DB")

        with engine.connect() as conn:
            data = pd.read_sql(f"SELECT * FROM main.readable_elements WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id} ORDER BY order_executed", conn)
    # Revert the changed_data flag
    st.session_state.changed_data = False

    # displaying dataframe
    st.dataframe(
        data,
        hide_index=True,
        column_config={
            "id": None,
            "user_id": None,
            "program_id": None,
            "order_executed": "#",
            "element": "Element"
            },
    )

with c2:
    st.write("Grade of Execution")
    # add buttons - will use a function

st.divider()


def create_pcs_sliders(name: str):
    # slider arguments: label, min, max, default, step
    name_value = st.slider(f"{name}:", 0.0, 10.0, 5.0, 0.25)
    st.write("You chose", name_value, f"for {name}")
    return name_value

skating_skills_score = create_pcs_sliders("skating skills")
transitions_score = create_pcs_sliders("transitions")
performance_score = create_pcs_sliders("performance")
choreography_score = create_pcs_sliders("choreography")
interpretation_score = create_pcs_sliders("interpretation")

if st.button("submit pcs", key="submit-judge-pcs"):
    with engine.connect() as conn:
        pcs_query = f"""INSERT INTO main.pcs (user_id, program_id, skating_skills, transitions, performance, choreography, interpretation) 
        VALUES ('{st.session_state.user_id}', '{st.session_state.program_id}', '{skating_skills_score}', '{transitions_score}', '{performance_score}', '{choreography_score}', '{interpretation_score}')"""
        conn.execute(text(pcs_query))
        conn.commit()
        print("Inserted PCS scores")
