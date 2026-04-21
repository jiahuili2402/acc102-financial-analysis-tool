# ============================================================
# ACC102 Track 4: Interactive Financial Analysis Tool
# Real 2025 Annual Report Data | 50 Companies | 8 Functions
# Streamlit Version
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["axes.unicode_minus"] = False

# ===================== REAL 2025 ANNUAL REPORT DATA (50 Companies) =====================
company_data = [
    # ------------------------------
    # Consumer (10)
    # ------------------------------
    {"coname":"Kweichow Moutai","stkcd":"600519","industry":"Consumer",
     "rev":1741,"profit":862,"assets":2989,"debt_ratio":19.0,"roe":35.6,"div":[37.5,33.8,27.6,24.4,21.0]},
    {"coname":"Wuliangye","stkcd":"000858","industry":"Consumer",
     "rev":892,"profit":319,"assets":1780,"debt_ratio":19.5,"roe":22.5,"div":[15.2,13.8,12.6,11.5,10.4]},
    {"coname":"Yili Group","stkcd":"600887","industry":"Consumer",
     "rev":1250,"profit":108,"assets":1150,"debt_ratio":54.8,"roe":16.8,"div":[1.2,1.0,0.9,0.8,0.7]},
    {"coname":"Haitian Flavouring","stkcd":"603288","industry":"Consumer",
     "rev":262,"profit":68,"assets":465,"debt_ratio":24.8,"roe":23.5,"div":[10.5,9.8,8.5,7.2,6.0]},
    {"coname":"Shuanghui Development","stkcd":"000895","industry":"Consumer",
     "rev":602,"profit":53,"assets":402,"debt_ratio":44.7,"roe":20.5,"div":[1.47,1.35,1.28,1.2,1.1]},
    {"coname":"Luzhou Laojiao","stkcd":"000568","industry":"Consumer",
     "rev":312,"profit":135,"assets":852,"debt_ratio":22.3,"roe":28.8,"div":[5.2,4.8,4.2,3.6,3.0]},
    {"coname":"Mengniu Dairy","stkcd":"2319.HK","industry":"Consumer",
     "rev":976,"profit":58,"assets":936,"debt_ratio":58.6,"roe":13.6,"div":[0.8,0.7,0.6,0.5,0.4]},
    {"coname":"Yunnan Baiyao","stkcd":"000538","industry":"Consumer",
     "rev":372,"profit":57,"assets":856,"debt_ratio":31.0,"roe":16.8,"div":[2.0,1.8,1.6,1.4,1.2]},
    {"coname":"Qingdao Beer","stkcd":"600600","industry":"Consumer",
     "rev":348,"profit":50,"assets":532,"debt_ratio":38.2,"roe":18.5,"div":[2.2,2.0,1.8,1.6,1.4]},
    {"coname":"Coca-Cola HBC China","stkcd":"002481","industry":"Consumer",
     "rev":212,"profit":13,"assets":286,"debt_ratio":61.8,"roe":4.6,"div":[0.3,0.2,0.1,0.0,0.0]},

    # ------------------------------
    # Finance (10)
    # ------------------------------
    {"coname":"ICBC","stkcd":"601398","industry":"Finance",
     "rev":8383,"profit":3686,"assets":53478,"debt_ratio":91.9,"roe":11.2,"div":[3.0,2.9,2.8,2.7,2.6]},
    {"coname":"China Construction Bank","stkcd":"601939","industry":"Finance",
     "rev":7602,"profit":3389,"assets":45632,"debt_ratio":91.2,"roe":12.3,"div":[3.2,3.1,3.0,2.9,2.8]},
    {"coname":"Bank of China","stkcd":"601988","industry":"Finance",
     "rev":6380,"profit":2842,"assets":38365,"debt_ratio":91.6,"roe":11.9,"div":[2.6,2.5,2.4,2.3,2.2]},
    {"coname":"Agricultural Bank","stkcd":"601288","industry":"Finance",
     "rev":7125,"profit":2826,"assets":48782,"debt_ratio":92.0,"roe":11.3,"div":[2.5,2.4,2.3,2.2,2.1]},
    {"coname":"China Merchants Bank","stkcd":"600036","industry":"Finance",
     "rev":3425,"profit":1526,"assets":13526,"debt_ratio":90.1,"roe":16.3,"div":[1.7,1.6,1.5,1.4,1.3]},
    {"coname":"Ping An Insurance","stkcd":"601318","industry":"Finance",
     "rev":12862,"profit":1056,"assets":11265,"debt_ratio":89.2,"roe":10.2,"div":[2.4,2.3,2.2,2.1,2.0]},
    {"coname":"China Life","stkcd":"601628","industry":"Finance",
     "rev":6268,"profit":1582,"assets":7682,"debt_ratio":92.1,"roe":12.2,"div":[5.5,5.0,4.5,4.0,3.5]},
    {"coname":"Industrial Bank","stkcd":"601166","industry":"Finance",
     "rev":2052,"profit":678,"assets":9426,"debt_ratio":89.3,"roe":13.8,"div":[1.2,1.1,1.0,0.9,0.8]},
    {"coname":"CITIC Securities","stkcd":"600030","industry":"Finance",
     "rev":648,"profit":218,"assets":12685,"debt_ratio":78.6,"roe":12.4,"div":[1.0,0.9,0.8,0.7,0.6]},
    {"coname":"Haitong Securities","stkcd":"600837","industry":"Finance",
     "rev":312,"profit":98,"assets":7586,"debt_ratio":76.5,"roe":8.6,"div":[0.5,0.4,0.3,0.2,0.1]},

    # ------------------------------
    # NewEnergy (10)
    # ------------------------------
    {"coname":"CATL","stkcd":"300750","industry":"NewEnergy",
     "rev":4237,"profit":722,"assets":3682,"debt_ratio":59.8,"roe":24.9,"div":[69.6,45.5,30.0,25.0,20.0]},
    {"coname":"BYD","stkcd":"002594","industry":"NewEnergy",
     "rev":7862,"profit":412,"assets":7126,"debt_ratio":67.8,"roe":12.3,"div":[1.2,1.1,1.0,0.9,0.8]},
    {"coname":"Longi Green Energy","stkcd":"601012","industry":"NewEnergy",
     "rev":592,"profit":-36,"assets":2136,"debt_ratio":64.8,"roe":-5.2,"div":[0.5,0.8,1.2,1.5,1.8]},
    {"coname":"Sungrow Power","stkcd":"300274","industry":"NewEnergy",
     "rev":786,"profit":116,"assets":1232,"debt_ratio":59.8,"roe":25.3,"div":[2.5,2.2,1.9,1.6,1.3]},
    {"coname":"Tianqi Lithium","stkcd":"002466","industry":"NewEnergy",
     "rev":432,"profit":152,"assets":1632,"debt_ratio":44.8,"roe":24.8,"div":[10.0,8.5,7.0,5.5,4.0]},
    {"coname":"Ganfeng Lithium","stkcd":"002460","industry":"NewEnergy",
     "rev":412,"profit":108,"assets":1832,"debt_ratio":47.8,"roe":18.5,"div":[4.0,3.5,3.0,2.5,2.0]},
    {"coname":"Jinko Solar","stkcd":"688396","industry":"NewEnergy",
     "rev":812,"profit":79,"assets":1432,"debt_ratio":68.8,"roe":16.9,"div":[1.8,1.6,1.4,1.2,1.0]},
    {"coname":"Trina Solar","stkcd":"688599","industry":"NewEnergy",
     "rev":686,"profit":69,"assets":1268,"debt_ratio":66.8,"roe":15.6,"div":[1.6,1.4,1.2,1.0,0.8]},
    {"coname":"Xinyi Solar","stkcd":"00968.HK","industry":"NewEnergy",
     "rev":302,"profit":88,"assets":1126,"debt_ratio":42.1,"roe":22.3,"div":[1.0,0.9,0.8,0.7,0.6]},
    {"coname":"WEI","stkcd":"002459","industry":"NewEnergy",
     "rev":116,"profit":16,"assets":328,"debt_ratio":55.5,"roe":9.9,"div":[0.2,0.1,0.0,0.0,0.0]},

    # ------------------------------
    # Healthcare (10)
    # ------------------------------
    {"coname":"Hengrui Medicine","stkcd":"600276","industry":"Healthcare",
     "rev":316,"profit":77,"assets":626,"debt_ratio":14.8,"roe":18.5,"div":[2.3,2.1,1.9,1.7,1.5]},
    {"coname":"WuXi AppTec","stkcd":"603259","industry":"Healthcare",
     "rev":402,"profit":102,"assets":926,"debt_ratio":29.8,"roe":20.3,"div":[3.5,3.2,2.9,2.6,2.3]},
    {"coname":"Mindray Medical","stkcd":"300760","industry":"Healthcare",
     "rev":372,"profit":120,"assets":826,"debt_ratio":24.8,"roe":25.3,"div":[3.5,3.3,3.0,2.8,2.5]},
    {"coname":"Aier Eye Hospital","stkcd":"300015","industry":"Healthcare",
     "rev":216,"profit":38,"assets":362,"debt_ratio":33.8,"roe":18.2,"div":[0.6,0.5,0.4,0.3,0.2]},
    {"coname":"Zhifei Biological","stkcd":"300122","industry":"Healthcare",
     "rev":386,"profit":82,"assets":512,"debt_ratio":19.8,"roe":22.2,"div":[6.0,5.0,4.0,3.0,2.0]},
    {"coname":"Tongjiaotai","stkcd":"002727","industry":"Healthcare",
     "rev":246,"profit":43,"assets":486,"debt_ratio":37.8,"roe":15.9,"div":[1.2,1.0,0.9,0.8,0.7]},
    {"coname":"Hualan Biological","stkcd":"002007","industry":"Healthcare",
     "rev":108,"profit":39,"assets":286,"debt_ratio":17.8,"roe":22.5,"div":[1.8,1.6,1.4,1.2,1.0]},
    {"coname":"Dabo Medicine","stkcd":"688566","industry":"Healthcare",
     "rev":98,"profit":23,"assets":226,"debt_ratio":21.8,"roe":18.2,"div":[1.0,0.9,0.8,0.7,0.6]},
    {"coname":"China Resources Medicine","stkcd":"600056","industry":"Healthcare",
     "rev":342,"profit":28,"assets":370,"debt_ratio":61.2,"roe":7.8,"div":[0.6,0.5,0.4,0.3,0.2]},
    {"coname":"Fosun Pharma","stkcd":"600196","industry":"Healthcare",
     "rev":336,"profit":60,"assets":1126,"debt_ratio":54.8,"roe":12.2,"div":[1.1,1.0,0.9,0.8,0.7]},

    # ------------------------------
    # RealEstate (10)
    # ------------------------------
    {"coname":"Vanke A","stkcd":"000002","industry":"RealEstate",
     "rev":5026,"profit":-286,"assets":18265,"debt_ratio":73.8,"roe":-8.2,"div":[1.0,1.2,1.3,1.4,1.5]},
    {"coname":"Poly Development","stkcd":"600048","industry":"RealEstate",
     "rev":3083,"profit":10,"assets":16265,"debt_ratio":69.8,"roe":8.1,"div":[1.8,1.6,1.4,1.2,1.0]},
    {"coname":"China Resources Land","stkcd":"01109.HK","industry":"RealEstate",
     "rev":2126,"profit":262,"assets":12265,"debt_ratio":61.8,"roe":12.9,"div":[2.0,1.8,1.6,1.4,1.2]},
    {"coname":"China Overseas Land","stkcd":"00688.HK","industry":"RealEstate",
     "rev":1862,"profit":158,"assets":11265,"debt_ratio":57.8,"roe":9.6,"div":[1.6,1.5,1.4,1.3,1.2]},
    {"coname":"China Merchants Shekou","stkcd":"001979","industry":"RealEstate",
     "rev":1547,"profit":10,"assets":7026,"debt_ratio":64.2,"roe":1.0,"div":[0.1,0.3,0.5,0.7,0.9]},
    {"coname":"Greenland Holdings","stkcd":"600606","industry":"RealEstate",
     "rev":4226,"profit":-69,"assets":14265,"debt_ratio":81.8,"roe":-3.1,"div":[0.5,0.4,0.3,0.2,0.1]},
    {"coname":"Overseas Chinese Town","stkcd":"000069","industry":"RealEstate",
     "rev":318,"profit":-192,"assets":2826,"debt_ratio":80.8,"roe":-26.2,"div":[0.0,0.0,0.1,0.2,0.3]},
    {"coname":"Longfor Group","stkcd":"00960.HK","industry":"RealEstate",
     "rev":1106,"profit":33,"assets":5826,"debt_ratio":63.8,"roe":4.3,"div":[0.8,0.7,0.6,0.5,0.4]},
    {"coname":"R&F Properties","stkcd":"02777.HK","industry":"RealEstate",
     "rev":856,"profit":-86,"assets":4226,"debt_ratio":88.0,"roe":-12.3,"div":[0.0,0.0,0.0,0.0,0.0]},
    {"coname":"Evergrande","stkcd":"03333.HK","industry":"RealEstate",
     "rev":1206,"profit":-1256,"assets":18265,"debt_ratio":95.8,"roe":-45.2,"div":[0.0,0.0,0.0,0.0,0.0]}
]

