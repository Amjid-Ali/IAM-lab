import streamlit as st

# Set the page width
st.set_page_config(page_title="Yejin Choi - Streamlit Webpage", layout="wide")

# Title
st.title("Yejin Choi - Streamlit Webpage")

# Create a three-column layout with some spacing
col1, col2, col3 = st.columns([3, 3, 3], gap="large")

# Information in the left column
with col1:
    # Align content to the left
    st.markdown('<div style="text-align: left; margin-left: 40px;">', unsafe_allow_html=True)

    st.write("Wissner-Slivka Chair")
    st.write("MacArthur Fellow")

    st.write("Office: 578 Allen Center")
    st.write("Fax: 206-685-2969")
    st.write("Email: [yejin@cs.washington.edu](mailto:yejin@cs.washington.edu)")

    # Close the alignment div
    st.markdown('</div>', unsafe_allow_html=True)

# Contact Information in the middle column
with col2:
    st.subheader("Contact Information:")
    st.write("Paul G. Allen School of Computer Science & Engineering")
    st.write("University of Washington")
    st.write("Box 352350")
    st.write("185 E Stevens Way NE")
    st.write("Seattle, WA 98195-2350")

    st.write("Allen Institute for Artificial Intelligence")
    st.write("2157 N Northlake Way, Suite 110")
    st.write("Seattle, WA 98103")

# Image in the right column with spacing
with col3:
    st.markdown('<div style="text-align: right; margin-right: 40px;">', unsafe_allow_html=True)
    st.subheader("Image:")
    st.image("logo192.png", caption="Placeholder Image", use_column_width=True)
    # Close the alignment div
    st.markdown('</div>', unsafe_allow_html=True)
