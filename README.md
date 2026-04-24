# Interactive Financial Analysis Dashboard

## 1. Problem & User

This project provides an interactive financial dashboard for analyzing listed companies using official annual report data. It is designed for students, investors, and analysts who need a clear, data-driven view of company performance and financial health. This tool helps users quickly interpret financial data, compare companies, and support basic investment or academic analysis decisions.

## 2. Data

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

* Consumer sector companies (e.g., Kweichow Moutai, Wuliangye) show strong and stable growth in both revenue and net profit, with consistently high ROE, indicating strong pricing power and profitability
* Financial institutions (e.g., ICBC, China Construction Bank) maintain extremely high revenue and profit levels with stable growth, but exhibit very high debt ratios, reflecting industry characteristics of high leverage
* New energy companies (e.g., CATL, BYD) demonstrate rapid revenue expansion, but profitability is more volatile, with some firms experiencing losses or sharp fluctuations due to market cycles and cost pressures
* Pharmaceutical companies show mixed performance: leading firms (e.g., Mindray, WuXi AppTec) achieve steady growth and strong margins, while others (e.g., BeiGene) continue to operate at losses due to high R&D investment
* Real estate companies exhibit declining revenue and profitability after 2021, with several firms showing negative profits and very high debt ratios, indicating increased financial risk and industry downturn
* Stock price trends do not always align with financial performance (e.g., some high-performing firms show declining prices), suggesting market sentiment and external factors also play a significant role

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
Streamlit App Link：
https://acc102-financial-analysis-tool-6ecmpakpxuvkuxfmjjsuxs.streamlit.app/

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
