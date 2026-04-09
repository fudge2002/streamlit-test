import streamlit as st

st.set_page_config(page_title="Sticky Row Demo", layout="wide")

# ------------------------------------------------
# ✅ Sticky row CSS (keeps Streamlit theme colors)
# ------------------------------------------------
st.markdown("""
    <style>
        /* Sticky row bar */
        .sticky-row {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 10000;
            padding: 6px 16px;
            background-color: var(--background-color);  /* uses Streamlit theme */
            border-bottom: 1px solid #ddd;
        }

        /* Push main content down so it's not hidden */
        .main > div {
            padding-top: 85px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# ✅ Sticky row with widgets (fake table row)
# ------------------------------------------------
st.markdown('<div class="sticky-row">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"], key="cat")
with col2:
    search = st.text_input("Search…", key="search")
with col3:
    apply = st.button("Apply Filters", key="apply")

st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------------------------
# ✅ Long scrollable content
# ------------------------------------------------
st.title("Scrollable Content Area")

for i in range(1, 60):
    st.write(f"### Row {i}")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10)