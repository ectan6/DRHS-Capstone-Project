import streamlit as st
from menu import menu_with_redirect
from apscheduler.schedulers.background import BackgroundScheduler

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
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
st.title("judge screen")

c1, c2 = st.columns(2)


# print(st.session_state.completed_program_elements)


# will probably not be using this function
def create_new_row(new_element: str):
    print(st.session_state.completed_program_elements)

    new_row = pd.DataFrame({"Element": [new_element]})
    st.session_state.completed_program_elements = pd.concat(
        [st.session_state.completed_program_elements, new_row], ignore_index=True
    )

    # c1.write(df1, hide_index=False, column_config={'Element': 'Element'})


with c1:
    st.write("Completed Program Elements")

    data = pd.DataFrame({})

    if st.session_state.changed_data:
        # Connect to the DB and read in a score for the user_id and program_id
        print("Getting an update from the DB")

        # Create a dummy dataframe for now
        data = pd.DataFrame({"Element": ["2F"]})

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
