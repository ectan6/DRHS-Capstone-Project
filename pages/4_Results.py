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

with engine.connect() as conn:
    judge_table = pd.read_sql(f"SELECT * FROM main.readable_elements WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id} ORDER BY order_executed", conn)
    pcs_table = pd.read_sql(f"SELECT * FROM main.pcs WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id}", conn)
    goe_table = pd.read_sql(f"SELECT * FROM main.judge_goe WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id}", conn)
    score_table = pd.read_sql(f"SELECT * FROM main.score WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id}", conn)

    jump_score_table = pd.read_sql(f"SELECT * FROM main.jumps", conn)
    spins_steps_score_table = pd.read_sql(f"SELECT * FROM main.spins_steps", conn)

# doing logging/debugging 50-55
print(goe_table)
# goes = goe_table["goe"].values
goes = goe_table["judge_1"].values
print(goes)
for goe in goes:
    print("GOE: ", goe)
    
elements = judge_table.drop(["id", "user_id", "program_id"], axis=1)
st.dataframe(elements, hide_index= True, column_config={"order_executed": "#", "element": "Element"})
print(score_table)
for index, row in score_table.iterrows():
    print("__________________")
    print(row)
    if row["jump_id"] is not None:
        print("Jump ID:", row["jump_id"])
        # return the score of the jump from the jump table

    else:
        print("Spin/Step ID:", row["spin_id"])
        # return the score of the spin/step from the spin/step table

# rn: showing the judge df. need to add in the base value, goe, judge score(s), and ref score of panel
# st.dataframe(
#     judge_table,
#     hide_index=True,
#     column_config={
#         "id": None,
#         "user_id": None,
#         "program_id": None,
#         "order_executed": "#",
#         "element": "Element"
#         },
# )

# df for pcs - need to display factor and totals
st.dataframe(
    pcs_table,
    hide_index=True,
    column_config={
        "id": None,
        "user_id": None,
        "program_id": None,
        "skating_skills": "Skating Skills",
        "transitions": "Transitions",
        "performance": "Performance",
        "choreography": "Choreography",
        "interpretation": "Interpretation"
        },
)