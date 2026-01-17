import streamlit as st

# 設定網頁標題與風格
st.set_page_config(page_title="2026 葡萄牙之旅", page_icon="🇵🇹", layout="wide")

# 自定義 Threads 風格 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Noto Sans TC', sans-serif; background-color: #f7f7f7; }
    .stApp { background-color: #f7f7f7; }
    
    .post-card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #efefef;
    }
    .time-tag { color: #bc6c25; font-weight: bold; font-size: 0.9rem; margin-bottom: 5px; }
    .activity-title { font-size: 1.2rem; font-weight: bold; color: #333; margin-bottom: 8px; }
    .note-box { background-color: #f8f9fa; padding: 12px; border-radius: 10px; font-size: 0.85rem; color: #666; border-left: 4px solid #dee2e6; }
    .tag { display: inline-block; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: bold; margin-right: 5px; }
    .tag-hotel { background-color: #e3f2fd; color: #0d47a1; }
    .tag-car { background-color: #fff3e0; color: #e65100; }
    .tag-food { background-color: #f1f8e9; color: #1b5e20; }
    </style>
    """, unsafe_allow_html=True)

# 側邊導航
with st.sidebar:
    st.title("🇵🇹 旅程目錄")
    day = st.radio("選擇日期", [
        "🌟 行程總覽", "2/13 出發", "2/14 波多抵達", "2/15 波多探索", 
        "2/16 杜羅河谷(租車)", "2/17 康布拉", "2/18 辛特拉(還車)", 
        "2/19 里斯本(北)", "2/20 里斯本(西)", "2/21 里斯本(市區)", 
        "2/22 最終採買", "2/23-24 歸途"
    ])
    st.divider()
    st.write("### 🏠 住宿速查")
    st.caption("2/14-15: Torel Avantgarde")
    st.caption("2/16: Quinta de la Rosa")
    st.caption("2/17: Sapientia Boutique")
    st.caption("2/18: Sintra Marmòris")
    st.caption("2/19-22: Corpo Santo")

# --- 邏輯呈現 ---

if day == "🌟 行程總覽":
    st.title("2026 葡萄牙家族冒險")
    st.markdown("### 全行程 Excel 數據同步版")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="post-card"><div class="activity-title">🚗 租車資訊</div>
        取車：2/16 10:00 (Porto)<br>還車：2/18 20:00 (Lisbon)<br>車型：Mercedes-Benz V-Class (9人座)</div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="post-card"><div class="activity-title">🛂 準備清單</div>
        護照正本、國際駕照、歐規轉接頭、網卡、好走的鞋。</div>""", unsafe_allow_html=True)

elif day == "2/14 波多抵達":
    st.header("2/14 (六) 波多抵達")
    st.markdown("""<div class="post-card"><div class="time-tag">19:15</div><div class="activity-title">抵達 OPO 機場</div>
    辦理入境後搭車前往飯店 check-in。</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="post-card"><div class="tag tag-hotel">HOTEL</div><div class="activity-title">Torel Avantgarde</div>
    地址：R. de Entre-Quintas 220, Porto</div>""", unsafe_allow_html=True)

elif day == "2/15 波多探索":
    st.header("2/15 (日) 波多舊城")
    activities = [
        ("09:00", "萊羅書店", "全球最美書店，需提前預約門票。"),
        ("11:00", "聖本托車站", "欣賞兩萬片藍瓷壁畫。"),
        ("13:00", "午餐：Tapabento", "推薦海鮮燉飯（需預約）。"),
        ("16:00", "路易一世大橋", "步行至上層看夕陽。")
    ]
    for time, title, note in activities:
        st.markdown(f"""<div class="post-card"><div class="time-tag">{time}</div><div class="activity-title">{title}</div>
        <div class="note-box">{note}</div></div>""", unsafe_allow_html=True)

elif day == "2/16 杜羅河谷(租車)":
    st.header("2/16 (一) 自駕起點")
    st.markdown("""<div class="post-card"><div class="tag tag-car">RENTAL</div><div class="time-tag">10:00</div>
    <div class="activity-title">Europcar 取車 (Porto City Center)</div>
    確認車輛狀況、保險、滿油取還。</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="post-card"><div class="time-tag">15:00</div><div class="activity-title">Pinhao 酒莊巡禮</div>
    入住 Quinta de la Rosa，享受河谷晚餐。</div>""", unsafe_allow_html=True)

elif day == "2/18 辛特拉(還車)":
    st.header("2/18 (三) 童話與最西端")
    items = [
        ("10:00", "佩納宮", "繽紛色彩的皇宮，人潮眾多建議早到。"),
        ("14:00", "雷加萊拉莊園", "探索奇幻地底深井。"),
        ("17:00", "羅卡角 Cabo da Roca", "歐亞大陸最西端紀念碑。"),
        ("20:00", "里斯本還車", "Europcar Lisbon Downtown 還車。")
    ]
    for t, a, n in items:
        st.markdown(f"""<div class="post-card"><div class="time-tag">{t}</div><div class="activity-title">{a}</div>
        <div class="note-box">{n}</div></div>""", unsafe_allow_html=True)

elif day == "2/19-21 里斯本(市區)":
    st.header("🌉 里斯本精華")
    st.markdown("""<div class="post-card"><div class="tag tag-food">MUST EAT</div><div class="activity-title">貝倫區正宗蛋塔</div>
    Pastéis de Belém，搭配肉桂粉更道地。</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="post-card"><div class="activity-title">28 號黃色電車</div>
    建議從起站搭乘，避開人潮，體驗坡道穿梭。</div>""", unsafe_allow_html=True)

# 歸途
elif day == "2/23-24 歸途":
    st.header("✈️ 結束旅程")
    st.markdown("""<div class="post-card"><div class="time-tag">2/23 08:00</div><div class="activity-title">前往 LIS 機場</div>
    搭乘 EK192 經杜拜轉機。</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="post-card"><div class="time-tag">2/24 14:15</div><div class="activity-title">抵達小港機場</div>
    回到溫暖的家。</div>""", unsafe_allow_html=True)
