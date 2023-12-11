# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="Aplikasi Kategori Berita | Klasifikasi Berita Radar Jatim", page_icon="📺")
    st.write("Oleh | Aulya Miftahkhul Hikmah | 200411100050")
    col1, col2 = st.columns(2)

    with col1:

        st.image("assets/banner.jpg", use_column_width=True)

    with col2:
        st.subheader("News Classification: Aplikasi Kategori untuk Berita")
        st.caption("Berita umumnya dikategorikan menjadi beberapa jenis kategori seperti pendidikan, sosial, religi dan kategori lainnya. Dengan news classification ini kita dapat menemukan jenis kategori berita yang sesuai dengan isi berita tersebut.")

    news_text = st.text_area(
        "Masukkan Isi Berita", key="input_text", height=250)

    if st.button("Cari Kategori"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write('Berita yang anda masukkan termasuk dalam kategori: ')
                if text == "pendidikan":
                    st.info(text, icon="🧑‍🏫")
                    url = "https://radarjatim.id/?s=berita+pendidikan+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait pendidikan 🔎 [Berita pendidikan hari ini](%s)'  %url)
                elif text == "sosial":
                    st.info(text, icon="🚣")
                    url = "https://radarjatim.id/?s=berita+sosial+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait sosial 🔎 [Berita sosial hari ini](%s)'  %url)
                elif text == "religi":
                    st.info(text, icon="💸")
                    url = "https://radarjatim.id/?s=berita+religi+hari+ini"
                    st.write(
                        'Baca juga berita terbaru terkait religi 🔎 [Berita religi hari ini](%s)'  %url)
                
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu', icon='🤧')


if __name__ == "__main__":
    main()
