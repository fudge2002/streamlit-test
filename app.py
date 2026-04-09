st.markdown("""
<style>

    /* ✅ MAIN sticky container selector */
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header-marker) {
        position: sticky;
        top: 0;
        z-index: 9999;

        /* Background of the sticky bar */
        background: rgba(0, 0, 0, 0.70);
        backdrop-filter: blur(6px);

        /* Removes gaps */
        padding-top: 6px !important;
        padding-bottom: 6px !important;
        margin: 0 !important;

        /* Remove bottom border entirely */
        border: none !important;
        border-bottom: 0 !important;
    }

    /* ✅ Remove Streamlit's wrapper border + padding */
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header-marker) > div {
        padding: 0 !important;
        margin: 0 !important;
        border: none !important;
    }

    /* ✅ Remove Streamlit element-container padding */
    div[data-testid="stElementContainer"] {
        padding: 0 !important;
        margin: 0 !important;
    }

    .fixed-header-marker { height: 0px; }

</style>
""", unsafe_allow_html=True)