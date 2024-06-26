import time
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
engine = create_engine(
    f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}"
)

if st.session_state.role not in ["technical specialist", "judge"]:
    st.warning("You do not have permission to view this page.")
    st.stop()
st.title("judge screen")

st.write("Juding for", st.session_state.user_name)
st.write("Program: ", st.session_state.program_id)

c1, c2 = st.columns([0.2, 0.8])


with c1:
    st.write("Program Elements")

    # df = st.dataframe(pd.DataFrame({'Element': []}))
    data = pd.DataFrame({'Element': []})
    styled_data = pd.DataFrame({'Element': []})
                 
    if st.session_state.changed_data:
        # Connect to the DB and read in a score for the user_id and program_id
        print("Getting an update from the DB")

        with engine.connect() as conn:
            data = pd.read_sql(f"SELECT * FROM main.readable_elements WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id} ORDER BY order_executed", conn)
            # styled_data = data.style.set_properties(**{'height': 100px})
            # styled_data = data.style.set_table_styles([{"selector": "tr", "props": "line-height: 100px;"}])
        
    # styled_data_html = data.to_html(classes="styled-data")
    # styled_data_html_with_css = f'<style>table tr {{ height: 100px; }}</style>{styled_data_html}'
    # st.write(styled_data_html_with_css, unsafe_allow_html=True)

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
    st.write("")
    st.write("")
    def add_goe_buttons(row_num: int):
        goe_buttons = st.columns([.1, .1, .1, .1, .1, .083, .083, .083, .083, .083, .083])
        for i in range(11):
            with goe_buttons[i]:
                print("creating button", i-5)
                if st.button(label=str(i-5), key=f"goe-{i}-row-{row_num}"):
                    print(f"goe-{i}-row-{row_num}")
                    with engine.connect() as conn:
                        print("Connected to DB")
                        goe_query = f"""
                            INSERT INTO main.judge_goe (user_id, program_id, element_number, goe, judge_1)
                            VALUES ('{st.session_state.user_id}', '{st.session_state.program_id}', '{row_num}', '{i-5}', '{i-5}')
                        """
                        conn.execute(text(goe_query))
                        conn.commit()
                        print("Updated GOE")
                        st.session_state.changed_data = False

    if st.session_state.changed_data:
        print("data changed")
        for j in range(st.session_state.selected_element -1):
            print(j+1)
            add_goe_buttons(j+1)
        print("done")
        

st.divider() #--------------------------------------------------------

st.subheader("Program Component Scores")

c1, c2 = st.columns([0.9, 0.1])

def create_pcs_sliders(name: str):
    # st.write(name, ": ", name_value)
    with c1:
        name_value = st.slider(f"{name}:", 0.0, 10.0, 5.0, 0.25)
    with c2:
        # st.write("You chose", name_value, f"for {name}")
        st.write("")
        st.write("")
        st.write(name_value)
        st.write("")
        st.write("")
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
    st.snow()
