import streamlit as st
import random

# —— 必须最先调用 ——  
st.set_page_config(page_title="🎡 多选次数转盘抽奖", layout="centered")

# 页面标题
st.title("🎡 转盘抽奖小程序")
st.write("点击下面对应按钮，进行单次、十连或五十连抽。")

# 奖项与权重（万分之）
prizes = {
    "龙王": 1,
    "女神": 2,
    "邮轮": 30,
    "豹豹": 140,
    "王冠": 400,
    "熊熊": 1311,
    "雪花": 8116,
}
labels = list(prizes.keys())
weights = list(prizes.values())

# 三列并排按钮
col1, col2, col3 = st.columns(3)
draw_times = None
if col1.button("单抽"):
    draw_times = 1
if col2.button("10 连抽"):
    draw_times = 10
if col3.button("50 连抽"):
    draw_times = 50

# 如果有点击，执行抽奖
if draw_times:
    results = random.choices(labels, weights=weights, k=draw_times)
    counts = {label: results.count(label) for label in labels}

    st.subheader(f"🎉 本次 {draw_times} 次抽奖结果")
    for label, cnt in counts.items():
        if cnt > 0:
            st.write(f"- {label}：{cnt} 个")

# 侧边栏展示概率
st.sidebar.header("当前概率（万分之）")
for label, p in prizes.items():
    st.sidebar.write(f"- {label}：{p}")
