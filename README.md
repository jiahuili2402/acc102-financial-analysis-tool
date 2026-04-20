# acc102-financial-analysis-tool
Interactive financial analysis tool for 50 listed companies (ACC102 Track4)
## 1. Project Overview
This project is an interactive financial analysis tool designed for the ACC102 Accounting course (Track 4: Small Individual Project). It is developed with Python and Jupyter Notebook, aiming to help users analyze financial performance of 50 listed companies across 5 industries.

### Key Objectives
- Demonstrate practical Python skills in data processing and visualization
- Conduct financial analysis using real 2025 annual report data
- Build an user-friendly interface to display key financial indicators
- Generate charts to support investment decision-making and risk assessment

---

## 2. Data Source and Structure
- **Primary Data Source**:
  - China Stock Market & Accounting Research (CSMAR)
  - Official 2025 Annual Reports of A-share/H-share listed companies
- **Data Coverage**: 5 industries × 10 companies = 50 companies
- **Key Financial Metrics**:
  - Revenue and Net Profit
  - Total Assets
  - Debt Ratio
  - Return on Equity (ROE)
  - Dividend history (2020–2024)

---

## 3. Core Functionalities
The tool includes 8 professional analysis features:

1. **Stock Price Trend Simulation**
   Generate trends based on real company size and profitability.

2. **Core Financial Indicators**
   Display assets, revenue, profit, ROE, and debt ratio.

3. **Revenue & Profit Trend Analysis**
   Visualize 5-year growth trends with bar charts.

4. **Asset Structure Analysis**
   Use pie charts to show asset composition (e.g., current vs. fixed assets).

5. **Dividend History Report**
   Review annual dividend payments from 2020 to 2024.

6. **Industry Ranking & Comparison**
   Rank companies by a composite score (Profit × 0.6 + ROE × 8).

7. **Profitability & Growth Analysis**
   Calculate gross/net margins and assess growth strength.

8. **Debt & Solvency Risk Assessment**
   Analyze leverage level with risk warnings for high-debt companies.

---

## 4. How to Run
### Prerequisites
Install required Python libraries:
```bash
pip install pandas numpy matplotlib

