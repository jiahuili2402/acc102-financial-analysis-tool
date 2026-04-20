# ACC102 Track 4: Interactive Financial Analysis Tool
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 页面配置
st.set_page_config(page_title="Financial Analysis Tool", layout="wide")
st.title("ACC102 Track 4: Interactive Financial Analysis Tool")
st.subheader("A Simple Corporate Finance Analysis Tool")

# 示例数据（可替换为你的真实数据）
df = pd.DataFrame({
    "Company": ["Midea", "Gree", "Haier"],
    "Revenue (Billion)": [200.5, 188.2, 152.7],
    "Net Profit (Billion)": [20.1, 18.3, 15.2],
    "ROE (%)": [23.4, 22.5, 17.7]
})

# 数据预览
st.subheader("Data Preview")
st.dataframe(df)

# 交互式分析
st.subheader("Interactive Analysis")
selected_company = st.selectbox("Choose a company to analyze", df["Company"])
selected_data = df[df["Company"] == selected_company].iloc[0]

st.write(f"**Selected Company:** {selected_company}")
st.write(f"Revenue: {selected_data['Revenue (Billion)']} billion")
st.write(f"Net Profit: {selected_data['Net Profit (Billion)']} billion")
st.write(f"ROE: {selected_data['ROE (%)']}%")

# 可视化图表
st.subheader("Revenue Comparison")
fig, ax = plt.subplots()
ax.bar(df["Company"], df["Revenue (Billion)"], color=["#1f77b4", "#ff7f0e", "#2ca02c"])
ax.set_ylabel("Revenue (Billion)")
st.pyplot(fig)

st.success("✅ Tool runs successfully!")
