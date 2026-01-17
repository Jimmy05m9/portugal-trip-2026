import streamlit as st

# 強制網頁高對比度設定
st.set_page_config(page_title="2026 葡萄牙行程表", page_icon="🇵🇹", layout="wide")

# 自定義 CSS：極簡黑白高對比
st.markdown("""
    <style>
    /* 全域背景設為純白，文字設為純黑 */
    html, body, [class*="css"] { 
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: "Microsoft JhengHei", "PingFang TC", sans-serif;
    }
    .stApp { background-color: #FFFFFF !important; }

    /* 側邊欄改為深灰色背景，白色文字，確保區隔清晰 */
    [data-testid="stSidebar"] {
        background-color: #212121 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* 勾選框文字：純黑、加粗、加大 */
    .stCheckbox label p {
        color: #000000 !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        line-height: 1.5;
    }

    /* 分隔線改為深灰色，增加區塊感 */
    hr {
        border: 1px solid #333333 !important;
        margin: 20px 0 !important;
    }

    /* 資訊區塊：淺灰色背景配深黑字 */
    .info-box {
        background-color: #F0F0F0;
        border-left: 8px solid #000000;
        padding: 15px;
        margin: 10px 0;
        color: #000000 !important;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 側邊欄
with st.sidebar:
    st.markdown("# 🇵🇹 導覽選單")
    day = st.radio("請點擊切換日期：", [
        "🏠 行程總覽", "✈️ 2/13-14 出發/波多", "🍷 2/15 波多探索", 
        "🍇 2/16 杜羅河谷", "🎓 2/17 康布拉", "🏰 2/18 辛特拉", 
        "🌉 2/19-21 里斯本", "🛍️ 2/22 最終採買", "✈️ 2/23-24 歸途"
    ])
    st.divider()
    st.write("### 🏠 住宿整理")
    st.markdown("- 2/14-16: VIVA Liberty\n- 2/16-17: Salgueiral\n- 2/17-18: Casas do Arco\n- 2/18-19: Hotel Arribas\n- 2/19-23: Corpo Santo")

# 頁面主標題
st.title(f"📍 {day}")

# --- 內容區 ---

if day == "🏠 行程總覽":
    st.markdown('<div class="info-box">此 App 專為本次葡萄牙自駕之旅設計，請勾選完成項目。</div>', unsafe_allow_html=True)
    st.checkbox("護照與國際駕照 (正本)")
    st.checkbox("歐規兩圓孔轉接頭")
    st.checkbox("景點預約門票 (QR Code)")

elif day == "✈️ 2/13-14 出發/波多":
    st.markdown('<div class="info-box">2/13 22:10 桃園機場集合</div>', unsafe_allow_html=True)
    st.checkbox("22:10 桃機 TPE 集合 (TK25)")
    st.checkbox("05:50 抵達伊斯坦堡轉機")
    st.checkbox("11:30 飛往波多 OPO (TK1449)")
    st.checkbox("19:15 抵達並入住 VIVA Liberty 310")

elif day == "🍷 2/15 波多探索":
    st.markdown('<div class="info-box">波多舊城一日遊</div>', unsafe_allow_html=True)
    st.checkbox("09:00 萊羅書店 (需預約)")
    st.checkbox("11:00 聖本托車站看壁畫")
    st.checkbox("13:00 午餐：Tapabento")
    st.checkbox("16:00 路易一世大橋夕陽")

elif day == "🍇 2/16 杜羅河谷":
    st.markdown('<div class="info-box">🚗 租車取車與自駕起點</div>', unsafe_allow_html=True)
    st.checkbox("10:00 波多市區 Europcar 取車")
    st.checkbox("14:00 杜羅河谷酒莊巡禮")
    st.checkbox("16:00 入住 Casa do Salgueiral")

elif day == "🏰 2/18 辛特拉":
    st.markdown('<div class="info-box">城堡與陸地最西端</div>', unsafe_allow_html=True)
    st.checkbox("10:00 佩納宮入場")
    st.checkbox("14:00 雷加萊拉莊園")
    st.checkbox("17:00 羅卡角 Cabo da Roca")
    st.checkbox("20:00 里斯本市區還車")

elif day == "🌉 2/19-21 里斯本":
    st.markdown('<div class="info-box">里斯本 28 號電車與蛋塔</div>', unsafe_allow_html=True)
    st.checkbox("貝倫區正宗蛋塔創始店")
    st.checkbox("搭乘 28 號黃色電車")
    st.checkbox("聖胡斯塔升降機")
    st.checkbox("入住 Corpo Santo Hotel")

elif day == "✈️ 2/23-24 歸途":
    st.markdown('<div class="info-box">回台灣囉！</div>', unsafe_allow_html=True)
    st.checkbox("2/23 08:00 前往機場 (EK192)")
    st.checkbox("2/24 14:15 抵達小港機場")
