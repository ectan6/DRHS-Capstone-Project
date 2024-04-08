import pandas as pd
import streamlit as st
from menu import menu_with_redirect
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()

menu_with_redirect()

database_name = "postgres"
postgres_password = os.getenv("POSTGRES_PASSWORD")
engine = create_engine(
    f"postgresql+psycopg2://postgres:{postgres_password}@localhost:5432/{database_name}"
)

# if st.session_state.role not in ["admin", "super-admin"]:
#     st.warning("You do not have permission to view this page.")
#     st.stop()

with engine.connect() as conn:
    # get date from main.competitions "date" column
    sql = f"SELECT * FROM main.competitions WHERE competition_id = {st.session_state.competition_id}"
    competition_data = pd.read_sql(sql, conn)
    competition_date = competition_data["date"].values[0]

st.title(f"Planned Program Components for {st.session_state.user_name}")
st.subheader(f"Event: {st.session_state.competition_name} on {competition_date}")

# something to consider: multiple tabs for multiple programs (short and long) ?
# t1, t2 = st.tabs(["short program", "long program"])
# with t1:
#     st.write("sp")
# with t2:
#     st.write("lp")

first_jump = False
if "first_jump" not in st.session_state:
    st.session_state.first_jump = first_jump

def write_to_ppc_table(code: str, order: int):
    with engine.connect() as conn:
        # need to add user_id and program_id at some point
        sql = f"INSERT INTO main.ppc(element_code, element_order, user_id, program_id) VALUES('{code}', '{order}', '{st.session_state.user_id}', '{st.session_state.program_id}')"
        print(f"successfully written {code} to database")
        conn.execute(text(sql))
        conn.commit()


def create_jump_buttons(num_rotations: int, element_number: int):
    if st.button(label=str(num_rotations), key=f"{num_rotations}toe-{element_number}"):
        ppc_i.append(f"{num_rotations}T")
        write_to_ppc_table(f"{num_rotations}T", element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}sal-{element_number}"):
        ppc_i.append(f"{num_rotations}S")
        write_to_ppc_table(f"{num_rotations}S", element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}loop-{element_number}"):
        ppc_i.append(f"{num_rotations}Lo")
        write_to_ppc_table(f"{num_rotations}Lo", element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}flip-{element_number}"):
        ppc_i.append(f"{num_rotations}F")
        write_to_ppc_table(f"{num_rotations}F", element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}lz-{element_number}"):
        ppc_i.append(f"{num_rotations}Lz")
        write_to_ppc_table(f"{num_rotations}Lz", element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}axel-{element_number}"):
        ppc_i.append(f"{num_rotations}A")
        write_to_ppc_table(f"{num_rotations}A", element_number)
    if st.session_state.first_jump == True:
        if st.button(label=str(num_rotations), key=f"{num_rotations}eu-{element_number}"):
            ppc_i.append(f"{num_rotations}Eu")
            write_to_ppc_table(f"{num_rotations}Eu", element_number)

def create_spin_buttons(variation: int, element_number: int):
    lab = ""
    lab_for_db = ""
    if variation == 1:
        lab = "✓"
    elif variation == 2:
        lab = "F"
        lab_for_db = "F"
    elif variation == 3:
        lab = "C"
        lab_for_db = "C"

    if st.button(label=lab, key=f"{str(variation)}u-{element_number}"):
        # oopsies i need to change the variation from number to string (like in create_spin_buttons function)
        write_to_ppc_table(f"{lab_for_db}USp", element_number)
    if st.button(label=lab, key=f"{str(variation)}l-{element_number}"):
        write_to_ppc_table(f"{lab_for_db}LSp", element_number)
    if st.button(label=lab, key=f"{str(variation)}c-{element_number}"):
        write_to_ppc_table(f"{lab_for_db}CSp", element_number)
    if st.button(label=lab, key=f"{str(variation)}s-{element_number}"):
        write_to_ppc_table(f"{lab_for_db}SSp", element_number)
    if st.button(label=lab, key=f"{str(variation)}co-{element_number}"):
        write_to_ppc_table(f"{lab_for_db}CoSp", element_number)


def ppc_options(element_number: int):
    # st.write("these are the element options")
    c1, c2, c3 = st.columns([.4, .375, .25])
    with c1:
        st.subheader("jumps")
        c4, c5, c6, c7, c8 = st.columns([.25, .15, .15, .15, .15])
        with c4:
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
        with c5:
            st.session_state.first_jump = True
            create_jump_buttons(1, element_number)
            st.session_state.first_jump = False
        with c6:
            create_jump_buttons(2, element_number)
        with c7:
            create_jump_buttons(3, element_number)
        with c8:
            create_jump_buttons(4, element_number)

    with c2:
        st.subheader("spins")
        # could change all to checkboxes and implement logic like if (fly and upright) then code FUSp
        c9, c10, c11, c12 = st.columns([.35, .15, .15, .15])
        with c9:
            st.write("Upright")
            st.write("")
            st.write("Layback")
            st.write("")
            st.write("Camel")
            st.write("")
            st.write("Sit")
            st.write("")
            st.write("Combination")
        with c10:
            create_spin_buttons(1, element_number)
        with c11:
            create_spin_buttons(2, element_number)
        with c12:
            create_spin_buttons(3, element_number)

    with c3:
        st.subheader("sequences")
        if st.button(label="Step Sequence", key=f"stsq{element_number}", use_container_width=True):
            write_to_ppc_table("StSq", element_number)
        if st.button(label="Choreographic Sequence", key=f"chsq{element_number}", use_container_width=True):
            write_to_ppc_table("ChSq", element_number)
    
    print(ppc_i)
    ppc_i_string = "+".join(i for i in ppc_i)
    print(ppc_i_string)


# I want to have the label default to "enter an element" and then change to the name of the element
# when the user selects an element - use some function

for i in range(1, 8):
    with st.expander(f"Element {i}"):
        ppc_i = []
        ppc_options(i)


st.subheader("Your Planned Program Components:")
for i in range(1, 8):
    # st.write(f"Element {i}")
    with engine.connect() as conn:
        sql = f"SELECT * FROM main.ppc WHERE user_id = '{st.session_state.user_id}' and program_id = '{st.session_state.program_id}' and element_order = {i}"
        ppc_data = pd.read_sql(sql, conn)
        selected_ppc_list = []
        for j in range(len(ppc_data)):
            selected_ppc_list.append(ppc_data["element_code"].values[j])
        selected_ppc = " + ".join(selected_ppc_list)
        st.write(i, ". ", selected_ppc)

if st.button(label="Submit", key="submit-ppc"):
    st.balloons()
    st.success('PPC succesffuly submitted!')