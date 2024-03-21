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

def create_new_row(new_element: str, df1: pd.DataFrame):
    # add a new row to the completed program elements dataframe
    # completed_program_elements.add_row({'Order': 'New Order', 'Element': 'New Element'})
    new_row = {'Element': f'{new_element}'}
    df1 = df1.append(new_row, ignore_index=True)
    print(df1)
    c1.dataframe(df1, hide_index=False, column_config={'Element': 'Element'})

    # add buttons in the same line as the row
        # c2.button
    
def check_changed_data():
    if get_changed_data() == True:
        print("data has changed")
        # add a row to the completed_program_elements dataframe
        create_new_row('3F', df)
    else: 
        print("data has not changed")

c1, c2 = st.columns(2)
with c1:
    st.write("Completed Program Elements")
    # put table here - same as the one on the technical specialist page
    data = {
        'Element': ['2Lz']
    }
    df = pd.DataFrame(data)
    df.index += 1
    completed_program_elements = st.dataframe(df, hide_index=False, column_config={'Element': 'Element'})

with c2:
    st.write("Grade of Execution")
    # buttons should line up with the rows on the completed program elements table

sched = BackgroundScheduler()
sched.add_job(check_changed_data, 'interval', seconds = 3)
sched.start()

st.divider()

def create_pcs_sliders(name: str):
    # slider arguments: label, min, max, default, step
    name_value = st.slider(f'{name}:', 0.0, 10.0, 5.0, 0.25)
    st.write("you chose", name_value, f'for {name}')

# slider arguments: label, min, max, default, step
create_pcs_sliders('skating skills')
create_pcs_sliders('transitions')
create_pcs_sliders('performance')
create_pcs_sliders('choreography')
create_pcs_sliders('interpretation')

st.button("submit", key="submit-judge")