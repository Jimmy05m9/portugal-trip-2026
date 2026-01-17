import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="2026 葡萄牙之旅", page_icon="🇵🇹", layout="wide")

# 自定義 CSS 優化手機閱讀體驗
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .day-card { background-color: white; padding: 20px; border-radius: 15px; border-left: 6px solid #d4a373; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .hotel-info { background-color: #e9ecef; padding: 10px; border-radius: 10px; font-size: 0.9rem; margin-top: 10px; }
    .transport-info { background-color: #fff3cd; padding: 10px; border-radius: 10px; font-size: 0.9rem; margin-top: 10px; border: 1px solid #ffeeba; }
    .section-title { color: #bc6c25; font-weight: bold; font-size: 1.3rem; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 側邊導航
with st.sidebar:
    st.title("🧭 行程目錄")
    day = st.radio("選擇日期", ["行程總覽", "2/13 出發", "2/14-15 波多", "2/16 杜羅河谷", "2/17 康布拉", "2/18 辛特拉", "2/19-21 里斯本", "2/22 最後採買", "2/23-24 歸途"])
    st.divider()
    st.info("💡 貼心提醒：點擊下方按鈕可快速導航")
    st.link_button("✈️ 查看機票資訊", "https://www.emirates.com")

# --- 行程總覽 ---
if day == "行程總覽":
    st.title("🇵🇹 2026 葡萄牙家族之旅")
    st.image("https://images.unsplash.com/photo-1555881400-74d7acaacd8b?q=80&w=2000", caption="美麗的葡萄牙風景")
    
    st.markdown("### 📝 旅行快速導覽")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**🏠 住宿點：**")
        st.write("- Porto: Torel Avantgarde")
        st.write("- Coimbra: Sapientia Boutique Hotel")
        st.write("- Lisbon: Corpo Santo Historical Hotel")
    with col2:
        st.write("**🚗 交通工具：**")
        st.write("- 2/16-2/18 租車自駕")
        st.write("- 市區搭乘電車與步行")

# --- 每日細節 ---
elif day == "2/13 出發":
    st.header("✈️ 啟程 2/13 (五)")
    st.markdown('<div class="day-card"><b>22:10 桃園機場集合</b><br>搭乘阿聯酋航空 EK367 飛往杜拜。</div>', unsafe_allow_html=True)

elif day == "2/14-15 波多":
    st.header("🍷 波多 2/14 - 2/15")
    with st.expander("2/14 (六) 抵達與入住", expanded=True):
        st.markdown('<div class="day-card">19:15 抵達波多機場，搭車前往飯店。<br><div class="hotel-info">🏨 住宿：Torel Avantgarde</div></div>', unsafe_allow_html=True)
    with st.expander("2/15 (日) 波多經典行程"):
        st.write("✅ 萊羅書店 (Livraria Lello)")
        st.write("✅ 聖本托車站 (São Bento)")
        st.write("✅ 路易一世大橋夕陽")

elif day == "2/16 杜羅河谷":
    st.header("🍇 杜羅河谷 2/16 (一)")
    st.markdown('<div class="transport-info">🚗 租車取車：10:00 Porto 市中心</div>', unsafe_allow_html=True)
    st.markdown('<div class="day-card">前往 Douro Valley 酒莊巡禮，享受河谷風光。</div>', unsafe_allow_html=True)

elif day == "2/17 康布拉":
    st.header("🎓 康布拉 2/17 (二)")
    st.markdown('<div class="day-card">參觀全球最美圖書館：喬安娜圖書館。<br><div class="hotel-info">🏨 住宿：Sapientia Boutique Hotel</div></div>', unsafe_allow_html=True)

elif day == "2/18 辛特拉":
    st.header("🏰 辛特拉 2/18 (三)")
    st.markdown('<div class="day-card">佩納宮 (Pena Palace)、雷加萊拉莊園、羅卡角 (歐亞大陸最西端)。</div>', unsafe_allow_html=True)
    st.markdown('<div class="transport-info">🚗 租車還車：20:00 里斯本市區</div>', unsafe_allow_html=True)

elif day == "2/19-21 里斯本":
    st.header("🌉 里斯本 2/19 - 2/21")
    st.markdown('<div class="hotel-info">🏨 住宿：Corpo Santo Historical Hotel (連住三晚)</div>', unsafe_allow_html=True)
    st.write("### 📅 里斯本重點")
    st.write("- **2/20 (五)：** 貝倫區、聖胡斯塔升降機、Fado 表演。")
    st.write("- **2/21 (六)：** 28號電車體驗、Alfama 舊城區、聖喬治城堡。")
    st.link_button("📍 打開貝倫蛋塔店地圖", "https://maps.app.goo.gl/k9u7uR6A5N1u1K1Q8")

elif day == "2/22 最後採買":
    st.header("🛍️ 里斯本最後衝刺 2/22 (日)")
    st.markdown('<div class="day-card">自由大道 (Av. da Liberdade) 採買名品與紀念品，享受最後的葡萄牙時光。</div>', unsafe_allow_html=True)

elif day == "2/23-24 歸途":
    st.header("✈️ 返家 2/23 - 2/24")
    st.markdown('<div class="day-card"><b>2/23 08:00 前往機場</b><br>搭乘 EK192 經杜拜轉機。<br><b>2/24 14:15 抵達高雄小港機場</b></div>', unsafe_allow_html=True)
