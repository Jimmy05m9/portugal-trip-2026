import streamlit as st

# 網頁設定：優化對比度與字體
st.set_page_config(page_title="2026 葡萄牙之旅 Checklist", page_icon="🇵🇹", layout="wide")

# 自定義 CSS：強化文字顏色對比
st.markdown("""
    <style>
    /* 全域文字顏色改為深黑，背景改為白色 */
    html, body, [class*="css"] { 
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #1A1A1A !important;
    }
    .stApp { background-color: #FFFFFF; }
    
    /* 側邊欄深色背景，白字 */
    [data-testid="stSidebar"] {
        background-color: #2D3436 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* 行程卡片樣式：增加深色邊框加強視覺邊界 */
    .itinerary-card {
        border: 2px solid #EEEEEE;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        background-color: #FAFAFA;
    }
    
    /* 標籤樣式：顏色加深確保可讀性 */
    .badge {
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: bold;
        margin-right: 5px;
        color: white !important;
    }
    .bg-blue { background-color: #0984E3; } /* 交通 */
    .bg-green { background-color: #00B894; } /* 景點 */
    .bg-orange { background-color: #E17055; } /* 飯店 */
    
    /* 勾選框文字加大加深 */
    .stCheckbox label {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 側邊導航
with st.sidebar:
    st.title("🇵🇹 葡萄牙清單")
    day = st.radio("選擇日期：", [
        "🏠 行程總覽", "✈️ 2/13-14 出發/波多", "🍷 2/15 波多探索", 
        "🍇 2/16 杜羅河谷", "🎓 2/17 康布拉", "🏰 2/18 辛特拉", 
        "🌉 2/19-21 里斯本", "🛍️ 2/22 最終採買", "✈️ 2/23-24 歸途"
    ])
    st.divider()
    st.write("### 📌 住宿清單")
    st.write("2/14-16: VIVA Liberty 310")
    st.write("2/16-17: Casa do Salgueiral")
    st.write("2/17-18: Casas do Arco")
    st.write("2/18-19: Hotel Arribas")
    st.write("2/19-23: Corpo Santo")

# 定義顯示勾選清單的函式
def task_item(time, label, text, category="景點"):
    badge_class = "bg-green"
    if "交通" in category or "機" in category: badge_class = "bg-blue"
    elif "飯店" in category or "住" in category: badge_class = "bg-orange"
    
    col_time, col_check = st.columns([1, 5])
    with col_time:
        st.markdown(f"**{time}**")
    with col_check:
        # 使用唯一 key 避免衝突
        st.checkbox(f"{text}", key=f"{day}_{time}_{text}")
        st.markdown(f'<span class="badge {badge_class}">{category}</span>', unsafe_allow_html=True)
    st.divider()

# --- 內容呈現 ---

if day == "🏠 行程總覽":
    st.header("🌟 旅程重點檢查 (Checklist)")
    st.checkbox("帶齊所有護照、國際駕照")
    st.checkbox("歐規兩圓孔轉接頭、快充頭")
    st.checkbox("波多 & 里斯本景點預約門票 (萊羅書店/佩納宮)")
    st.checkbox("歐元現金與海外刷卡信用卡")
    st.image("https://images.unsplash.com/photo-1555881400-74d7acaacd8b?q=80&w=2000")

elif day == "✈️ 2/13-14 出發/波多":
    st.header("2/13 - 2/14 啟程")
    task_item("22:10", "交通", "桃園機場 TPE 集合 (TK25)", "交通")
    task_item("05:50", "交通", "抵達伊斯坦堡轉機", "交通")
    task_item("11:30", "交通", "搭乘 TK1449 飛往波多 OPO", "交通")
    task_item("19:15", "飯店", "入住 VIVA Liberty 310 (波多)", "飯店")

elif day == "🍷 2/15 波多探索":
    st.header("2/15 (日) 波多舊城")
    task_item("09:00", "景點", "萊羅書店 (Livraria Lello) 入場", "景點")
    task_item("11:00", "景點", "聖本托車站 (São Bento) 看壁畫", "景點")
    task_item("13:00", "美食", "午餐：Tapabento (建議預約)", "景點")
    task_item("16:00", "景點", "路易一世大橋看夕陽", "景點")

elif day == "🍇 2/16 杜羅河谷":
    st.header("2/16 (一) 租車自駕")
    task_item("10:00", "交通", "波多市區 Europcar 取車", "交通")
    task_item("14:00", "景點", "前往杜羅河谷酒莊巡禮", "景點")
    task_item("16:00", "飯店", "入住 Casa do Salgueiral Douro", "飯店")

elif day == "🏰 2/18 辛特拉":
    st.header("2/18 (三) 童話辛特拉")
    task_item("10:00", "景點", "佩納宮 (Pena Palace)", "景點")
    task_item("14:00", "景點", "雷加萊拉莊園", "景點")
    task_item("17:00", "景點", "羅卡角 (Cabo da Roca) 歐亞最西端", "景點")
    task_item("20:00", "交通", "里斯本市區還車 (Europcar)", "交通")

elif day == "🌉 2/19-21 里斯本":
    st.header("里斯本精彩行程")
    task_item("ALL", "景點", "搭乘 28 號黃色電車", "景點")
    task_item("ALL", "景點", "貝倫區正宗蛋塔店朝聖", "景點")
    task_item("ALL", "景點", "聖胡斯塔升降機俯瞰市區", "景點")
    st.info("💡 里斯本住宿：Corpo Santo Historical Hotel (連住四晚)")

elif day == "✈️ 2/23-24 歸途":
    st.header("2/23 - 2/24 返家")
    task_item("08:00", "交通", "前往 LIS 機場 (EK192)", "交通")
    task_item("14:15", "交通", "2/24 抵達高雄小港機場", "交通")
