import streamlit as st

st.set_page_config(page_title="Ljunior Home", page_icon="🧰", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(180deg, #FF6B00 0%, #FF8C33 100%); }
.main-box { background:white; padding:28px; border-radius:22px; box-shadow:0 10px 30px rgba(0,0,0,0.18); }
h1 { color:white !important; text-align:center; text-shadow:0 2px 6px rgba(0,0,0,0.25); }
.stButton>button { background:#0E4DA4 !important; color:white !important; border-radius:14px !important; width:100%; font-weight:800; font-size:19px; padding:14px; border:none; }
.stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>div { border-radius:12px !important; border:2px solid #FF6B00 !important; }
</style>
""", unsafe_allow_html=True)

st.image("IMG-20261105-WA2497.jpg", width=200)
st.markdown("<h1>Generator Konten Shopee Affiliate</h1>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:white; font-weight:bold;">Ljunior Home<br>SERBA ADA BUAT TUKANG & RUMAH</p>', unsafe_allow_html=True)

st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.markdown("#### 🧰 Buat Konten Affiliate 1 Klik")

nama_produk = st.text_input("Nama Produk", placeholder="Contoh: ZENTOR Tool Box 12 inch")
spesifikasi = st.text_area("Spesifikasi", placeholder="Contoh: 12 inch 300x170x125mm bahan tebal anti karat", height=110)
target = st.selectbox("Target Pembeli", ["Tukang", "Rumah Tangga", "Pemula DIY", "Teknisi", "Ibu Rumah Tangga"])

if st.button("✨ Generate Konten"):
    if not nama_produk or not spesifikasi:
        st.error("Isi dulu Nama Produk & Spesifikasi ya kak!")
    else:
        st.success("Jadi! Tinggal copy paste")
        st.code(f"WAJIB PUNYA! {nama_produk} Buat {target} 🔥", language=None)
        st.code(f"Tukang wajib tau! {nama_produk} solusinya. Spesifikasi: {spesifikasi}. Cocok buat {target}. Cek keranjang orange! 🧰👇 #LjuniorHome", language=None)
        st.balloons()

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><center><small style='color:white;'>© Ljunior Home</small></center>", unsafe_allow_html=True)
