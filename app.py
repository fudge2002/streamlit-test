import streamlit as st

st.set_page_config(page_title="Sticky Header Demo", layout="wide")

# --------------------------------------------------
# ✅ CSS that makes the container holding the filters sticky
# --------------------------------------------------
st.markdown("""
    <style>
        /* Make the first container sticky */
        .stSticky > div {
            position: sticky;
            top: 0;
            z-index: 999;
            background-color: white;
            padding-top: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# ✅ Sticky container
# --------------------------------------------------
sticky = st.container()
with sticky:
    st.markdown("### 🔍 Filters (Sticky Header)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("Category", ["All", "A", "B", "C"])
    with col2:
        search = st.text_input("Search")
    with col3:
        apply = st.button("Apply")

# --------------------------------------------------
# ✅ Scrollable content
# --------------------------------------------------
st.title("Scroll to see the sticky header in action")

for i in range(1, 80):
    st.write(f"### Item {i}")
    st.write("Long content line… " * 10)