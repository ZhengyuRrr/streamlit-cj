import streamlit as st
import random

# —— 这一行必须第一个调用 ——  
st.set_page_config(page_title="🎡 十连抽转盘", layout="centered")

# 页面标题和说明
st.title("🎡 十连抽转盘抽奖小程序")
st.write("每次点击下面按钮，系统将按你设定的万分比进行 10 次抽奖。")

# 奖项与万分比（万分之）
prizes = {
    "龙王": 3,
    "女神": 6,
    "邮轮": 90,
    "豹豹": 140,
    "王冠": 400,
    "熊熊": 1311,
    "雪花": 8049,
}
labels = list(prizes.keys())
weights = list(prizes.values())

# 十连抽按钮
if st.button("开始十连抽"):
    results = random.choices(labels, weights=weights, k=10)
    counts = {label: results.count(label) for label in labels}

    st.subheader("🎉 本次十连抽结果")
    for label, cnt in counts.items():
        if cnt > 0:
            st.write(f"- {label}：{cnt} 个")
    # 显示未中的奖项（可选）
    zeros = [l for l, c in counts.items() if c == 0]
    if zeros:
        st.write(f"- 未中的奖项：{', '.join(zeros)}")

# 侧边栏展示当前概率
st.sidebar.header("当前概率（万分之）")
for label, p in prizes.items():
    st.sidebar.write(f"- {label}：{p}")
