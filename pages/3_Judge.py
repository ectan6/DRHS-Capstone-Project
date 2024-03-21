import streamlit as st
from menu import menu_with_redirect
from apscheduler.schedulers.background import BackgroundScheduler
from app import get_changed_data
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
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
st.title("judge screen")

c1, c2 = st.columns(2)

# creating dataframe
data = {
    'Element': ['2Lz']
}
df = pd.DataFrame(data)
df.index += 1

if "completed_program_elements" not in st.session_state:
    st.session_state.completed_program_elements = df

print(st.session_state.completed_program_elements)

def create_new_row(new_element: str):
    # polling is running before rendering the screen
    # if "completed_program_elements" not in st.session_state:
    #     data = {
    #     'Element': ['2Lz']
    #     }
    #     df = pd.DataFrame(data)
    #     df.index += 1

    #     st.session_state.completed_program_elements = df

    print(st.session_state.completed_program_elements)

    new_row = pd.DataFrame({'Element': [new_element]})
    st.session_state.completed_program_elements = pd.concat([st.session_state.completed_program_elements, new_row], ignore_index=True)
    
    # df1 = pd.concat([df1, new_row], ignore_index=True)
    # print(df1)
    # st.dataframe(df1, hide_index=False, column_config={'Element': 'Element'})
    # c1.write(df1, hide_index=False, column_config={'Element': 'Element'})

def check_changed_data():
    if get_changed_data() == True:
        print("data has changed")
        with engine.connect() as conn:
            # user and program id to be added so that know when to start reading
            df = pd.read_sql("SELECT * FROM main.score", conn)
            print(df)
            # c1.dataframe(df, hide_index=False, column_config={'Element': 'Element'})
    else: 
        print("data has not changed")

with c1:
    st.write("Completed Program Elements")
    # displaying dataframe
    st.dataframe(st.session_state.completed_program_elements, hide_index=False, column_config={'Element': 'Element'})

with c2:
    st.write("Grade of Execution")
    # add buttons - will use a function

sched = BackgroundScheduler()
sched.add_job(check_changed_data, 'interval', seconds=3)
sched.start()

st.divider()

def create_pcs_sliders(name: str):
    # slider arguments: label, min, max, default, step
    name_value = st.slider(f'{name}:', 0.0, 10.0, 5.0, 0.25)
    st.write("You chose", name_value, f'for {name}')

create_pcs_sliders('skating skills')
create_pcs_sliders('transitions')
create_pcs_sliders('performance')
create_pcs_sliders('choreography')
create_pcs_sliders('interpretation')

st.button("submit", key="submit-judge")
