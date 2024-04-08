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
c1.write("Name")
c1.write("")
c2.write("Total Segment Score")
c3.write("Total Element Score")
c4.write("Total Program Component Score (Factored)")
c5.write("Total Deductions")

c6, c7, c8, c9, c10 = st.columns(5)
c6.write(st.session_state.user_name)

st.divider() # --------------------------------------------------

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
# scores of panel = bv + goe
scores_of_panel = []
for e in elements.index:
    scores_of_panel.append(elements["Base Value"].values[e] + elements["GOE"].values[e])
print("scores_of_panel", scores_of_panel)
elements["Scores of Panel"] = scores_of_panel
st.dataframe(elements, hide_index= True, column_config={
        "order_executed": "#", 
        "element": "Element", 
        "Base Value": "Base Value", 
        "GOE": "GOE", 
        "Judge Score": "Judge Score",
        "Scores of Panel": "Scores of Panel"
        },
        use_container_width=True
    )

tes = 0
for sop in scores_of_panel:
    tes += sop
c8.write(tes.round(1))

# ----------------------------------------------

judge_1_pcs = [pcs_table["skating_skills"].values[0], pcs_table["transitions"].values[0], pcs_table["performance"].values[0], pcs_table["choreography"].values[0], pcs_table["interpretation"].values[0]]
pcs_df = pd.DataFrame(judge_1_pcs, columns=["Judge 1"])
factor = [0.8, 0.8, 0.8, 0.8, 0.8]
pcs_df["Factor"] = factor
pcs_df["Factored PCS"] = pcs_df["Judge 1"] * pcs_df["Factor"]

fpcs_score = 0
for fpcs in pcs_df["Factored PCS"]:
    fpcs_score += fpcs
c9.write(round(fpcs_score, 1))

st.dataframe(pcs_df, hide_index=True, column_config={
        "Judge 1": "Judge 1", 
        "Factor": "Factor", 
        "Factored PCS": "Factored PCS"
        },
        use_container_width=True
    )

deductions = 0
st.write("Deductions: ", deductions)
c10.write(0)

total_segment_score = tes + fpcs_score - deductions
c7.write(round(total_segment_score, 1))
