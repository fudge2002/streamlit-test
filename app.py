import streamlit as st

st.set_page_config(page_title="Sticky Header Demo", layout="wide")

# -------------------------------
# ✅ Make a fixed-position header
# -------------------------------
st.markdown("""
    <style>
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 90px;
            background-color: white;
            border-bottom: 1px solid #ddd;
            z-index: 9999;
            padding: 10px 20px;
        }
        /* Push content down so it doesn't hide behind header */
        .main > div {
            padding-top: 110px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Fake div for fixed header container
st.markdown('<div class="fixed-header">', unsafe_allow_html=True)

# --------------------------------
# ✅ Widgets INSIDE sticky header
# --------------------------------
col1, col2, col3 = st.columns(3)
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"], key="cat")
with col2:
    search = st.text_input("Search", key="search")
with col3:
    apply = st.button("Apply Filters", key="apply")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------
# ✅ Long scrollable content
# -------------------------------
st.title("Scroll to test sticky header")

for i in range(1, 60):
    st.write(f"### Item {i}")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 8)