import streamlit as st

st.set_page_config(page_title="Sticky Header", layout="wide")

# ----------------------------------------------------
# ✅ CSS that makes a chosen container sticky using :has()
# ----------------------------------------------------
st.markdown("""
<style>

div[data-testid="stVerticalBlock"] div:has(div.fixed-header-marker) {
    position: sticky;
    top: 0;
    z-index: 999;
    background: var(--background-color);
    padding-bottom: 8px;
    padding-top: 8px;
    border-bottom: 1px solid #ddd;
}

.fixed-header-marker { height: 0px; }

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# ✅ This container becomes sticky because of the marker
# ----------------------------------------------------
sticky = st.container()
sticky.markdown("<div class='fixed-header-marker'></div>", unsafe_allow_html=True)

# ✅ Horizontal layout (your fake table row)
col1, col2, col3 = sticky.columns([1, 2, 1])
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"])
with col2:
    search = st.text_input("Search…")
with col3:
    st.button("Apply Filters")

# ----------------------------------------------------
# ✅ Long scrollable content
# ----------------------------------------------------
st.title("Scrollable content")
for i in range(60):
    st.write(f"### Row {i}")
    st.write("Lorem ipsum dolor sit amet " * 8)