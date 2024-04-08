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
    
# number and element completed df -> need to add ase value, goe, judge score(s), and totals
elements = judge_table.drop(["id", "user_id", "program_id"], axis=1)

score_list = []

# for each individual component (row in score table), get the base value
for index, row in score_table.iterrows():
    print("__________________")
    print(row)
    if row["jump_id"] is not None:
        print("Jump ID:", row["jump_id"])
        # return the score of the jump from the jump table
        with engine.connect() as conn:
            jump_row = pd.read_sql(f"SELECT * FROM main.jumps WHERE jump_id = '{row['jump_id']}'", conn)
            print(jump_row)
            score = jump_row["sov"].values[0]
    else:
        print("Spin/Step ID:", row["spin_id"])
        # return the score of the spin/step from the spin/step table
        with engine.connect() as conn:
            spin_row = pd.read_sql(f"SELECT * FROM main.spins_steps WHERE spin_id = '{row['spin_id']}'", conn)
            print(spin_row)
            spin_level = int(row["spin_level"])
            print("Spin Level: ", spin_level)
            score = spin_row[f"level{spin_level}"].values[0]
    print("Score: ", score)
    score_list.append(score)
print("score_list", score_list)

# getting number of elements in each order_executed
num_order_executed = []
counter = 0
prev_order = 0
for index, row in score_table.iterrows():
    if row["order_executed"] != prev_order:
        if counter != 0:
            num_order_executed.append(counter)
        counter = 1
    else:
        counter += 1
    prev_order = row["order_executed"]
# (appending count for the last order_executed)
if counter != 0:
    num_order_executed.append(counter)
print("num_order_executed", num_order_executed)
    
list_for_df_scores = []
for i in range(len(num_order_executed)):
    # num_order_executed[i] is the number of elements in the i-th order_executed
    sum_of_scores = 0
    for j in range(num_order_executed[i]):
        sum_of_scores += score_list.pop(0)
    list_for_df_scores.append(round(sum_of_scores, 1))
print("list_for_df_scores", list_for_df_scores)

elements["Base Value"] = list_for_df_scores
goes = goe_table["judge_1"].values
elements["GOE"] = goes
elements["Judge Score"] = goes
st.dataframe(elements, hide_index= True, column_config={
        "order_executed": "#", 
        "element": "Element", 
        "Base Value": "Base Value", 
        "GOE": "GOE", 
        "Judge Score": "Judge Score"
        }
    )

# ----------------------------------------------

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