# Interactive Financial Analysis Dashboard

## 1. Problem & User

This project provides an interactive financial dashboard for analyzing listed companies using official annual report data. It is designed for students, investors, and analysts who need a clear, data-driven view of company performance and financial health. This tool helps users quickly interpret financial data, compare companies, and support basic investment or academic analysis decisions.

## 2. Data (source + access date + key fields)

* **Source**: Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), Hong Kong Exchanges and Clearing (HKEX) official annual reports
* **Access Date**: April 2026
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

* Load and clean financial data using pandas
* Cache dataset with `@st.cache_data` for performance
* Build interactive UI with Streamlit
* Generate financial metrics and ratios dynamically
* Visualize trends using matplotlib:

  * Line charts (price, margins)
  * Bar + line combination charts (revenue & profit)
  * Pie charts (asset and capital structure)
* Implement modular dashboard navigation with session state

## 4. Key Findings

* Revenue and net profit trends reveal differences in growth stability and potential performance risks across companies
* ROE and profit margin help identify high-quality, efficient firms
* Debt ratio highlights financial risk and leverage level
* Industry ranking provides relative competitive positioning
* Asset and capital structure show how companies allocate resources and manage liabilities

## 5. How to run

```bash
# Clone the repository
git clone https://github.com/jiahuili2402/acc102-financial-analysis-tool
cd acc102-financial-analysis-tool

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Make sure the `financial_data.csv` file is in the same directory as `app.py`.

## 6. Product link

GitHub Repository:
[https://github.com/jiahuili2402/acc102-financial-analysis-tool](https://github.com/jiahuili2402/acc102-financial-analysis-tool)

## Project Structure

* app.py – main Streamlit application
* financial_data.csv – dataset
* requirements.txt – dependencies
* README.md – project documentation

## 7. Limitations & next steps

* Dataset limited to selected listed companies (not full market coverage)
* No real-time data updates (static annual report data)
* Lacks advanced financial modeling (e.g., forecasting, valuation models)

Future improvements:

* Integrate real-time APIs
* Add valuation models (DCF, PE comparison)
* Enhance UI with more interactive filtering and benchmarking tools
