import streamlit as st
from datetime import datetime
import pytz

# 極致清晰設定
st.set_page_config(page_title="葡萄牙行程與雙時區", page_icon="🇵🇹", layout="wide")

# 強制黑白高對比 CSS
st.markdown("""
    <style>
    html, body, [class*="css"] { background-color: #FFFFFF !important; }
    .stApp { background-color: #FFFFFF !important; }
    p, span, div, label, h1, h2, h3 {
        color: #000000 !important;
        font-family: "Microsoft JhengHei", "Heiti TC", sans-serif !important;
    }
    .stCheckbox label p {
        font-size: 24px !important;
        font-weight: 900 !important;
        color: #000000 !important;
    }
    [data-testid="stSidebar"] { background-color: #000000 !important; }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }
    
    /* 底部固定時鐘樣式 */
    .time-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #000000;
        color: #FFFFFF !important;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        font-weight: bold;
        z-index: 999;
        border-top: 3px solid #bc6c25;
    }
    .time-footer span { color: #FFFFFF !important; margin: 0 15px; }
    
    /* 增加底部間距避免內容被時鐘擋住 */
    .main-content { margin-bottom: 100px; }
    </style>
    """, unsafe_allow_html=True)

# 計算即時時間
def get_times():
    tw_tz = pytz.timezone('Asia/Taipei')
    pt_tz = pytz.timezone('Europe/Lisbon')
    now_tw = datetime.now(tw_tz)
    now_pt = datetime.now(pt_tz)
    return now_pt.strftime("%H:%M"), now_tw.strftime("%H:%M")

pt_time, tw_time = get_times()

# 頁面主體容器
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# 側邊欄導航
with st.sidebar:
    st.markdown("## 🇵🇹 導覽選單")
    day = st.radio("切換日期：", [
        "2/13-14 啟程波多", "2/15 波多一日遊", "2/16 租車/杜羅河谷", 
        "2/17 康布拉/傘街", "2/18 辛特拉/還車", "2/19-21 里斯本全覽", 
        "2/22 最終採買", "2/23-24 返家"
    ])

# 頁面標題
st.markdown(f'<h1 style="border-bottom: 5px solid #000;">📍 {day}</h1>', unsafe_allow_html=True)

# 清單功能
def item(task, detail=""):
    st.checkbox(task, key=f"{day}_{task}")
    if detail:
        st.markdown(f'<div style="background:#F0F0F0; padding:10px; margin-bottom:20px; font-size:18px;">└ ℹ️ {detail}</div>', unsafe_allow_html=True)

# 內容邏輯 (根據先前 Excel 整理)
if day == "2/13-14 啟程波多":
    item("22:10 桃園機場 TPE 集合", "阿聯酋航空行李直掛波多")
    item("19:15 抵達波多 OPO 機場", "辦理入境並入住 VIVA Liberty 310")

elif day == "2/15 波多一日遊":
    item("09:00 萊羅書店入場", "全球最美書店 (需預約)")
    item("聖本托車站 (藍瓷磚壁畫)")
    item("路易一世大橋看夕陽")

elif day == "2/16 租車/杜羅河谷":
    item("10:00 Europcar 取車", "賓士 V-Class 9人座")
    item("阿瑪蘭蒂 Amarante 慢遊")
    item("入住河谷飯店：Casa do Salgueiral")

elif day == "2/17 康布拉/傘街":
    item("阿格達 Águeda 傘街拍照")
    item("康布拉大學喬安娜圖書館")

elif day == "2/18 辛特拉/還車":
    item("10:00 佩納宮入場")
    item("羅卡角 (歐亞大陸最西端)")
    item("20:00 里斯本市區還車", "Europcar 還車，記得加滿油")

elif day == "2/19-21 里斯本全覽":
    item("貝倫區正宗蛋塔店朝聖")
    item("搭乘 28 號黃色電車")
    item("入住五星飯店：Corpo Santo")

elif day == "2/23-24 返家":
    item("08:00 前往里斯本機場", "辦理退稅")
    item("2/24 14:15 抵達小港機場")

st.markdown('</div>', unsafe_allow_html=True)

# --- 底部固定雙時區時鐘 ---
st.markdown(f"""
    <div class="time-footer">
        <span>🇵🇹 葡萄牙：{pt_time}</span>
        <span>🇹🇼 台灣：{tw_time}</span>
    </div>
    """, unsafe_allow_html=True)
