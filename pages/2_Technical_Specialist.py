import streamlit as st
from menu import menu_with_redirect
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pages.Planned_Program_Components import create_jump_buttons

load_dotenv()
import os
import pandas as pd
from streamlit_modal import Modal
# import time

# from Planned_Program_Components import create_jump_buttons
# from app import set_changed_data

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(
    f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}"
)

MAX_ELEMENTS = 7


class Element:
    def __init__(self, element: str, level: int | None):
        self.element = element
        self.level = level

    def print_element(self):
        if self.level is not None:
            if self.level == 0:
                element_string = self.element + "B"
            else:
                element_string = self.element + str(self.level)
        else:
            element_string = self.element
        return element_string


menu_with_redirect()
if st.session_state.role not in ["technical specialist", "judge"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title("Technical Specialist Screen")

# function for adding elements to the score table in the database
def click_button(jump_id: str, spin_id: str, spin_level: int):
    if jump_id:
        st.session_state.completed_elements.loc[
            st.session_state.selected_element - 1, "element_list"
        ].append(Element(jump_id, None))
    if spin_id:
        st.session_state.completed_elements.loc[
            st.session_state.selected_element - 1, "element_list"
        ].append(Element(spin_id, spin_level))

st.write("Competitor: ", st.session_state.user_name)
st.write("Program: ", st.session_state.program_id)

# 3 big columns and then nest columns for jumps and spins
col1, col2 = st.columns(2)

# jumps column
with col1:
    # nest jump columns in here
    st.subheader("jumps")
    c1, c2, c3, c4, c5 = st.columns(spec=[0.32, 0.17, 0.17, 0.17, 0.17])
    with c1:
        st.write("Toeloop")
        st.write("")
        st.write("Salchow")
        st.write("")
        st.write("Loop")
        st.write("")
        st.write("Flip")
        st.write("")
        st.write("Lutz")
        st.write("")
        st.write("Axel")
        st.write("")
        st.write("Euler")
    with c2:
        # create_jump_buttons(1, 1)
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


modal = Modal(
    "Spin Level",
    key="spin_level_modal",
    # Optional
    padding=20,
    max_width=744,
)
if modal.is_open():
    with modal.container():
        # insert id and level (from buttons) and close the modal
        spin_id = st.session_state["spin_id"]
        # Always set modal_selected_element to selected_element
        st.session_state.modal_selected_element = st.session_state.selected_element

        if st.button("B", key="spin_level_0"):
            click_button("", spin_id, 0)
            modal.close()
        if st.button("1", key="spin_level_1"):
            click_button("", spin_id, 1)
            modal.close()
        if st.button("2", key="spin_level_2"):
            click_button("", spin_id, 2)
            modal.close()
        if st.button("3", key="spin_level_3"):
            click_button("", spin_id, 3)
            modal.close()
        if st.button("4", key="spin_level_4"):
            click_button("", spin_id, 4)
            modal.close()


# spins and steps column
with col2:
    st.subheader("spins")
    c6, c7, c8, c9 = st.columns(4)
    with c6:
        st.write("Upright")
        st.write("")
        st.write("Layback")
        st.write("")
        st.write("Camel")
        st.write("")
        st.write("Sit")
        st.write("")
        st.write("Combo")
    with c7:
        if st.button(label="✓", key="us"):
            st.session_state["spin_id"] = "USp"
            modal.open()
        if st.button(label="✓", key="ls"):
            st.session_state["spin_id"] = "LSp"
            modal.open()
        if st.button(label="✓", key="cs"):
            st.session_state["spin_id"] = "CSp"
            modal.open()
        if st.button(label="✓", key="ss"):
            st.session_state["spin_id"] = "SSp"
            modal.open()
        if st.button(label="✓", key="cos"):
            st.session_state["spin_id"] = "CoSp"
            modal.open()
    with c8:
        if st.button(label="F", key="fus"):
            st.session_state["spin_id"] = "FUSp"
            modal.open()
        if st.button(label="F", key="fls"):
            st.session_state["spin_id"] = "FLSp"
            modal.open()
        if st.button(label="F", key="fcs"):
            st.session_state["spin_id"] = "FCSp"
            modal.open()
        if st.button(label="F", key="fss"):
            st.session_state["spin_id"] = "FSSp"
            modal.open()
        if st.button(label="F", key="fcos"):
            st.session_state["spin_id"] = "FCoSp"
            modal.open()
    with c9:
        if st.button(label="C", key="cus"):
            st.session_state["spin_id"] = "CUSp"
            modal.open()
        if st.button(label="C", key="cls"):
            st.session_state["spin_id"] = "CLSp"
            modal.open()
        if st.button(label="C", key="ccs"):
            st.session_state["spin_id"] = "CCSp"
            modal.open()
        if st.button(label="C", key="css"):
            st.session_state["spin_id"] = "CSSp"
            modal.open()
        if st.button(label="C", key="ccos"):
            st.session_state["spin_id"] = "CCoSp"
            modal.open()

    # -------------

    st.subheader("sequences")
    c11, c12, c13, c14, c15, c16 = st.columns([0.24, 0.12, 0.12, 0.12, 0.12, 0.12])
    with c11:
        st.write("Step")
        st.write("Choreo")
    with c12:
        if st.button(label="B", key="0step"):
            click_button("", "StSq", 0)
        if st.button(label="✓", key="choreo"):
            click_button("", "ChSq", 1)
    with c13:
        if st.button(label="1", key="1step"):
            click_button("", "StSq", 1)

    with c14:
        if st.button(label="2", key="2step"):
            click_button("", "StSq", 2)
    with c15:
        if st.button(label="3", key="3step"):
            click_button("", "StSq", 3)
    with c16:
        if st.button(label="4", key="4step"):
            click_button("", "StSq", 4)

st.divider()

# completed elements table
st.subheader("completed elements table")

if "modal_selected_element" in st.session_state:
    selected_element = st.selectbox(
        "select an element number",
        ([i for i in range(1, 8)]),
        index=st.session_state.modal_selected_element - 1,
    )
else:
    selected_element = st.selectbox(
        "select an element number", ([i for i in range(1, MAX_ELEMENTS + 1)])
    )

# If selected element is not in state, add it
if "selected_element" not in st.session_state:
    st.session_state.selected_element = selected_element
else:
    # If selected element is not the same as the one in state, update it
    st.session_state.selected_element = selected_element

if "sequence_counter" not in st.session_state:
    st.session_state.sequence_counter = 0

def write_to_database(element_list: list, execution_order: int):
    sequence_counter = 0
    for element in element_list:
        print("write element to database ", element.element, " ", element.level)
        with engine.connect() as conn:
            if element.level != None:
                sql = f"""INSERT INTO main.score(spin_id, order_executed, spin_level, user_id, program_id) 
                VALUES('{element.element}', '{execution_order}', '{element.level}', '{st.session_state.user_id}', '{st.session_state.program_id}')"""
            else:
                sql = f"""INSERT INTO main.score(jump_id, order_executed, user_id, program_id) 
                VALUES('{element.element}', '{execution_order}', '{st.session_state.user_id}', '{st.session_state.program_id}')"""
            conn.execute(text(sql))
            conn.commit()
        sequence_counter += 1
        # print("sequence counter: ", sequence_counter)
    with engine.connect() as conn:
        sql2 = f"""
            INSERT INTO main.readable_elements(user_id, program_id, element, order_executed)
            VALUES('{st.session_state.user_id}', '{st.session_state.program_id}', '{element_string}', '{execution_order}')
        """
        conn.execute(text(sql2))
        conn.commit()
    print("Changing state to true")
    st.session_state.changed_data = True
    st.session_state.sequence_counter = sequence_counter

base_data = {
    "execution_order": [i for i in range(1, MAX_ELEMENTS + 1)],
    "element_list": [[], [], [], [], [], [], []],
    "element_string": ["", "", "", "", "", "", ""],
}

# If the dataframe is not in state, then create it
if "completed_elements" not in st.session_state:
    st.session_state.completed_elements = pd.DataFrame(
        base_data, columns=["execution_order", "element_list", "element_string"]
    )

element_column = st.session_state.completed_elements["element_list"][
    selected_element - 1
]
element_string = "+".join(element.print_element() for element in element_column)
# print(element_string)

# If selected element is less than the max, display a button to increment it
if st.session_state.selected_element < MAX_ELEMENTS:
    # Create a button to increment the selected element
    if st.button("Increment Element", use_container_width=True):
        if "modal_selected_element" in st.session_state:
            st.session_state.modal_selected_element += 1
        else:
            st.session_state.modal_selected_element = 2
        row = st.session_state.completed_elements.iloc[selected_element - 1]
        write_to_database(row["element_list"], row["execution_order"])
        st.rerun()
else:
    if st.button("Submit", use_container_width=True):
        row = st.session_state.completed_elements.iloc[selected_element - 1]
        write_to_database(row["element_list"], row["execution_order"])

# Update the dataframe with the new element
st.session_state.completed_elements.loc[selected_element - 1, "element_string"] = (
    element_string
)
st.dataframe(
    st.session_state.completed_elements.drop(columns=["element_list"]),
    hide_index=True,
    use_container_width=True,
    column_config={
        "execution_order": "Execution Order",
        # "element_list": None,
        "element_string": "Element",
    },
)

if st.button("submit", key="submit-techspecialist"):
    st.snow()


# streamlit example for highlighting dataframe: ---------

# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

# st.dataframe(df.style.highlight_max(axis=0))
