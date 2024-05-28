import streamlit as st
from login_ui import login_ui


def main():
    if st.session_state.get("authenticated", False):
        st.title("Main Page: Welcome, " + st.session_state["display_name"])
    else:
        login_ui()


if __name__ == "__main__":
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    main()
