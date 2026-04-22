````markdown
# Financial Analysis Dashboard

## 1. Problem & User
This project provides an interactive financial dashboard designed to visualize and analyze the financial data of publicly listed companies, including revenue, net profit, stock price trends, and other key metrics. It is ideal for investors, analysts, and finance professionals who need a comprehensive, user-friendly interface to analyze a company’s financial health and performance over multiple years.

## 2. Data
- **Source**: Official Annual Reports of companies listed on the Shanghai Stock Exchange (SSE), Shenzhen Stock Exchange (SZSE), and Hong Kong Exchanges and Clearing (HKEX).
- **Access Date**: Data is extracted from audited reports for the fiscal years 2020-2024.
- **Key Fields**:
  - Company Name (`coname`)
  - Industry (`industry`)
  - Stock Code (`stkcd`)
  - Total Assets (`total_assets`)
  - Revenue (`rev_2024`, `rev_2020` to `rev_2024`)
  - Net Profit (`profit_2024`, `profit_2020` to `profit_2024`)
  - ROE (`roe`)
  - Dividend History (`div`)
  - Debt Ratio (`debt_ratio`)
  - Stock Prices (`price_2020` to `price_2024`)

## 3. Methods
The dashboard leverages the following steps to visualize the financial data:
- **Data Preprocessing**: Load and process financial data from CSV files.
- **Visualization**: 
  - Line charts for stock price trends, revenue & profit trends, and profitability analysis.
  - Bar charts for revenue and net profit trends.
  - Pie charts for asset structure and debt & solvency risk.
- **Financial Metrics**: Display key financial ratios like ROE, debt-to-equity ratio, profit margin, etc.
- **Interactive Widgets**: Allow users to select industries and companies for a tailored financial analysis.

## 4. Key Findings
- **Interactive Dashboards**: Users can select any industry and company to explore key financial metrics, such as total assets, revenue, and net profit.
- **Trend Analysis**: Provides a visual representation of key metrics over the fiscal years (2020-2024) to help track company performance.
- **Profitability Insights**: Net profit margin and return on equity (ROE) are calculated to help assess financial health.
- **Risk Assessment**: Debt ratio and leverage levels are visualized to gauge a company's solvency and financial risk.
- **Dividend History**: A clear display of dividends per share for each fiscal year.

## 5. How to Run
To run this project locally:
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/financial-analysis-dashboard.git
````

2. Install the necessary Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Download the financial data CSV file (`financial_data.csv`) and place it in the root directory of the project.
4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

The app will launch in your browser, and you can start exploring the financial data and analysis.

## 6. Product Link

You can access the live version of the dashboard [here](#). (Replace with your actual product link if applicable.)

## 7. Limitations & Next Steps

* **Limitations**:

  * The data is limited to companies listed on SSE, SZSE, and HKEX, so global coverage is not available.
  * The app relies on the `financial_data.csv` file for data, which needs to be kept up to date for accurate analysis.
* **Next Steps**:

  * Expand the dataset to include companies from other stock exchanges.
  * Integrate additional financial metrics such as cash flow, working capital, and earnings before interest and taxes (EBIT).
  * Implement more advanced predictive analysis features using machine learning.
  * Enhance the user interface with more visualizations and tools for in-depth analysis.
