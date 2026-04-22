# ACC102 Track 4: Interactive Financial Analysis Tool

## 1. Problem & User
This project develops a lightweight interactive financial analysis tool to help users conduct corporate performance comparison, ratio calculation, and data visualization efficiently. It is designed for students and beginners in finance and accounting.

## 2. Data
- Data source: Public corporate financial statement data of listed companies
- Access date: April 21, 2026
- Key fields: Company name, stock code, industry, year, operating income, net profit, total assets, total liabilities, ROE, debt-to-asset ratio, gross profit margin, closing price, dividend history

## 3. Methods
1.  Data loading and formatting: Read the local CSV financial dataset and load it into a Pandas DataFrame for subsequent analysis.
2.  Data cleaning and preprocessing: Perform basic formatting to ensure consistent column names and standardized numerical formats.
3.  Financial indicator display: Directly extract and present key pre-calculated indicators including operating income, net profit, total assets, total liabilities, ROE, debt-to-asset ratio, and gross profit margin.
4.  Interactive filtering and function control: Build Streamlit-based selection tools to support filtering by industry and company name, enabling cross-company horizontal comparison.
5.  Chart plotting and result output: Automatically generate stock price trend charts and financial indicator bar charts based on filtered results to clearly show business performance and market trends.
6.  Interactive interface and presentation: Use buttons, select boxes, and layout panels to create a visual operating interface, and present analysis results in tables, charts, and text.

## 4. Key Findings
1.  Leading enterprises maintain steady growth in operating income and net profit over the past five years, with strong performance resilience and low volatility.
2.  Gross profit margin and ROE differ noticeably across industries, with asset-light industries generally showing higher profit margins and asset returns.
3.  Overall corporate solvency stays healthy and low-risk, with most companies maintaining a reasonable debt-to-asset ratio.
4.  Five-year trend charts clearly reflect business changes and the correlation between financial performance and stock price trends.

## 5. How to run
1.  Install required libraries: `pip install pandas numpy matplotlib streamlit`
2.  Open the project folder and run in the terminal: `streamlit run app.py`
3.  The browser will automatically open the interactive interface. Use the on-screen buttons to select analysis functions.

## 6. Product link / Demo
- GitHub Repository: https://github.com/jiahuili2402/acc102-financial-analysis-tool
- Demo: Run `app.py` locally to launch the interactive tool, or visit the online Streamlit application link.

## 7. Limitations & next steps
- Limitations: Limited coverage of companies and industries; no real-time data update; no advanced modules such as DuPont analysis or forecasting models.
- Next steps: Expand the coverage of industries and companies; integrate data APIs for automatic updates; add DuPont analysis, chart export, and industry ranking functions.
