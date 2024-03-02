import streamlit as st
from menu import menu_with_redirect
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
load_dotenv()
import os 
import pandas as pd
from streamlit_modal import Modal

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}")


menu_with_redirect()
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("tech specialist screen")
st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

# function for adding elements to the score table in the database
def click_button(jump_id: str, spin_id: str, order_executed: int, spin_level: int):
    # connect to the database
    with engine.connect() as conn:
        sql = f"INSERT INTO main.score(jump_id, spin_id, order_executed, spin_level) VALUES('{jump_id}', '{spin_id}', '{order_executed}', '{spin_level}')"
        conn.execute(text(sql))
        conn.commit()
        # st.dataframe(pd.read_sql("select * from main.score", conn))        

# testing out if the buttons always display one after the other (i want them to be in a row...)
st.button("test1")
st.button("test2")

# 3 big columns and then nest columns for jumps and spins
col1, col2, col3 = st.columns(3)

# jumps column
with col1:
    # nest jump columns in here
    st.write("jumps")
    c1, c2, c3, c4, c5 = st.columns(spec=[0.32, 0.17, 0.17, 0.17, 0.17])
    with c1:
        st.write("Toeloop")
        st.write("Salchow")
        st.write("Loop")
        st.write("Flip")
        st.write("Lutz")
        st.write("Axel")
        st.write("Euler")
    with c2:
        if st.button(label="1", key="1toe"):
            click_button("1T", "", 2)
        if st.button(label="1", key="1sal"):
            click_button("1S", "", 2)
        if st.button(label="1", key="1loop"):
            click_button("1Lo", "", 2)
        if st.button(label="1", key="1flip"):
            click_button("1F", "", 2)
        if st.button(label="1", key="1lz"):
            click_button("1Lz", "", 2)
        if st.button(label="1", key="1axel"):
            click_button("1A", "", 2)
        if st.button(label="1", key="1eu"):
            click_button("1Eu", "", 2)
    with c3: 
        if st.button(label="2", key="2toe"):
            click_button("2T", "", 2)
        if st.button(label="2", key="2sal"):
            click_button("2S", "", 2)
        if st.button(label="2", key="2loop"):
            click_button("2Lo", "", 2)
        if st.button(label="2", key="2flip"):
            click_button("2F", "", 2)
        if st.button(label="2", key="2lz"):
            click_button("2Lz", "", 2)
        if st.button(label="2", key="2axel"):
            click_button("2A", "", 2)
    with c4:
        if st.button(label="3", key="3toe"):
            click_button("3T", "", 2)
        if st.button(label="3", key="3sal"):
            click_button("3S", "", 2)
        if st.button(label="3", key="3loop"):
            click_button("3Lo", "", 2)
        if st.button(label="3", key="3flip"):
            click_button("3F", "", 2)
        if st.button(label="3", key="3lz"):
            click_button("3Lz", "", 2)
        if st.button(label="3", key="3axel"):
            click_button("3A", "", 2)
    with c5:
        if st.button(label="4", key="4toe"):
            click_button("4T", "", 2)
        if st.button(label="4", key="4sal"):
            click_button("4S", "", 2)
        if st.button(label="4", key="4loop"):
            click_button("4Lo", "", 2)
        if st.button(label="4", key="4flip"):
            click_button("4F", "", 2)
        if st.button(label="4", key="4lz"):
            click_button("4Lz", "", 2)
        if st.button(label="4", key="4axel"):
            click_button("4A", "", 2)

# completed elements table
with col2:
    st.write("completed elements table")
    # probably going to get rid of this dataframe??? and use the sql commands to pull the elements from the score table
    completed_elements = pd.DataFrame(
        {
            "element": ["Element"]
        }
    )
    st.dataframe(completed_elements)


modal = Modal(
    "Spin Level", 
    key="spin_level_modal",
    # Optional
    padding=20,
    max_width=744
)
if modal.is_open():
    with modal.container():
        # insert id and level (from buttons) and close the modal
        spin_id = st.session_state['spin_id'] 
        if st.button("0", key="spin_level_0"):
            click_button("", spin_id, 1, 0)     
            modal.close()
        if st.button("1", key="spin_level_1"):
            click_button("", spin_id, 1, 1)     
            modal.close()
        if st.button("2", key="spin_level_2"):
            click_button("", spin_id, 1, 2)     
            modal.close()
        if st.button("3", key="spin_level_3"):
            click_button("", spin_id, 1, 3)     
            modal.close()
        if st.button("4", key="spin_level_4"):
            click_button("", spin_id, 1, 4)     
            modal.close()
        
# spins and steps column
with col3:
    st.write("spins")
    c6, c7, c8, c9 = st.columns(4)
    with c6:
        st.write("Upright")
        st.write("Layback")
        st.write("Camel")
        st.write("Sit")
        st.write("Combo")
    with c7:
        if st.button(label="✓", key="us"):
            st.session_state['spin_id'] = "USp"
            modal.open()
        if st.button(label="✓", key="ls"):
            st.session_state['spin_id'] = "LSp"
            modal.open()
        if st.button(label="✓", key="cs"):
            st.session_state['spin_id'] = "CSp"
            modal.open()
        if st.button(label="✓", key="ss"):
            st.session_state['spin_id'] = "SSp"
            modal.open()
        if st.button(label="✓", key="cos"):
            st.session_state['spin_id'] = "CoSp"
            modal.open()
    with c8: 
        if st.button(label="F", key="fus"):
            st.session_state['spin_id'] = "FUSp"
            modal.open()
        if st.button(label="F", key="fls"):
            st.session_state['spin_id'] = "FLSp"
            modal.open()
        if st.button(label="F", key="fcs"):
            st.session_state['spin_id'] = "FCSp"
            modal.open()
        if st.button(label="F", key="fss"):
            st.session_state['spin_id'] = "FSSp"
            modal.open()
        if st.button(label="F", key="fcos"):
            st.session_state['spin_id'] = "FCoSp"
            modal.open()
    with c9:
        if st.button(label="C", key="cus"):
            st.session_state['spin_id'] = "CUSp"
            modal.open()
        if st.button(label="C", key="cls"):
            st.session_state['spin_id'] = "CLSp"
            modal.open()
        if st.button(label="C", key="ccs"):
            st.session_state['spin_id'] = "CCSp"
            modal.open()
        if st.button(label="C", key="css"):
            st.session_state['spin_id'] = "CSSp"
            modal.open()
        if st.button(label="C", key="ccos"):
            st.session_state['spin_id'] = "CCoSp"
            modal.open()
    
    # -------------
            
    st.write("")
    st.write("sequences")
    c11, c12, c13, c14, c15 = st.columns(5)
    with c11:
        st.write("step")
        st.write("choreo")
    with c12:
        if st.button(label="1", key="1step"):
            click_button("", "StSq", 1)
        if st.button(label="✓", key="choreo"):
            click_button("", "ChSq", 1)

    with c13:
        if st.button(label="2", key="2step"):
            click_button("", "StSq", 1)
    with c14:
        if st.button(label="3", key="3step"):
            click_button("", "StSq", 1)
    with c15:
        if st.button(label="4", key="4step"):
            click_button("", "StSq", 1)
        