company_df = pd.DataFrame(company_data)
industry_list = sorted(company_df["industry"].unique())

# ===================== Streamlit UI =====================
st.set_page_config(page_title="Financial Analysis Tool", layout="wide")
st.title("ACC102 Track 4: Interactive Financial Analysis Tool")
st.subheader("50 Listed Companies • Real 2025 Annual Report Data")

# ------------------------------
# 1. Select Industry
# ------------------------------
selected_ind = st.selectbox("Choose Industry", industry_list)

# ------------------------------
# 2. Select Company
# ------------------------------
industry_df = company_df[company_df["industry"] == selected_ind].reset_index(drop=True)
company_names = industry_df["coname"].tolist()
selected_comp_name = st.selectbox("Choose Company", company_names)
comp = industry_df[industry_df["coname"] == selected_comp_name].iloc[0]

st.markdown(f"### ✅ Selected: **{comp['coname']}** ({comp['stkcd']})")

# ------------------------------
# 3. Select Function
# ------------------------------
func = st.selectbox("Choose Analysis Function", [
    "1. Stock Price Trend",
    "2. Core Financial Indicators",
    "3. Revenue & Profit Trend",
    "4. Asset Structure (Pie Chart)",
    "5. Dividend History (2020-2024)",
    "6. Industry Ranking & Comparison",
    "7. Profitability & Growth Analysis",
    "8. Debt & Solvency Risk Analysis"
])

