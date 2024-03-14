import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Event: (title of the event - date, time?)")

# something to consider: multiple tabs for multiple programs (short and long) ? 
# t1, t2 = st.tabs(["short program", "long program"])
# with t1:
#     st.write("sp")
# with t2:
#     st.write("lp")

first_jump = False
if "first_jump" not in st.session_state:
    st.session_state.first_jump = first_jump
else:
    st.session_state.first_jump = first_jump

def create_jump_buttons(num_rotations: int, element_number: int):
    if st.button(label=str(num_rotations), key=f"{num_rotations}toe-{element_number}"):
        st.balloons()
    if st.button(label=str(num_rotations), key=f"{num_rotations}sal-{element_number}"):
        st.balloons()
    if st.button(label=str(num_rotations), key=f"{num_rotations}loop-{element_number}"):
        st.balloons()
    if st.button(label=str(num_rotations), key=f"{num_rotations}flip-{element_number}"):
        st.balloons()
    if st.button(label=str(num_rotations), key=f"{num_rotations}lz-{element_number}"):
        st.balloons()
    if st.button(label=str(num_rotations), key=f"{num_rotations}axel-{element_number}"):
        st.balloons()
    if st.session_state.first_jump == True:
        if st.button(label=str(num_rotations), key=f"{num_rotations}eu-{element_number}"):
            st.balloons()

def create_spin_buttons(variation: int, element_number: int):
    lab = ""
    if variation == 1:
        lab = "✓"
    elif variation == 2:
        lab = "F"
    elif variation == 3:
        lab = "C"
    
    if st.button(label=lab, key = f"{str(variation)}u-{element_number}"):
        st.snow()
    if st.button(label=lab, key = f"{str(variation)}l-{element_number}"):
        st.snow()
    if st.button(label=lab, key = f"{str(variation)}c-{element_number}"):
        st.snow()
    if st.button(label=lab, key = f"{str(variation)}s-{element_number}"):
        st.snow()
    if st.button(label=lab, key = f"{str(variation)}co-{element_number}"):
        st.snow()

def ppc_options(element_number: int):
    st.write("these are the element options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("jumps")
        # maybe for 3 jump combinations I can make it so that if they click it, it refreshes each time they click a jump
        # ex: click 3 jump combination. click first jump, code appears on dropdown label, repeat 3 times, then 
        # doesn't allow any more jumps to be clicked?
        # nah just do what I did for the tech specialist page
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
            # something silly for now hehe
            st.balloons()
        if st.button(label="Choreographic Sequence", key=f"chsq{element_number}"):
            st.snow()

# I want to have the label default to "enter an element" and then change to the name of the element
# when the user selects an element - use some function
with st.expander("1"):
    ppc_options(1)
with st.expander("2"):
    ppc_options(2)
with st.expander("3"):
    ppc_options(3)
with st.expander("4"):
    ppc_options(4)
with st.expander("5"):
    ppc_options(5)
with st.expander("6"):
    ppc_options(6)
with st.expander("7"):
    ppc_options(7)

st.button("submit")