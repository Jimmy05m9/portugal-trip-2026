import streamlit as st

st.set_page_config(page_title="葡萄牙之旅 2026", layout="wide")
st.title("🇵🇹 2026 葡萄牙冬日之旅")
st.subheader("給旅伴的快速手冊 (2/13 - 2/24)")

# 行程快速表
st.info("📅 2/13 22:10 桃園機場集合")

col1, col2 = st.columns(2)
with col1:
    st.write("### 📍 主要停留點")
    st.write("- **Porto 波多** (2/14-2/16)")
    st.write("- **Coimbra 康布拉** (2/17)")
    st.write("- **Sintra 辛特拉** (2/18-2/19)")
    st.write("- **Lisbon 里斯本** (2/20-2/22)")

with col2:
    st.write("### 🧳 必帶清單")
    st.checkbox("護照正本")
    st.checkbox("歐規轉接頭 (兩圓孔)")
    st.checkbox("好走的運動鞋")

st.success("🍴 必吃：貝倫區正宗蛋塔、波特酒")