import streamlit as st 
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

data2018=pd.read_excel('Data_2018.xlsx')
data2019=pd.read_excel('Data_2019.xlsx')


with st.sidebar:
    st.title("Pariwisata Indonesia")
    tahun = st.radio("", ("Pendahuluan", "2018", "2019", "Analisa Data", "Simpulan"))
    tickerData = ([data2018, data2019])
if tahun == "Analisa Data":
    st.subheader("Untuk mencoba mencari target, data yang ada dilakukan clustering untuk melihat kemiripan kebangsaan dengan KMeans=4 (sesuai uji Elbow Method), dengan hasil:")
    st.write("Hasil 2018")
    st.image("cluster2018.png")
    
    st.write("Hasil 2019")
    st.image("cluster2019.png")
    st.subheader("Dengan Decision Tree sebagai berikut")
    
    x1, x2 = st.columns (2)
    with x1:
        st.write("2018")
        st.image("tree2018.png")
    with x2:
        st.write("2019")
        st.image("tree2019.png")
    
    
if tahun == "Pendahuluan":
    st.title("Siapa Target Wisatawan Mancanegara Sekarang Setelah Covid-19 Menjadi Endemik")
    st.write("Pandemi Covid-19 pada tahun 2020, menutup Indonesia dan seluruh negara dari kedatangan wisatawan mancanegara, akibatnya sektor pariwisata Indonesia, bahkan dunia mengalami kemunduran, sektor ini menjadi sektor yang paling terpengaruh dibandingkan dengan sektor lainnya.")
    st.write("Data dari Badan Pusat statistik (BPS) menunjukkan dari jumlah Wisatawan Mancanegara sejumlah 16.106.954 pada tahun 2019, turun berturut-turut menjadi 4.052.923 dan 1.557.530 di tahun 2020 dan 2021 setelah terbitnya kebijakan pemerintah PPKM dalam rangka penyebaran Covid-19. Saat ini ketika kunjungan luar negeri sudah diperbolehkan kembali, saatnya Indonesia fokus dalam meningkatkan kunjungan wisatawan mancanegara demi meningkatkan perekonomian dan meningkatkan cadangan devisa.")
    st.subheader("Lalu bagaimana cara menentukan siapa atau negara mana yang seharusnya menjadi prioritas untuk dijadikan target wisatawan mancanegara?")
    st.write("Untuk menentukan itu, salah satunya caranya adalah, kembali ke data sebelum pandemik atau tahun 2018 dan 2019 saat kondisi masih normal dan kunjungan wisatawan mancanegara belum mengalami penurunan")
    st.write("Dalam laman BPS, ada 3 cara mengukur dampak wisatawan mancanegara yang datang ke Indonesia:")
    st.write("1. Jumlah Kunjungan (orang)")
    st.write("2. Rerata lama tinggal (hari)")
    st.write( "3. Rerata Pengeluaran (US$)")
    st.subheader("mari kita cermati data wisatawan pada tahun tersebut dengan radio button di sebelah kiri anda")

if tahun == "2018":
    kunjungantop5=data2018.sort_values(by='kunjungan_2018', ascending=False).head()
    expendtop5=data2018.sort_values(by='expend_2018', ascending=False).head()
    reratatop5=data2018.sort_values(by='Rerata_2018', ascending=False).head()
    st.subheader("Ketika kita cermati data tahun 2018, ternyata ketiga data tersebut tidak didominasi oleh negara yang sama")
    st.subheader('Top 5 Jumlah  Kunjungan ')
    a1, a2 = st.columns(2)
    with a1:
        st.table(kunjungantop5.drop(['expend_2018', 'Rerata_2018'], axis=1))
    with a2:
        st.image('top52018.png')
    st.subheader('Top 5 Rerata Pengeluaran ')
    
    b1, b2 = st.columns(2)
    with b1:
        st.table(expendtop5.drop(['kunjungan_2018', 'Rerata_2018'], axis=1))
    with b2:
        st.image('expend52018.png')
    st.subheader('Top 5 Rerata Lama Tinggal ')
    
    c1, c2 = st.columns(2)
    with c1:
        st.table(reratatop5.drop(['expend_2018', 'kunjungan_2018'], axis=1))
    with c2:
        st.image('rerata2018.png')

if tahun == "2019":
    kunjungan2019=data2019.sort_values(by='kunjungan_2019', ascending=False).head()
    expend2019=data2019.sort_values(by='expend_2019', ascending=False).head()
    rerata2019=data2019.sort_values(by='Rerata_2019', ascending=False).head()
    st.subheader("Demikian juga untuk data tahun 2018, ternyata ketiga data tersebut tidak didominasi oleh negara yang sama")
    st.subheader('Top 5 Jumlah Kunjungan')
    d1, d2 = st.columns(2)
    with d1:
        st.table(kunjungan2019.drop(['expend_2019', 'Rerata_2019'], axis=1))
    with d2:
        st.image('kunjungan2019.png')
    st.subheader('Top 5 Rerata Pengeluaran')
    
    e1, e2 = st.columns(2)
    with e1:
        st.table(expend2019.drop(['kunjungan_2019', 'Rerata_2019'], axis=1))
    with e2:
        st.image('expend2019.png')
    st.subheader('Top Data Rerata Lama Tinggal ')
    
    f1, f2 = st.columns(2)
    with f1:
        st.table(rerata2019.drop(['expend_2019', 'kunjungan_2019'], axis=1))
    with f2:
        st.image('rerata2019.png')

if tahun == "Simpulan":
    st.subheader("•	Berdasarkan hasil di atas, maka Cina, Malaysia, Australia, dan Singapura adalah negara-negara yang diprioritaskan menjadi target Wisatawan Mancanegara di Indonesia.")
    st.subheader("•	Diantara 4 Negara tersebut jika Pemerintah menilai dari Rerata Lama Tinggal dan Rerata Pengeluaran, Australia dan Cina selalu menjadi 2 teratas.")
    st.subheader("•	Namun jika Pemerintah menilai dari Jumlah kunjungan diantara 4 negara ini, maka Cina dan Malaysia selalu menjadi 2 terbaik.")

    



