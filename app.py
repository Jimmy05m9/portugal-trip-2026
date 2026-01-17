import streamlit as st

# 設定網頁：極致對比、大字體、手機優化
st.set_page_config(page_title="葡萄牙完整行程", page_icon="🇵🇹", layout="wide")

# CSS：確保在陽光下也清晰的黑白配色
st.markdown("""
    <style>
    html, body, [class*="css"] { 
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: "Microsoft JhengHei", "PingFang TC", sans-serif;
    }
    .stApp { background-color: #FFFFFF !important; }
    
    /* 側邊欄深色背景，確保導航清晰 */
    [data-testid="stSidebar"] { background-color: #1A1A1A !important; }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }

    /* 勾選框文字：加大、加粗、純黑 */
    .stCheckbox label p {
        color: #000000 !important;
        font-size: 20px !important;
        font-weight: 800 !important;
        margin-bottom: 5px;
    }
    
    /* 區塊樣式 */
    .time-badge { background-color: #000000; color: #FFFFFF; padding: 2px 10px; border-radius: 5px; font-weight: bold; }
    .location-box { border-left: 10px solid #000000; background-color: #F5F5F5; padding: 15px; margin: 15px 0; }
    </style>
    """, unsafe_allow_html=True)

# 側邊選單
with st.sidebar:
    st.title("🇵🇹 2026 葡萄牙行程")
    day = st.radio("切換日期：", [
        "✈️ 2/13-14 啟程波多", "🍷 2/15 波多一日遊", "🚗 2/16 租車/杜羅河谷", 
        "🎓 2/17 康布拉/阿格達", "🏰 2/18 辛特拉/還車", "🏛️ 2/19 里斯本(西)", 
        "🚋 2/20 里斯本(中)", "🛍️ 2/21 里斯本(北)", "⛪ 2/22 最終採買", "🏠 2/23-24 返家"
    ])

st.title(f"📍 {day}")

# 渲染 Checklist 的函式
def check(time, task, note=""):
    st.checkbox(f"【{time}】 {task}", key=f"{day}_{time}_{task}")
    if note:
        st.caption(f"└ 💡 {note}")

# --- 2/13-14 出發與抵達 ---
if day == "✈️ 2/13-14 啟程波多":
    st.markdown('<div class="location-box"><b>航班與入住</b></div>', unsafe_allow_html=True)
    check("2/13 22:10", "桃園機場集合 (TK25)", "行李直掛波多")
    check("2/14 05:50", "抵達伊斯坦堡轉機")
    check("2/14 11:30", "搭乘 TK1449 飛往波多 OPO")
    check("2/14 19:15", "抵達波多機場並取行李")
    check("2/14 20:30", "入住 VIVA Liberty 310", "休息備戰明天")

# --- 2/15 波多全日 ---
elif day == "🍷 2/15 波多一日遊":
    st.markdown('<div class="location-box"><b>步行探索波多</b></div>', unsafe_allow_html=True)
    check("09:00", "萊羅書店入場", "需預約，全球最美書店")
    check("10:30", "卡爾莫教堂", "欣賞外牆巨大藍瓷磚畫")
    check("11:30", "教士塔 & 自由廣場")
    check("13:00", "午餐：Tapabento", "熱門海鮮燉飯，建議預約")
    check("15:00", "聖本托車站", "2萬片藍瓷壁畫")
    check("16:30", "主教座堂 & 路易一世大橋", "步行至對岸加亞新城")
    check("18:00", "加亞新城看夕陽", "品嚐波特酒，看杜羅河夜景")

# --- 2/16 租車與河谷 ---
elif day == "🚗 2/16 租車/杜羅河谷":
    st.markdown('<div class="location-box"><b>自駕開啟</b></div>', unsafe_allow_html=True)
    check("10:00", "Europcar 波多市區取車", "Mercedes-Benz V-Class 9人座")
    check("11:30", "阿瑪蘭蒂 (Amarante) 慢遊", "聖公薩洛橋")
    check("14:30", "皮尼昂 (Pinhão) 車站", "瓷磚畫背景")
    check("16:00", "入住 Casa do Salgueiral Douro", "享受杜羅河谷景致")

# --- 2/17 康布拉與阿格達 ---
elif day == "🎓 2/17 康布拉/阿格達":
    st.markdown('<div class="location-box"><b>大學城與傘街</b></div>', unsafe_allow_html=True)
    check("10:00", "阿格達 (Águeda) 傘街", "彩色雨傘裝飾街道")
    check("13:00", "康布拉大學 (Coimbra)", "喬安娜圖書館(需預約)")
    check("16:00", "康布拉舊城區散步")
    check("18:00", "入住 Casas do Arco", "體驗大學城氛圍")

# --- 2/18 辛特拉 ---
elif day == "🏰 2/18 辛特拉/還車":
    st.markdown('<div class="location-box"><b>童話城堡與陸地之最</b></div>', unsafe_allow_html=True)
    check("10:00", "佩納宮 (Pena Palace)", "強烈建議搭接駁車或 Uber 上山")
    check("13:00", "雷加萊拉莊園", "探索奇幻地底塔")
    check("15:30", "羅卡角 (Cabo da Roca)", "歐亞大陸最西端證書")
    check("18:30", "入住 Hotel Arribas", "海邊飯店")
    check("20:00", "里斯本市中心還車 (Europcar)", "滿油還車，確認檢查")

# --- 2/19-21 里斯本 ---
elif day == "🏛️ 2/19 里斯本(西)":
    st.markdown('<div class="location-box"><b>貝倫區朝聖</b></div>', unsafe_allow_html=True)
    check("10:00", "熱羅尼莫斯修道院", "曼努埃爾建築代表")
    check("12:00", "貝倫正宗蛋塔店 (Pastéis de Belém)")
    check("14:00", "發現者紀念碑 & 貝倫塔")
    check("18:00", "入住 Corpo Santo Historical Hotel", "五星級服務")

elif day == "🚋 2/20 里斯本(中)":
    st.markdown('<div class="location-box"><b>經典電車之旅</b></div>', unsafe_allow_html=True)
    check("09:00", "28號黃色電車全線體驗", "建議起站 Martim Moniz 搭乘")
    check("11:00", "聖露西亞觀景台", "俯瞰 Alfama 舊城區")
    check("13:00", "Time Out Market 午餐")
    check("15:00", "聖胡斯塔升降機")

elif day == "🛍️ 2/21 里斯本(北)":
    check("10:00", "自由大道 (Av. da Liberdade) 採買", "精品與當地名產")
    check("14:00", "愛德華七世公園", "修剪整齊的迷宮花園")
    check("18:00", "晚餐：里斯本海鮮拼盤")

# --- 歸途 ---
elif day == "🏠 2/23-24 返家":
    st.markdown('<div class="location-box"><b>再見葡萄牙</b></div>', unsafe_allow_html=True)
    check("2/23 08:00", "里斯本機場報到", "辦理退稅手續")
    check("2/23 10:35", "搭乘 EK192 飛往杜拜")
    check("2/24 14:15", "抵達高雄小港機場 (KHH)", "溫暖的家")
