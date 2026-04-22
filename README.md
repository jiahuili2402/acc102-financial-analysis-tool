# Financial Analysis Dashboard

## 1. Problem & User (1–2 sentences)

This project provides an interactive financial dashboard for analyzing listed companies using official annual report data. It is designed for students, investors, and analysts who need a clear, data-driven view of company performance and financial health.

## 2. Data (source + access date + key fields)

* **Source**: Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), Hong Kong Exchanges and Clearing (HKEX) official annual reports
* **Access Date**: 2025–2026
* **File**: `financial_data.csv`
* **Key Fields**:

  * Company info: `coname`, `stkcd`, `industry`
  * Financials: `total_assets`, `total_liabilities`, `total_equity`
  * Revenue & profit: `rev_2020–2024`, `profit_2020–2024`
  * Ratios: `roe`, `debt_ratio`
  * Prices: `price_2020–2024`
  * Dividends: `div`
  * Asset structure: `current_assets`, `non_current_assets`

## 3. Methods (main Python steps)

* Load and clean financial data using **pandas**
* Cache dataset with `@st.cache_data` for performance
* Build interactive UI with **Streamlit**
* Generate financial metrics and ratios dynamically
* Visualize trends using **matplotlib**:

  * Line charts (price, margins)
  * Bar + line combination charts (revenue & profit)
  * Pie charts (asset and capital structure)
* Implement modular dashboard navigation with session state

## 4. Key Findings (3–5 bullets)

* Revenue and net profit trends reveal company growth and volatility over time
* ROE and profit margin help identify high-quality, efficient firms
* Debt ratio highlights financial risk and leverage level
* Industry ranking provides relative competitive positioning
* Asset and capital structure show how companies allocate resources and manage liabilities

## 5. How to run (optional but valuable)

```bash
# Clone the repository
git clone <your-repo-link>
cd <your-repo-folder>

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 6. Product link / Demo

Local deployment via Streamlit:

```bash
streamlit run app.py
```

## 7. Limitations & next steps

* Dataset limited to selected listed companies (not full market coverage)
* No real-time data updates (static annual report data)
* Lacks advanced financial modeling (e.g., forecasting, valuation models)
* Future improvements:

  * Integrate real-time APIs
  * Add valuation models (DCF, PE comparison)
  * Enhance UI with more interactive filtering and benchmarking tools