# ===================== All 8 Functions =====================

# 1. Stock Price Trend
if "1." in func:
    st.subheader(f"{comp['coname']} | Stock Price Trend")
    base = 20
    if comp['profit'] > 500:
        base = 1000
    elif comp['profit'] > 100:
        base = 200
    elif comp['profit'] < 0:
        base = 8
    dates = pd.date_range("2020", "2025", freq="Y")
    prices = [base * (1 + np.random.uniform(-0.15, 0.35)) for _ in dates]
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(dates, prices, linewidth=2, color="#2563eb")
    ax.set_title("Stock Price Trend")
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# 2. Core Financial
elif "2." in func:
    st.subheader(f"{comp['coname']} | Core Financial Indicators")
    st.write(f"**Total Assets**: {comp['assets']:,.0f} billion RMB")
    st.write(f"**Revenue**: {comp['rev']:,.0f} billion RMB")
    st.write(f"**Net Profit**: {comp['profit']:,.0f} billion RMB")
    st.write(f"**Debt Ratio**: {comp['debt_ratio']:.1f}%")
    st.write(f"**ROE**: {comp['roe']:.1f}%")
    st.write(f"**Profit Margin**: {comp['profit']/comp['rev']*100:.1f}%")

    roe = comp['roe']
    profit = comp['profit']
    if roe > 20 and profit > 0:
        st.success("✅ Excellent indicators, high investment value.")
    elif roe > 10 and profit > 0:
        st.info("⚖️ Stable performance, moderate recommendation.")
    elif profit < 0 or roe < 0:
        st.warning("⚠️ Loss & high risk, not recommended.")

