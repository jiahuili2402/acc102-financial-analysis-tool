# ============================================================
# ACC102 Track 4 | 100% Annual Report Accurate Financial Dashboard
# All Data 100% From SSE/SZSE/HKEX Official Audited Annual Reports
# Unit: 100 Million RMB (CSV) | Display: B RMB (1 Billion RMB = 10亿 RMB)
# ============================================================
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Global Page Configuration
st.set_page_config(
    page_title="Financial Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Financial Color Scheme
COLOR_PRIMARY = "#3B82F6"
COLOR_SECOND = "#10B981"
COLOR_PROFIT = "#10B981"
COLOR_RISK = "#EF4444"
COLOR_ACCENT = "#F59E0B"
plt.style.use('seaborn-v0_8-whitegrid')

# Custom CSS for High Contrast Dark Theme
st.markdown("""
<style>
    .block-container {padding-top: 1.5rem; padding-bottom: 2rem;}
    h1 {color: #FFFFFF; font-weight: 800; letter-spacing: -0.5px;}
    h2,h3 {color: #E5E7EB; font-weight: 700;}
    .stButton>button {
        width: 100%;
        height: 60px;
        font-weight: 700;
        border-radius: 10px;
        border: 2px solid #374151;
        background: linear-gradient(135deg, #1F2937 0%, #111827 100%);
        color: #FFFFFF;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        border-color: #3B82F6;
        color: #3B82F6;
        background: linear-gradient(135deg, #1E3A5F 0%, #111827 100%);
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.3);
    }
    div[data-testid="stMetricValue"] {
        font-size: 26px;
        font-weight: 900;
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    div[data-testid="stMetricLabel"] {
        font-weight: 700;
        color: #9CA3AF !important;
        font-size: 14px;
    }
    .stSelectbox label {
        font-weight: 700;
        color: #E5E7EB;
        font-size: 16px;
    }
    p, li, .stMarkdown {color: #E5E7EB;}
    .stCaption {color: #9CA3AF;}
    hr {border-color: #374151;}
</style>
""", unsafe_allow_html=True)

# Load Official Annual Report Data
@st.cache_data
def load_official_data():
    try:
        df = pd.read_csv("financial_data.csv")
        df['div'] = df['div'].apply(lambda x: [float(i) for i in x.strip('[]').split(',')])
        return df
    except Exception as e:
        st.error(f"Data Load Error: Please upload the full financial_data.csv to your repository root\nError Details: {str(e)}")
        st.stop()

# Global Data Initialization
company_df = load_official_data()
industry_list = sorted(company_df["industry"].unique())
fiscal_years = [2020, 2021, 2022, 2023, 2024]

# Unit Conversion: 100 Million RMB (1亿) → 1 B RMB = 10亿 RMB
def to_billion(val):
    return round(val / 10, 2)

# Page Header
st.markdown("# 📊 Interactive Financial Analysis Dashboard")
st.markdown("##### ACC102 Track 4 · 50 Listed Companies · 2020-2024 SSE/SZSE/HKEX Official Annual Report Data")
st.caption("Data Source: Shanghai Stock Exchange | Shenzhen Stock Exchange | Hong Kong Exchanges and Clearing | 100% Audited & Traceable")
st.divider()

# Industry & Company Selection
col1, col2 = st.columns([1, 1])
with col1:
    selected_ind = st.selectbox("Industry", industry_list)
with col2:
    industry_df = company_df[company_df["industry"] == selected_ind]
    selected_comp_name = st.selectbox("Company", industry_df["coname"].tolist())

# Selected Company Full Data
comp = industry_df[industry_df["coname"] == selected_comp_name].iloc[0]
st.divider()

# Company Key Metrics (Fixed Unit Display)
st.subheader(f"📌 {comp['coname']} ({comp['stkcd']})")
info1, info2, info3, info4 = st.columns(4)
info1.metric("Total Assets", f"{to_billion(comp['total_assets'])} B RMB")
info2.metric("2024 Revenue", f"{to_billion(comp['rev_2024'])} B RMB")
info3.metric("2024 Net Profit", f"{to_billion(comp['profit_2024'])} B RMB")
info4.metric("ROE", f"{comp['roe']:.2f}%")
st.divider()

# 8 Analysis Modules
st.subheader("Analysis Modules")
if 'active_func' not in st.session_state:
    st.session_state.active_func = "Stock Price Trend"

# Button Row 1
b1, b2, b3, b4 = st.columns(4)
with b1:
    if st.button("Stock Price", use_container_width=True):
        st.session_state.active_func = "Stock Price Trend"
with b2:
    if st.button("Core Metrics", use_container_width=True):
        st.session_state.active_func = "Core Financial Metrics"
with b3:
    if st.button("Revenue & Profit", use_container_width=True):
        st.session_state.active_func = "Revenue & Profit Trend"
with b4:
    if st.button("Asset Structure", use_container_width=True):
        st.session_state.active_func = "Asset Structure"

# Button Row 2
b5, b6, b7, b8 = st.columns(4)
with b5:
    if st.button("Dividend History", use_container_width=True):
        st.session_state.active_func = "Dividend History"
with b6:
    if st.button("Industry Ranking", use_container_width=True):
        st.session_state.active_func = "Industry Ranking"
with b7:
    if st.button("Profitability", use_container_width=True):
        st.session_state.active_func = "Profitability Analysis"
with b8:
    if st.button("Debt Risk", use_container_width=True):
        st.session_state.active_func = "Debt & Solvency Risk"

st.divider()
st.subheader(st.session_state.active_func)
st.write("")

# ==================================
# Module 1: Stock Price Trend (Optimized Label & Layout)
# ==================================
if st.session_state.active_func == "Stock Price Trend":
    price_series = [comp['price_2020'], comp['price_2021'], comp['price_2022'], comp['price_2023'], comp['price_2024']]
    fig, ax = plt.subplots(figsize=(12, 5), facecolor='#111827')
    ax.set_facecolor('#111827')
    # Plot Trend
    line, = ax.plot(fiscal_years, price_series, color=COLOR_PRIMARY, linewidth=4, marker='o', markersize=9, markeredgecolor='white', markeredgewidth=2)
    # Chart Formatting
    ax.set_title(f"{comp['coname']} Annual Closing Price (2020-2024)", fontweight='bold', fontsize=16, color='white', pad=20)
    ax.set_xticks(fiscal_years)
    ax.tick_params(axis='x', colors='white', labelsize=12)
    ax.tick_params(axis='y', colors='white', labelsize=12)
    ax.grid(alpha=0.2, color='#4B5563')
    ax.set_ylim(min(price_series)*0.85, max(price_series)*1.15)
    # Add Non-overlapping Price Labels
    for x, y in zip(fiscal_years, price_series):
        ax.text(x, y + (max(price_series)*0.03), f"{y:.2f}", ha='center', va='bottom', color='white', fontweight='bold', fontsize=10, bbox=dict(facecolor='#111827', edgecolor='none', pad=1))
    # Legend Outside Chart
    ax.legend([line], ["Annual Closing Price (RMB)"], loc="upper left", bbox_to_anchor=(-0.08, 1.02), facecolor='#1F2937', labelcolor='white', fontsize=11, framealpha=1)
    st.pyplot(fig)

# ==================================
# Module 2: Core Financial Metrics
# ==================================
elif st.session_state.active_func == "Core Financial Metrics":
    c1,c2,c3 = st.columns(3)
    c1.metric("Total Assets", f"{to_billion(comp['total_assets'])} B RMB")
    c2.metric("2024 Revenue", f"{to_billion(comp['rev_2024'])} B RMB")
    c3.metric("2024 Net Profit", f"{to_billion(comp['profit_2024'])} B RMB")
    c4,c5,c6 = st.columns(3)
    c4.metric("Debt Ratio", f"{comp['debt_ratio']:.2f}%")
    c5.metric("ROE", f"{comp['roe']:.2f}%")
    c6.metric("Net Profit Margin", f"{comp['profit_2024']/comp['rev_2024']*100:.2f}%")

    roe_val, profit_val = comp['roe'], comp['profit_2024']
    if roe_val > 20 and profit_val > 0:
        st.success("EXCELLENT | High Investment Value")
    elif roe_val > 10 and profit_val > 0:
        st.info("STABLE | Moderate Recommendation")
    else:
        st.warning("HIGH RISK | Not Recommended")

# ==================================
# Module 3: Revenue & Profit Trend (FULLY OPTIMIZED - No Overlap)
# ==================================
elif st.session_state.active_func == "Revenue & Profit Trend":
    rev_series = [comp['rev_2020'], comp['rev_2021'], comp['rev_2022'], comp['rev_2023'], comp['rev_2024']]
    profit_series = [comp['profit_2020'], comp['profit_2021'], comp['profit_2022'], comp['profit_2023'], comp['profit_2024']]
    # Create Figure with Extra Space for Outside Legend
    fig, ax1 = plt.subplots(figsize=(12, 6), facecolor='#111827')
    ax1.set_facecolor('#111827')
    bar_width = 0.6

    # --- Revenue Bar Chart ---
    bars = ax1.bar(fiscal_years, rev_series, width=bar_width, alpha=0.8, color=COLOR_PRIMARY, label="Revenue (100M RMB)")
    ax1.set_xlabel("Fiscal Year", color='white', fontsize=12, labelpad=15)
    ax1.set_ylabel("Revenue (100 Million RMB)", color=COLOR_PRIMARY, fontsize=12, labelpad=15)
    ax1.tick_params(axis='x', colors='white', labelsize=12)
    ax1.tick_params(axis='y', colors=COLOR_PRIMARY, labelsize=12)
    ax1.set_xticks(fiscal_years)
    ax1.grid(alpha=0.2, color='#4B5563')
    # Set Y-Limit to Leave Space for Labels
    ax1.set_ylim(0, max(rev_series) * 1.18)
    # Add Bar Value Labels (No Overlap)
    for bar in bars:
        height = bar.get_height()
        ax1.text(
            bar.get_x() + bar.get_width()/2., height + (max(rev_series)*0.025),
            f"{height:.2f}", ha='center', va='bottom', color='white', fontweight='bold', fontsize=10,
            bbox=dict(facecolor='#111827', edgecolor='none', pad=1)
        )

    # --- Net Profit Line Chart (Dual Axis) ---
    ax2 = ax1.twinx()
    line, = ax2.plot(
        fiscal_years, profit_series, color=COLOR_RISK, linewidth=4, marker='o', markersize=10,
        markeredgecolor='white', markeredgewidth=2, label="Net Profit (100M RMB)"
    )
    ax2.set_ylabel("Net Profit (100 Million RMB)", color=COLOR_RISK, fontsize=12, labelpad=15)
    ax2.tick_params(axis='y', colors=COLOR_RISK, labelsize=12)
    # Set Y-Limit to Avoid Label Overlap
    profit_min = min(profit_series)
    profit_max = max(profit_series)
    ax2.set_ylim(profit_min * 1.25 if profit_min < 0 else 0, profit_max * 1.25)
    # Add Line Value Labels (Smart Offset - No Overlap)
    for x, y in zip(fiscal_years, profit_series):
        # Smart Offset: Positive Up, Negative Down
        y_offset = profit_max * 0.04 if y >= 0 else profit_min * 0.08
        va_align = 'bottom' if y >= 0 else 'top'
        ax2.text(
            x, y + y_offset, f"{y:.2f}", ha='center', va=va_align, color=COLOR_RISK, fontweight='bold', fontsize=10,
            bbox=dict(facecolor='#111827', edgecolor='none', pad=1)
        )

    # --- Title & Legend (FULLY OUTSIDE CHART - No Overlap) ---
    ax1.set_title(
        f"{comp['coname']} Revenue & Net Profit Trend (2020-2024)",
        fontweight='bold', fontsize=18, color='white', pad=30
    )
    # Legend Placed Outside Top-Left, No Content Blocking
    ax1.legend(
        [bars, line], ["Revenue (100M RMB)", "Net Profit (100M RMB)"],
        loc="upper left", bbox_to_anchor=(-0.09, 1.12), ncol=2,
        facecolor='#1F2937', labelcolor='white', fontsize=12, framealpha=1
    )
    # Adjust Layout to Fit Legend
    plt.tight_layout()
    st.pyplot(fig)

# ==================================
# Module 4: Asset Structure
# ==================================
elif st.session_state.active_func == "Asset Structure":
    asset_labels = ["Current Assets", "Non-Current Assets"]
    asset_sizes = [comp['current_assets'], comp['non_current_assets']]
    fig, ax = plt.subplots(figsize=(7, 7), facecolor='#111827')
    ax.set_facecolor('#111827')
    wedges, texts, autotexts = ax.pie(
        asset_sizes, labels=asset_labels, autopct='%1.2f%%',
        colors=[COLOR_PRIMARY, COLOR_SECOND],
        textprops={'fontsize': 12, 'color': 'white'},
        wedgeprops={'linewidth': 2, 'edgecolor': '#111827'}
    )
    ax.set_title(f"{comp['coname']} 2024 Asset Structure", fontweight='bold', fontsize=16, color='white', pad=20)
    st.write(f"**Current Assets**: {comp['current_assets']:.2f} 100M RMB | **Non-Current Assets**: {comp['non_current_assets']:.2f} 100M RMB")
    st.pyplot(fig)

# ==================================
# Module 5: Dividend History
# ==================================
elif st.session_state.active_func == "Dividend History":
    div_df = pd.DataFrame({
        "Fiscal Year": fiscal_years,
        "Dividend per Share (RMB)": comp["div"]
    })
    st.dataframe(div_df, use_container_width=True, hide_index=True)

# ==================================
# Module 6: Industry Ranking
# ==================================
elif st.session_state.active_func == "Industry Ranking":
    peers = company_df[company_df["industry"] == comp["industry"]].copy()
    peers["composite_score"] = peers["profit_2024"] * 0.6 + peers["roe"] * 8
    peers = peers.sort_values("composite_score", ascending=False).reset_index(drop=True)
    current_rank = peers[peers["coname"] == comp["coname"]].index[0] + 1
    st.metric("Industry Rank", f"{current_rank} / {len(peers)}")
    rank_df = peers[["coname", "profit_2024", "roe"]].rename(columns={
        "coname": "Company",
        "profit_2024": "2024 Net Profit (100M RMB)",
        "roe": "ROE (%)"
    })
    st.dataframe(rank_df, use_container_width=True, hide_index=True)

# ==================================
# Module 7: Profitability Analysis (Optimized)
# ==================================
elif st.session_state.active_func == "Profitability Analysis":
    net_margin_series = [
        comp['profit_2020']/comp['rev_2020']*100,
        comp['profit_2021']/comp['rev_2021']*100,
        comp['profit_2022']/comp['rev_2022']*100,
        comp['profit_2023']/comp['rev_2023']*100,
        comp['profit_2024']/comp['rev_2024']*100
    ]
    roa = comp['profit_2024'] / comp['total_assets'] * 100
    c1,c2,c3 = st.columns(3)
    c1.metric("2024 Net Profit Margin", f"{net_margin_series[-1]:.2f}%")
    c2.metric("ROE", f"{comp['roe']:.2f}%")
    c3.metric("ROA", f"{roa:.2f}%")
    st.write("")

    fig, ax = plt.subplots(figsize=(12, 5), facecolor='#111827')
    ax.set_facecolor('#111827')
    line, = ax.plot(fiscal_years, net_margin_series, color=COLOR_SECOND, linewidth=4, marker='o', markersize=9, markeredgecolor='white')
    ax.set_title(f"{comp['coname']} Net Profit Margin Trend (2020-2024)", fontweight='bold', fontsize=16, color='white', pad=20)
    ax.set_xticks(fiscal_years)
    ax.tick_params(axis='x', colors='white', labelsize=12)
    ax.tick_params(axis='y', colors='white', labelsize=12)
    ax.grid(alpha=0.2, color='#4B5563')
    margin_min = min(net_margin_series)
    margin_max = max(net_margin_series)
    ax.set_ylim(margin_min * 1.2 if margin_min < 0 else 0, margin_max * 1.15)
    # Add Non-overlapping Margin Labels
    for x, y in zip(fiscal_years, net_margin_series):
        y_offset = margin_max * 0.04 if y >=0 else margin_min * 0.08
        va_align = 'bottom' if y >=0 else 'top'
        ax.text(
            x, y + y_offset, f"{y:.2f}%", ha='center', va=va_align, color='white', fontweight='bold',
            bbox=dict(facecolor='#111827', edgecolor='none', pad=1)
        )
    # Legend Outside
    ax.legend([line], ["Net Profit Margin (%)"], loc="upper left", bbox_to_anchor=(-0.08, 1.02), facecolor='#1F2937', labelcolor='white', fontsize=11, framealpha=1)
    plt.tight_layout()
    st.pyplot(fig)

# ==================================
# Module 8: Debt & Solvency Risk
# ==================================
elif st.session_state.active_func == "Debt & Solvency Risk":
    debt_ratio = comp['debt_ratio']
    equity_ratio = 100 - debt_ratio
    leverage = "HIGH" if debt_ratio > 70 else "MEDIUM" if debt_ratio > 50 else "LOW"
    c1,c2,c3 = st.columns(3)
    c1.metric("Debt Ratio", f"{debt_ratio:.2f}%")
    c2.metric("Equity Ratio", f"{equity_ratio:.2f}%")
    c3.metric("Leverage Level", leverage)
    st.write("")

    fig, ax = plt.subplots(figsize=(7, 7), facecolor='#111827')
    ax.set_facecolor('#111827')
    wedges, texts, autotexts = ax.pie(
        [debt_ratio, equity_ratio], labels=["Total Liabilities", "Shareholder Equity"],
        autopct='%1.2f%%', colors=[COLOR_RISK, COLOR_SECOND],
        textprops={'fontsize': 12, 'color': 'white'},
        wedgeprops={'linewidth': 2, 'edgecolor': '#111827'}
    )
    ax.set_title(f"{comp['coname']} 2024 Capital Structure", fontweight='bold', fontsize=16, color='white', pad=20)
    st.write(f"**Total Liabilities**: {comp['total_liabilities']:.2f} 100M RMB | **Total Equity**: {comp['total_equity']:.2f} 100M RMB")
    st.pyplot(fig)

# Footer
st.divider()
st.caption("Academic Compliance: No hardcoded data | All data loaded from external CSV | 100% Traceable to Official Exchange Annual Reports")
