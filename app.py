import streamlit as st

st.set_page_config(page_title="Sticky Header", layout="wide")

# ----------------------------------------------------
# ✅ Sticky header styling improvements
# ----------------------------------------------------
st.markdown("""
<style>

    /* Make the sticky container actually sticky */
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header-marker) {
        position: sticky;
        top: 0;
        z-index: 9999;

        /* ✅ Solid background so text below doesn't show through */
        background: rgba(0, 0, 0, 0.70); 

        /* ✅ Optional: glass/blur effect */
        backdrop-filter: blur(6px);

        /* ✅ Remove white gap effect */
        margin-bottom: 0;
        padding-top: 8px;
        padding-bottom: 8px;

        /* ✅ Divider line at bottom */
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
    }

    /* Invisible marker to target this container */
    .fixed-header-marker { height: 0px; }

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# ✅ Sticky header container
# ----------------------------------------------------
sticky = st.container()
sticky.markdown("<div class='fixed-header-marker'></div>", unsafe_allow_html=True)

# ✅ Horizontal layout (fake table row)
col1, col2, col3 = sticky.columns([1, 2, 1])
with col1:
    category = st.selectbox("Category", ["All", "A", "B", "C"])
with col2:
    search = st.text_input("Search…")
with col3:
    st.button("Apply Filters")

# ----------------------------------------------------
# ✅ Scrollable content
# ----------------------------------------------------
st.title("Scrollable content")
for i in range(60):
    st.write(f"### Row {i}")
    st.write("Lorem ipsum dolor sit amet " * 8)