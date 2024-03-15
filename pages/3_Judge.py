import streamlit as st
from menu import menu_with_redirect
from apscheduler.schedulers.background import BackgroundScheduler

menu_with_redirect()

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.markdown(f"You are currently logged with the role of {st.session_state.role}.")
st.title("judge screen")

sched = BackgroundScheduler()

def check_changed_data():
    # if st.session_state.changed_data == True:
    print("just changed the data")

sched.add_job(check_changed_data, 'interval', seconds = 3)
sched.start()

c1, c2 = st.columns(2)
with c1:
    st.write("Completed Program Elements")
    # put table here - same as the one on the technical specialist page

    # see if session state has changed (from tech specialist submission)

with c2:
    st.write("Grade of Execution")
    # buttons should line up with the rows on the completed program elements table

st.divider()

# slider arguments: label, min, max, default, step
skating_skills = st.slider('skating skills', 0.0, 10.0, 5.0, 0.25)
st.write("you chose", skating_skills, 'for skating skills')

transitions = st.slider('transitions', 0.0, 10.0, 5.0, 0.25)
st.write("you chose", transitions, 'for transitions')

performance = st.slider('performance', 0.0, 10.0, 5.0, 0.25)
st.write("you chose", performance, 'for performance')

choreography = st.slider('choreography', 0.0, 10.0, 5.0, 0.25)
st.write("you chose", choreography, 'for choreography')

interpretation = st.slider('interpretation', 0.0, 10.0, 5.0, 0.25)
st.write("you chose", interpretation, 'for interpretation')

st.button("submit")