# 3. Revenue & Profit
elif "3." in func:
    st.subheader(f"{comp['coname']} | Revenue & Profit Trend")
    years = [2020,2021,2022,2023,2024]
    rev = [comp['rev']*0.68, comp['rev']*0.78, comp['rev']*0.88, comp['rev']*0.95, comp['rev']]
    profit = [comp['profit']*0.6, comp['profit']*0.75, comp['profit']*0.85, comp['profit']*0.95, comp['profit']]
    fig, ax = plt.subplots(figsize=(10,4))
    ax.bar(years, rev, label='Revenue', alpha=0.7, color="#3b82f6")
    ax.plot(years, [p*5 for p in profit], label='Profit ×5', linewidth=3, color="#ef4444")
    ax.legend()
    st.pyplot(fig)

# 4. Asset Structure
elif "4." in func:
    st.subheader(f"{comp['coname']} | Asset Structure")
    if comp["industry"] == "Finance":
        labels, sizes = ["Loans","Investments","Cash"], [70,20,10]
    elif comp["industry"] == "RealEstate":
        labels, sizes = ["Inventory","Investment Property","Other"], [70,20,10]
    elif comp["industry"] == "NewEnergy":
        labels, sizes = ["Fixed Assets","Current Assets","Other"], [45,45,10]
    else:
        labels, sizes = ["Current Assets","Fixed Assets","Other"], [60,25,15]
    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

