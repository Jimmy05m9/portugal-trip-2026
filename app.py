import streamlit as st

# 極致清晰設定
st.set_page_config(page_title="葡萄牙行程表", page_icon="🇵🇹", layout="wide")

# 強制黑白高對比 CSS (解決看不見字的問題)
st.markdown("""
    <style>
    /* 1. 全域背景強制純白 */
    html, body, [class*="css"] { 
        background-color: #FFFFFF !important; 
    }
    .stApp { 
        background-color: #FFFFFF !important; 
    }

    /* 2. 所有文字強制純黑，且字體加大 */
    p, span, div, label, h1, h2, h3 {
        color: #000000 !important;
        font-family: "Microsoft JhengHei", "Heiti TC", sans-serif !important;
    }

    /* 3. 勾選框文字：加大至 24px、加粗、純黑 */
    .stCheckbox label p {
        font-size: 24px !important;
        font-weight: 900 !important;
        color: #000000 !important;
        line-height: 1.6 !important;
        padding-top: 5px;
    }

    /* 4. 側邊欄：雖然是深色，但確保文字是純白對比 */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
        font-size: 18px !important;
    }

    /* 5. 區塊線條：用粗黑線分隔，增加視覺辨識度 */
    .day-header {
        border-bottom: 5px solid #000000;
        margin-bottom: 20px;
        padding-bottom: 10px;
    }
    
    .note-text {
        font-size: 18px !important;
        color: #333333 !important;
        background-color: #F0F0F0;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 側邊欄導航
with st.sidebar:
    st.markdown("## 🇵🇹 葡萄牙清單")
    day = st.radio("切換日期：", [
        "2/13-14 啟程波多", "2/15 波多一日遊", "2/16 租車/杜羅河谷", 
        "2/17 康布拉/傘街", "2/18 辛特拉/還車", "2/19-21 里斯本全覽", 
        "2/22 最終採買", "2/23-24 返家"
    ])
    st.divider()
    st.write("住宿摘要：")
    st.write("• 波多: VIVA Liberty\n• 河谷: Salgueiral\n• 康布拉: Casas do Arco\n• 里斯本: Corpo Santo")

# 頁面大標題
st.markdown(f'<h1 class="day-header">📍 {day}</h1>', unsafe_allow_html=True)

# 建立 Checklist 的功能
def item(task, detail=""):
    st.checkbox(task, key=f"{day}_{task}")
    if detail:
        st.markdown(f'<div class="note-text">└ ℹ️ {detail}</div>', unsafe_allow_html=True)

# --- 根據 Excel 的完整內容 ---

if day == "2/13-14 啟程波多":
    item("2/13 22:10 桃園機場 TPE 集合", "阿聯酋航空行李直掛波多")
    item("2/14 05:50 抵達伊斯坦堡轉機")
    item("2/14 19:15 抵達波多 OPO 機場", "辦理入境、領取行李")
    item("入住波多飯店：VIVA Liberty 310", "地址：Rua da Alegria 310, Porto")

elif day == "2/15 波多一日遊":
    item("09:00 萊羅書店入場", "需預約，全球最美書店")
    item("卡爾莫教堂 (藍瓷磚牆)")
    item("教士塔 & 自由廣場")
    item("午餐：Tapabento", "熱門餐廳，建議預約海鮮燉飯")
    item("聖本托車站 (2萬片壁畫)")
    item("路易一世大橋看夕陽", "步行至加亞新城河岸")

elif day == "2/16 租車/杜羅河谷":
    item("10:00 Europcar 取車", "賓士 V-Class 9人座 (波多市區取)")
    item("阿瑪蘭蒂 (Amarante) 慢遊", "參觀聖公薩洛橋與教堂")
    item("皮尼昂 (Pinhão) 車站", "欣賞車站瓷磚畫")
    item("入住河谷飯店：Casa do Salgueiral", "享受杜羅河谷景致")

elif day == "2/17 康布拉/傘街":
    item("阿格達 (Águeda) 傘街", "彩色雨傘街道拍照")
    item("康布拉大學 (Coimbra)", "參觀喬安娜圖書館")
    item("入住康布拉飯店：Casas do Arco")

elif day == "2/18 辛特拉/還車":
    item("10:00 佩納宮 (Pena Palace)", "強烈建議提早抵達避開人潮")
    item("雷加萊拉莊園 (地底塔)")
    item("羅卡角 (Cabo da Roca)", "歐亞大陸最西端紀念碑")
    item("20:00 里斯本市區還車", "Europcar 還車，記得加滿油")
    item("入住海邊飯店：Hotel Arribas")

elif day == "2/19-21 里斯本全覽":
    item("貝倫區：熱羅尼莫斯修道院")
    item("貝倫區：正宗蛋塔始祖店", "Pastéis de Belém")
    item("搭乘 28 號黃色電車", "建議起站 Martim Moniz 搭乘")
    item("聖胡斯塔升降機")
    item("入住五星飯店：Corpo Santo", "市中心位置，服務極佳")

elif day == "2/23-24 返家":
    item("08:00 前往里斯本機場", "提早辦理退稅手續")
    item("10:35 搭乘 EK192 飛往杜拜")
    item("2/24 14:15 抵達小港機場", "回到溫暖的家")
