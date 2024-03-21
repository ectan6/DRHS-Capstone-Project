import streamlit as st
from menu import menu_with_redirect
from apscheduler.schedulers.background import BackgroundScheduler
from app import get_changed_data
import pandas as pd

menu_with_redirect()

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
st.title("judge screen")

# creating dataframe
data = {
    'Element': ['2Lz']
}
df = pd.DataFrame(data)
df.index += 1

c1, c2 = st.columns(2)

def create_new_row(new_element: str, df1: pd.DataFrame):
    new_row = pd.DataFrame({'Element': [new_element]})
    df1 = pd.concat([df1, new_row], ignore_index=True)
    print(df1)
    c1.dataframe(df1, hide_index=False, column_config={'Element': 'Element'})

def check_changed_data():
    if get_changed_data() == True:
        print("data has changed")
        # add a row to dataframe
        create_new_row('3F', df)
    else: 
        print("data has not changed")

with c1:
    st.write("Completed Program Elements")
    # displaying dataframe
    completed_program_elements = st.dataframe(df, hide_index=False, column_config={'Element': 'Element'})

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
