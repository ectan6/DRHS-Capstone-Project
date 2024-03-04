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

def ppc_options(element_number: int):
    st.write("these are the element options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("jumps")
        # maybe for 3 jump combinations I can make it so that if they click it, it refreshes each time they click a jump
        # ex: click 3 jump combination. click first jump, code appears on dropdown label, repeat 3 times, then 
        # doesn't allow any more jumps to be clicked?
    with c2:
        st.write("spins")
        # could change all to checkboxes and implement logic like if (fly and upright) then code FUSp
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