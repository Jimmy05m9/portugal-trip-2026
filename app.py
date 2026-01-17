import streamlit as st

# 網頁基本設定 (效仿精緻排版)
st.set_page_config(page_title="2026 葡萄牙冬日之旅", page_icon="🇵🇹", layout="wide")

# 自定義 CSS 讓介面更像手機 App
st.markdown("""
    <style>
    .stApp { background-color: #fdfaf5; }
    .main-card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; border-left: 5px solid #d4a373; }
    .date-header { color: #bc6c25; font-weight: bold; font-size: 1.2rem; }
    .location-tag { background-color: #e9edc9; padding: 2px 10px; border-radius: 20px; font-size: 0.8rem; }
    </style>
    """, unsafe_allow_html=True)

# 側邊欄：快速導航與實用連結
with st.sidebar:
    st.title("🧭 旅程地圖")
    selection = st.radio("前往日期", ["總覽", "2/13 出發", "2/14-16 波多", "2/17 康布拉", "2/18-19 辛特拉", "2/20-22 里斯本", "2/23 歸途"])
    st.divider()
    st.write("### ✈️ 機票/交通資訊")
    st.link_button("查看機票與電子票證", "https://www.emirates.com")
    st.write("### 🌦️ 即時天氣")
    st.write("波多：12°C ☁️ | 里斯本：15°C ☀️")

# 主頁面內容
if selection == "總覽":
    st.title("🇵🇹 2026 葡萄牙冬日冒險")
    st.image("https://images.unsplash.com/photo-1555881400-74d7acaacd8b?q=80&w=2070", caption="波多 (Porto) 的杜羅河畔")
    
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("💡 旅程重點")
    col1, col2 = st.columns(2)
    with col1:
        st.write("🏠 **住哪裡：** 波多、康布拉、辛特拉、里斯本")
        st.write("🍴 **吃什麼：** 葡式蛋塔、海鮮飯、波特酒")
    with col2:
        st.write("🎒 **帶什麼：** 護照、歐規兩圓孔頭、舒適好走的鞋")
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "2/14-16 波多":
    st.header("📍 波多 (Porto)")
    
    st.markdown('<div class="main-card"><span class="date-header">2/14 (六) 入住與漫步</span><br>預計 19:15 抵達，辦理入境後入住飯店。<br><a href="https://www.google.com/maps/search/Porto+Hotel">📍 打開飯店地圖</a></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="main-card"><span class="date-header">2/15 (日) 古城探索</span><br>必去：萊羅書店、路易一世大橋。<br><b>💡 巧兒推薦：</b>在河岸邊喝一杯波特酒看夕陽！</div>', unsafe_allow_html=True)

elif selection == "2/20-22 里斯本":
    st.header("📍 里斯本 (Lisbon)")
    st.markdown('<div class="main-card"><span class="date-header">2/21 (六) 貝倫區朝聖</span><br><b>🍴 必吃：Pastéis de Belém</b><br>這就是巧兒推薦的那家正宗蛋塔創始店！</div>', unsafe_allow_html=True)
    st.link_button("Google Maps 導航至蛋塔店", "https://maps.app.goo.gl/9S6M6S6f888888")

# 其他日期內容以此類推...
