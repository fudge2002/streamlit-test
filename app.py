import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# HTML wrapper for sticky bar
sticky_html = """
<div style="
    position:sticky;
    top:0;
    z-index:9999;
    padding:10px;
    background: var(--background-color);
    border-bottom: 1px solid #ddd;">
    <iframe srcdoc="
        <html>
        <body style='margin:0; font-family:sans-serif;'>
            <form>
                Category:
                <select id='cat'>
                    <option>All</option>
                    <option>A</option>
                    <option>B</option>
                    <option>C</option>
                </select>

                <input id='search' placeholder='Search...' />

                <button type='button'>Apply</button>
            </form>
        </body>
        </html>
    " width="100%" height="60" style="border:none;"></iframe>
</div>
"""

components.html(sticky_html, height=90)

# content
st.title("Scroll down")
for i in range(80):
    st.write(f"### Item {i}")
    st.write("Lorem ipsum dolor sit amet " * 20)