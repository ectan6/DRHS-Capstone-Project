import streamlit as st
from menu import menu_with_redirect
# from apscheduler.schedulers.background import BackgroundScheduler

# from app import get_changed_data
import pandas as pd
from sqlalchemy import create_engine
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

# if "user_id" in st.session_state:
#     for i, user in enumerate(st.session_state.available_users):
#         if user["user_id"] == st.session_state.user_id:
#             st.session_state.user_index = i

# user_dict = st.selectbox("Select a user: ", st.session_state.available_users, format_func=lambda x: x["first_name"] + " " + x["last_name"], index=st.session_state.user_index)

# if user_dict:
#     st.session_state.user_id = user_dict["user_id"]

st.write("Juding for", st.session_state.user_name)
st.write("Program: ", st.session_state.program_id)

c1, c2 = st.columns(2)


with c1:
    st.write("Completed Program Elements")

    data = pd.DataFrame({'Element': []})
    if st.session_state.changed_data:
        # Connect to the DB and read in a score for the user_id and program_id
        print("Getting an update from the DB")

        with engine.connect() as conn:
            # if spin_id is null then the element is a jump
            program_elements = pd.read_sql(f"SELECT * FROM main.score WHERE program_id = {st.session_state.program_id} and user_id = {st.session_state.user_id} ORDER BY id DESC", conn)
            print("program elements:")
            print(program_elements)
        # replace 3Lz with readable element 
        readable_element = ""
        print(program_elements["jump_id"][0])
        
        # for number of elements completed so far, run row adding loop
        for i in range(st.session_state.selected_element -1):
            # need this to be specific to order_executed 
            # num_in_order_executed = 0
            # for row in program_elements["order_executed"]:
            #     if row == i:
            #         num_in_order_executed += 1
            # print(num_in_order_executed)
            # for j in reversed(range(num_in_order_executed)):
            for j in reversed(range(st.session_state.sequence_counter)):
                # if program_elements["order_executed"][j] == i:
                # if spin is is null, then add jump
                if program_elements["spin_id"][j] == None:
                    if j == 0:
                        readable_element += program_elements["jump_id"][j]
                    else:
                        readable_element += program_elements["jump_id"][j] + "+"
                # if jump id is null, then add level and spin
                elif program_elements["jump_id"][j] == None:
                    readable_element += program_elements["spin_id"][j] + str(int(program_elements["spin_level"][j]))
                print(readable_element)
            print(readable_element)
            data.loc[len(data.index)] = [readable_element]
            # add to beginning of dataframe bc going backwards
    # Revert the changed_data flag
    st.session_state.changed_data = False

    # displaying dataframe
    st.dataframe(
        data,
        hide_index=False,
        column_config={"Element": "Element"},
    )

with c2:
    st.write("Grade of Execution")
    # add buttons - will use a function

st.divider()


def create_pcs_sliders(name: str):
    # slider arguments: label, min, max, default, step
    name_value = st.slider(f"{name}:", 0.0, 10.0, 5.0, 0.25)
    st.write("You chose", name_value, f"for {name}")


create_pcs_sliders("skating skills")
create_pcs_sliders("transitions")
create_pcs_sliders("performance")
create_pcs_sliders("choreography")
create_pcs_sliders("interpretation")

st.button("submit", key="submit-judge")
