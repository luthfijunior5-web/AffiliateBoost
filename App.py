import streamlit as st
import random

st.set_page_config(page_title="AffiliateBoost", page_icon="🚀", layout="centered")

st.markdown("# 🚀 AffiliateBoost")
st.markdown("### Generator Konten Shopee Affiliate")
st.markdown("---")

nama_produk = st.text_input("Nama Produk", placeholder="ZENTOR Tool Box ZT24310")
spek = st.text_area("Spesifikasi", placeholder="12 inch 300x170x125mm, bahan tebal")
target = st.selectbox("Target", ["Tukang", "Ibu RT", "Umum"])

if st.button("✨ Generate Konten"):
    if not nama_produk:
        st.warning("Isi nama produk dulu")
        st.stop()
    
    hooks = [f"TOOL BOX BERANTAKAN? {nama_produk.upper()} SOLUSINYA!", f"PUSING CARI OBENG? {nama_produk} BIKIN RAPI!", f"JANGAN BELI TOOL BOX SEBELUM LIHAT INI!"]
    
    st.success("Berhasil kak!")
    st.subheader("🎯 Hook Thumbnail")
    for h in hooks:
        st.code(h)
    
    st.subheader("🎙️ Script 15 Detik")
    st.code(f"Pusing cari obeng 10 menit? Ini {nama_produk}, {spek}. Bikin kerja cepat, rumah rapi. Cek keranjang oren!")
    
    st.subheader("⏱️ Script 30 Detik")
    st.code(f"Pusing cari obeng hilang terus? Ini {nama_produk}. Ukuran {spek}. Bahan tebal kunci kuat. Kerja cepat rumah rapi. Cek keranjang oren sebelum habis!")
    
    st.subheader("🔍 Judul SEO")
    st.code(f"{nama_produk} Tool Box 12 Inch Tebal Kunci Kuat Original")
