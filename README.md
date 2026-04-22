# ACC102 Track4 Interactive Financial Analysis Tool

## 1. Problem & User
This project is designed for students majoring in finance and accounting and beginners in financial analysis. It solves problems such as low efficiency, error-prone manual calculation of financial indicators, difficulties in quickly comparing multiple companies, and unintuitive trend visualization. It provides a one-stop, interactive, and repeatable financial analysis tool.

## 2. Data
- Data source: Public annual financial statement data of listed companies
- Access date: April 21, 2026
- Key fields: Company name, stock code, industry, year, operating income, net profit, total assets, total liabilities, ROE, debt-to-asset ratio, gross profit margin, closing price, dividend history

## 3. Methods
1. Import necessary libraries including Streamlit, Pandas, Matplotlib, and NumPy for data processing and visualization.
2. Load the local CSV financial dataset into a Pandas DataFrame for analysis.
3. Set up a Streamlit page configuration and title to form the basic interactive interface.
4. Create interactive selection boxes to allow users to filter data by industry and company.
5. Filter the dataset based on user selection to generate targeted analysis data.
6. Display key financial indicators of the selected company in text and table format, including operating income, net profit, total assets, total liabilities, ROE, debt-to-asset ratio, and gross profit margin.
7. Generate a variety of visualizations including line charts for stock price trends, bar charts for income and profit, and pie charts for asset-liability structure and profit composition.
8. Display all charts and analysis results in a clear and readable layout for users.

## 4. Key Findings
1. Leading enterprises have maintained steady growth in operating income and net profit over the past five years, with strong performance resilience and low volatility, significantly outperforming the industry average.
2. Gross profit margin and ROE differ noticeably across industries. Asset-light industries generally show higher profit margins and asset returns, while asset-heavy industries tend to have higher debt ratios.
3. The overall solvency of sampled companies is healthy, with most firms maintaining a reasonable debt-to-asset ratio, although some highly leveraged companies face certain liquidity pressure.
4. Financial performance is moderately correlated with stock price trends. Companies with consistent improvements in revenue and profit generally have more stable and stronger stock price performance.

## 5. How to run
1. Install required packages: pip install pandas numpy matplotlib streamlit
2. Open the project folder and run in the terminal: streamlit run app.py
3. The browser will automatically open the interactive interface. Use the on-screen buttons to select analysis functions.

## 6. Product link / Demo
- GitHub Repository: https://github.com/jiahuili2402/acc102-financial-analysis-tool
- Demo: Run app.py locally to launch the interactive tool, or visit the online Streamlit app link

## 7. Limitations & next steps
- Limitations: Limited coverage of companies; no real-time data update; no advanced modules such as DuPont analysis or forecasting models.
- Next steps: Expand coverage of industries and companies; integrate data APIs for automatic updates; add DuPont analysis, chart export, and industry ranking functions.
