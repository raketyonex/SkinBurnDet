import streamlit as st
from burnalyze import Analyzer


st.set_page_config("BurnAlyze | detect & classify", initial_sidebar_state="expanded")
st.markdown(f"<style>{open("stylee/style.css").read()}</style>", unsafe_allow_html=True)

st.header("BurnAlyze")
st.subheader("Detect and classify burn severity levels.")

_, container, _ = st.columns([2,8,2])
with container:
    img = st.file_uploader("**Skin Image**", type=['jpg','png'])
    st.write("")
    button = st.button("**Identification**", type="primary", use_container_width=True)
    st.write("")

if button:
    if img and type is not None:
        segment, time = Analyzer(img, type)

        st.write(f'Inference Time: **{time}ms**')
        c1, c2 = st.columns(2)
        with c1:
            st.image(image=img, caption="original image")
        with c2:
            st.image(image=segment, caption="detected image")
