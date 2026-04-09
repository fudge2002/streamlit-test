import streamlit as st

st.set_page_config(page_title="Sticky Header Demo", layout="wide")

# -------------------------------------
# ✅ Sticky header with transparent bg
# -------------------------------------
st.markdown("""
    <style>
        .fixed-header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 9999;
            padding: 8px 20px 4px 20px;

            /* ✅ No background (keeps Streamlit theme look) */
            background: transparent !important;
            backdrop-filter: blur(8px); /* optional: subtle glass effect */
        }

        /* ✅ Push down the main content so it's not hidden */
        .main > div {
            padding-top: 90px !important;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Sticky top bar
st.markdown('<div class="fixed-header">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"], key="cat")
with col2:
    search = st.text_input("Search", key="search")
with col3:
    apply = st.button("Apply Filters", key="apply")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------
# ✅ Scrollable content
# -------------------------------------
st.title("Scroll to test the sticky header")

for i in range(1, 60):
    st.write(f"### Item {i}")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10)