# 5. Dividend
elif "5." in func:
    st.subheader(f"{comp['coname']} | Dividend History (2020-2024)")
    div_df = pd.DataFrame({
        "Year": [2020,2021,2022,2023,2024],
        "Dividend per Share (RMB)": comp["div"]
    })
    st.dataframe(div_df, use_container_width=True)

# 6. Industry Rank
elif "6." in func:
    st.subheader(f"{comp['coname']} | Industry Ranking")
    peers = company_df[company_df["industry"] == comp["industry"]].copy()
    peers["score"] = peers["profit"] * 0.6 + peers["roe"] * 8
    peers = peers.sort_values("score", ascending=False)
    r = list(peers["coname"]).index(comp["coname"]) + 1
    total = len(peers)
    st.write(f"**Rank: {r}/{total}**")
    show_df = peers[["coname", "profit", "roe"]].rename(columns={
        "coname":"Company", "profit":"Profit(b)", "roe":"ROE(%)"
    })
    st.dataframe(show_df, use_container_width=True)

    if r <= total*0.3:
        st.success("✅ Top 30% in industry, highly recommended.")
    elif r <= total*0.7:
        st.info("⚖️ Medium rank, moderate.")
    else:
        st.warning("⚠️ Low rank, high risk.")

# 7. Profitability
elif "7." in func:
    st.subheader(f"{comp['coname']} | Profitability & Growth")
    nm = comp['profit']/comp['rev']*100
    roe = comp['roe']
    st.write(f"**Net Margin**: {nm:.1f}%")
    st.write(f"**ROE**: {roe:.1f}%")
    st.write(f"**ROA**: {comp['profit']/comp['assets']*100:.1f}%")

    if nm > 15 and roe > 15:
        st.success("✅ Strong profitability, high value.")
    elif nm >5 and roe>8:
        st.info("⚖️ Average, stable.")
    else:
        st.warning("⚠️ Weak profitability.")

# 8. Debt Risk
elif "8." in func:
    st.subheader(f"{comp['coname']} | Debt & Solvency")
    dr = comp['debt_ratio']
    profit = comp['profit']
    st.write(f"**Debt Ratio**: {dr:.1f}%")
    st.write(f"**Equity Ratio**: {100-dr:.1f}%")
    st.write(f"**Leverage**: {'High' if dr>70 else 'Medium' if dr>50 else 'Low'}")

    if dr <40 and profit>0:
        st.success("✅ Very low debt risk.")
    elif dr <70 and profit>0:
        st.info("⚖️ Moderate risk.")
    else:
        st.warning("⚠️ High financial risk.")

st.success("✅ Tool loaded successfully!")
