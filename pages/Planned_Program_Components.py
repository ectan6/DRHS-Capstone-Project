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

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.title(f"Planned Program Components for {st.session_state.user_name}")
st.title(f"Event: {st.session_state.competition_name} - date, time")

# something to consider: multiple tabs for multiple programs (short and long) ?
# t1, t2 = st.tabs(["short program", "long program"])
# with t1:
#     st.write("sp")
# with t2:
#     st.write("lp")

first_jump = False
if "first_jump" not in st.session_state:
    st.session_state.first_jump = first_jump

if "expander_label" not in st.session_state:
    st.session_state.expander_label = ""
if "combo_index" not in st.session_state:  
    st.session_state.combo_index = 1

def update_expander_label(code: str):
    # if st.session_state.combo_index == 1:
    #     st.session_state.expander_label = code
    #     print(f"expander label is {st.session_state.expander_label}")
    # else: 
    st.session_state.expander_label += f" + {code}"
    print(f"expander label is {st.session_state.expander_label} +")
    # i worked for like 30 mins 4/2/24
    st.session_state.combo_index += 1


def write_to_ppc_table(code: str, order: int):
    with engine.connect() as conn:
        # need to add user_id and program_id at some point
        sql = f"INSERT INTO main.ppc(element_code, element_order, user_id, program_id) VALUES('{code}', '{order}', '{st.session_state.user_id}', '{st.session_state.program_id}')"
        print(f"successfully written {code} to database")
        conn.execute(text(sql))
        conn.commit()


def create_jump_buttons(num_rotations: int, element_number: int):
    code = ""
    # , on_click=
    if st.button(label=str(num_rotations), key=f"{num_rotations}toe-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}T"]):
        code = f"{num_rotations}T"
        write_to_ppc_table(code, element_number)
        # st.session_state.exapnder_label += f"{num_rotations}toe-{element_number}"

    if st.button(label=str(num_rotations), key=f"{num_rotations}sal-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}S"]):
        code = f"{num_rotations}S"
        write_to_ppc_table(code, element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}loop-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}Lo"]):
        code = f"{num_rotations}Lo"
        write_to_ppc_table(code, element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}flip-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}F"]):
        code = f"{num_rotations}F"
        write_to_ppc_table(code, element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}lz-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}Lz"]):
        code = f"{num_rotations}Lz"
        write_to_ppc_table(code, element_number)
    if st.button(label=str(num_rotations), key=f"{num_rotations}axel-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}A"]):
        code = f"{num_rotations}A"
        write_to_ppc_table(code, element_number)
    if st.session_state.first_jump == True:
        if st.button(label=str(num_rotations), key=f"{num_rotations}eu-{element_number}", on_click=update_expander_label, args=[f"{num_rotations}Eu"]):
            code = f"{num_rotations}Eu"
            write_to_ppc_table(code, element_number)


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
    st.write("these are the element options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("jumps")
        c4, c5, c6, c7, c8 = st.columns(5)
        with c4:
            st.write("Toeloop")
            st.write("Salchow")
            st.write("Loop")
            st.write("Flip")
            st.write("Lutz")
            st.write("Axel")
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
        st.write("spins")
        # could change all to checkboxes and implement logic like if (fly and upright) then code FUSp
        c9, c10, c11, c12 = st.columns(4)
        with c9:
            st.write("Upright")
            st.write("Layback")
            st.write("Camel")
            st.write("Sit")
            st.write("Combination")
        with c10:
            create_spin_buttons(1, element_number)
        with c11:
            create_spin_buttons(2, element_number)
        with c12:
            create_spin_buttons(3, element_number)

    with c3:
        st.write("Sequences")
        if st.button(label="Step Sequence", key=f"stsq{element_number}"):
            write_to_ppc_table("StSq", element_number)
        if st.button(label="Choreographic Sequence", key=f"chsq{element_number}"):
            write_to_ppc_table("ChSq", element_number)


# I want to have the label default to "enter an element" and then change to the name of the element
# when the user selects an element - use some function

for i in range(1, 8):
    st.session_state.expander_label = f"{i}"
    with st.expander(st.session_state.expander_label):
        st.session_state.combo_index = 1
        ppc_options(i)


st.button("submit", key="submit-ppc")
