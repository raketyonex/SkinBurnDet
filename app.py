import streamlit as st
from detect import Detect


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

img_result = None

with st.container(border=True):
    st.write("**🔍 Analisa Luka Bakar**")

    c1, c2 = st.columns((2), vertical_alignment="top", gap="medium", border=True)

    with c1:
        img_source = st.file_uploader("**Upload Gambar**", type=["jpg", "jpeg", "png"])

        st.write("")
        if st.button("**Deteksi**", type="primary", use_container_width=True):
            if img_source is not None:
                img_result = Detect(img_source)
            else:
                st.error(
                    "Silakan unggah gambar terlebih dahulu sebelum melakukan prediksi."
                )

    with c2:
        if img_source:
            st.image(img_source, caption="Gambar Asli", use_container_width=True)
        else:
            st.info("**Gambar Asli** Akan Muncul Di Sini!")

    st.write("")
    if img_result:
        st.image(img_result, caption="Hasil Deteksi", use_container_width=True)
    else:
        st.info("**Hasil Deteksi** Akan Muncul Di Sini!")
