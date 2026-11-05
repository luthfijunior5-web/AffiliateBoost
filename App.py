import streamlit as st
from PIL import Image
import base64, os

st.set_page_config(page_title="AffiliateBoost - Ljunior Home", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

# --- LOAD LOGO - NAMA FILE SUDAH SESUAI GITHUB ---
# File di GitHub: IMG-20261105-WA2497.jpg
LOGO_FILE = "IMG-20261105-WA2497.jpg"

def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

logo_b64 = get_base64(LOGO_FILE)
if logo_b64:
    logo_html = f'<img src="data:image/jpeg;base64,{logo_b64}" style="width:92px;height:92px;object-fit:cover;border-radius:50%;border:3px solid white;box-shadow:0 4px 12px rgba(0,0,0,.25);flex-shrink:0;">'
else:
    logo_html = '<div style="width:92px;height:92px;border-radius:50%;background:white;display:flex;align-items:center;justify-content:center;font-size:38px;">🚀</div>'

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&display=swap');
* { font-family: 'Plus Jakarta Sans', sans-serif; }
.stApp { background: #FFF7F0; }
.block-container { max-width: 1100px; padding-top: 0.8rem !important; padding-bottom: 2rem; }
header { visibility: hidden; }

/* JUMBOTRON */
.jumbotron {
  position: relative; overflow: hidden; border-radius: 22px;
  background: linear-gradient(135deg, #FF4D1C 0%, #FF6A00 55%, #FF8A00 100%);
  padding: 18px; color: white;
  box-shadow: 0 12px 30px rgba(255,77,28,.35);
  display: flex; align-items: center; gap: 16px;
}
.jumbotron-bg {
  position: absolute; right: 0; top: 0; bottom: 0; width: 45%;
  background-image: url('https://images.unsplash.com/photo-1530124566582-a618bc2615dc?q=80&w=1200&auto=format&fit=crop');
  background-size: cover; background-position: center;
  -webkit-mask-image: linear-gradient(to right, transparent, black 35%);
  mask-image: linear-gradient(to right, transparent, black 35%);
  opacity: .95;
}
.jumbo-text { position: relative; z-index: 2; }
.jumbo-title { font-size: 28px; font-weight: 800; line-height: 1.1; }
.jumbo-sub { font-size: 15px; font-weight: 700; opacity: .95; margin-top: 2px; }
.jumbo-badge { display:inline-block; margin-top:10px; background: rgba(255,255,255,.22); border:1px solid rgba(255,255,255,.4); padding:5px 11px; border-radius:999px; font-size:11px; font-weight:700; }

/* INPUT */
.input-card { background:white; border-radius:20px; padding:18px; box-shadow:0 6px 20px rgba(0,0,0,.06); border:1px solid #FFE8D9; margin-top:14px; }
.upload-box { border:2px dashed #22A06B; background:#EAF7F0; border-radius:14px; padding:16px; text-align:center; font-size:13px; }
.result-head { display:flex; justify-content:space-between; align-items:center; margin:22px 0 12px 0; }
.badge-siap { background:#00A86B; color:white; padding:6px 12px; border-radius:999px; font-size:12px; font-weight:700; }
.card-hook { background:#FF6A00; color:white; border-radius:16px; padding:16px; height:100%; }
.card-s15 { background:#00A86B; color:white; border-radius:16px; padding:16px; height:100%; }
.card-s30 { background:#FF6A00; color:white; border-radius:16px; padding:16px; height:100%; }
.card-seo { background:#00A86B; color:white; border-radius:16px; padding:16px; height:100%; }
.card-title { font-weight:800; font-size:16px; margin-bottom:8px; }
.card-text { font-size:13.5px; line-height:1.55; white-space:pre-wrap; }
.stButton > button { border-radius:12px !important; font-weight:700 !important; height:48px !important; }

/* FIX: Sembunyikan upload bawaan Streamlit yang dobel */
[data-testid="stFileUploader"] > div:first-child { display: none; }
[data-testid="stFileUploader"] section { padding: 0 !important; border: none !important; }
div[data-testid="stFileUploaderDropzone"] { display: none !important; }
.stButton > button[kind="primary"] { background: #00A86B !important; border: none !important; }

@media (max-width: 768px) {
  .jumbotron { flex-direction: row; padding:14px; gap:12px; }
  .jumbotron-bg { width:100%; opacity:.30; -webkit-mask-image:none; mask-image:none; }
  .jumbo-title { font-size:20px; }
  .jumbo-sub { font-size:12px; }
  .block-container { padding-left:12px !important; padding-right:12px !important; }
}
@media (max-width: 480px) {
  .jumbotron { flex-direction: column; text-align:center; }
  .jumbo-title { font-size:19px; }
}
</style>
""", unsafe_allow_html=True)

# --- JUMBOTRON + LOGO ---
st.markdown(f"""
<div class="jumbotron">
  <div class="jumbotron-bg"></div>
  {logo_html}
  <div class="jumbo-text">
    <div class="jumbo-title">AffiliateBoost<br>Generator Konten</div>
    <div class="jumbo-sub">Shopee Affiliate</div>
    <div class="jumbo-badge">✨ Ljunior Home • Bikin konten 1 menit jadi!</div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- INPUT ---
st.markdown('<div class="input-card">', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center; margin:0;">☁️ Upload Foto Produk</h3>', unsafe_allow_html=True)
uploaded = st.file_uploader("Upload Foto Produk", type=["jpg","jpeg","png"], accept_multiple_files=True, label_visibility="collapsed")
st.markdown('<div class="upload-box">⬆️ <b>Seret & lepas foto produk di sini</b><br>atau klik untuk pilih dari galeri • JPG/PNG • Bisa pilih banyak foto</div>', unsafe_allow_html=True)

if uploaded:
    cols = st.columns(min(len(uploaded), 4))
    for i, f in enumerate(uploaded):
        with cols[i % len(cols)]:
            st.image(Image.open(f), use_container_width=True)
    st.success(f"✅ {len(uploaded)} foto berhasil diupload")

nama = st.text_input("Nama Produk", placeholder="Contoh: Bor Listrik 550W Tangan")
spek = st.text_area("Spesifikasi Produk", placeholder="Contoh: 550W, 220V, Chuck 10mm, Kecepatan 0-2800 RPM", height=70)
st.markdown('</div>', unsafe_allow_html=True)

generate = st.button("✨ Generate Konten", use_container_width=True, type="primary")

def generate_konten(nama, spek):
    n = nama
    s = spek if spek else "kualitas premium, harga terjangkau"
    hook = f"3 KESALAHAN beli {n.lower()}\nyang bikin rugi!\nNo.3 jarang orang tahu 👀"
    s15 = f"Lagi cari {n.lower()} budget tapi kualitas premium? Ini dia {n} - {s}. Pas buat harian!\nKlik keranjang kuning sekarang!"
    s30 = f"Hai! Kalau kamu sering pakai {n.lower()}, wajib punya ini.\n{s}. Nyaman dipakai, kualitas juara, harga terjangkau.\nCek keranjang kuning di bawah, stok terbatas!"
    seo = f"• Review {n} | Murah & Bagus\n• {n} - {s[:60]}\n• {n} Terbaik Shopee | Cek Harga Promo"
    return hook, s15, s30, seo

if generate:
    if not nama:
        st.warning("Isi dulu Nama Produknya kak 🙏")
    else:
        hook, s15, s30, seo = generate_konten(nama, spek)
        st.markdown('<div class="result-head"><h3 style="margin:0;">✨ Hasil Konten AI</h3><span class="badge-siap">Siap digunakan ✓</span></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f'<div class="card-hook"><div class="card-title">🖼️ Hook Thumbnail</div><div class="card-text">{hook}</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="card-s15"><div class="card-title">🎧 Script 15 Detik</div><div class="card-text">{s15}</div></div>', unsafe_allow_html=True)
        c3, c4 = st.columns(2)
        with c3:
            st.markdown(f'<div class="card-s30"><div class="card-title">▶️ Script 30 Detik</div><div class="card-text">{s30}</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="card-seo"><div class="card-title">🔍 Judul SEO</div><div class="card-text">{seo}</div></div>', unsafe_allow_html=True)
        st.write("")
        b1, b2, b3 = st.columns(3)
        with b1:
            if st.button("📋 Salin Semua", use_container_width=True):
                st.code(f"{hook}\n\n{s15}\n\n{s30}\n\n{seo}", language="text")
        with b2:
            st.download_button("⬇️ Export", data=f"{hook}\n\n{s15}\n\n{s30}\n\n{seo}", file_name=f"konten-{nama}.txt", use_container_width=True, type="primary")
        with b3:
            if st.button("🔄 Regenerate", use_container_width=True):
                st.rerun()

st.caption("Ljunior Home • AffiliateBoost v2.2 • Serba Ada Buat Tukang & Rumah")
