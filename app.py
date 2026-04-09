import streamlit as st

st.set_page_config(page_title="Sidebar Sticky Demo", layout="wide")

# -----------------------------
# ✅ Sticky filters in sidebar
# -----------------------------
st.sidebar.header("Filters")

category = st.sidebar.selectbox("Category", ["All", "A", "B", "C"])
search = st.sidebar.text_input("Search…")
apply = st.sidebar.button("Apply Filters")

# -----------------------------
# ✅ Scrollable main content
# -----------------------------
st.title("Scrollable Content")

for i in range(1, 60):
    st.write(f"### Item {i}")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10)