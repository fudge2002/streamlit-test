import streamlit as st

st.set_page_config(page_title="Sticky Header Demo", layout="wide")

# ----------------------------
# Sticky Header CSS
# ----------------------------
st.markdown("""
    <style>
        /* Sticky header container */
        .sticky-header {
            position: sticky;
            top: 0;
            background-color: white;
            padding: 10px 0 15px 0;
            z-index: 999;
            border-bottom: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Sticky Header UI
# ----------------------------
st.markdown('<div class="sticky-header">', unsafe_allow_html=True)

st.subheader("Sticky Filters")

col1, col2, col3 = st.columns(3)
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"])
with col2:
    search = st.text_input("Search")
with col3:
    apply = st.button("Apply Filters")

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Scrollable content
# ----------------------------
st.title("Scroll Down to Test Sticky Header")

for i in range(1, 80):
    st.write(f"### Item {i}")
    st.write(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    )