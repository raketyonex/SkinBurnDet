import streamlit as st
from burnalyze import Analyzer


st.set_page_config("BurnAlyze | detect & classify", initial_sidebar_state="expanded")
st.markdown(f"<style>{open("stylee/style.css").read()}</style>", unsafe_allow_html=True)

st.header("BurnAlyze")
st.subheader("Detect and classify burn severity levels with AI-driven image segmentation.")

b1, b2 = st.columns([4,2])
with b1:
    img = st.file_uploader("**Skin Image**", type=['jpg','png'])
    st.write("")
with b2:
    st.write("press to start!")
    button = st.button("**Identification**", type="primary", use_container_width=True)

if button:
    if img and type is not None:
        segment, time = Analyzer(img, type)

        st.write(f'Inference Time: **{time}ms**')
        c1, c2 = st.columns(2)
        with c1:
            st.image(image=img, caption="original image")
        with c2:
            st.image(image=segment, caption="detected image")
