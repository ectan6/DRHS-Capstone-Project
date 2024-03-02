import streamlit as st
from menu import menu_with_redirect

menu_with_redirect()

if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("You do not have permission to view this page.")
    st.stop()

st.markdown(f"You are currently logged with the role of {st.session_state.role}.")

st.title("Evemt: (title of the event - date, time?)")

# something to consider: multiple tabs for multiple programs (short and long) ?


def ppc_options():
    st.write("these are the element options")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("jumps")
    with c2:
        st.write("spins")
    with c3:
        st.write("steps")


# I want to have the label default to "enter an element" and then change to the name of the element
# when the user selects an element - use some function
with st.expander("1"):
    ppc_options()
with st.expander("2"):
    ppc_options()
with st.expander("3"):
    ppc_options()
with st.expander("4"):
    ppc_options()
with st.expander("5"):
    ppc_options()
with st.expander("6"):
    ppc_options()
with st.expander("7"):
    ppc_options()

st.button("submit")