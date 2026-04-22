# 📊 ACC102 Financial Analysis Dashboard  

An interactive financial dashboard built with Python and Streamlit, designed to transform raw annual report data into actionable insights for investment analysis.

---

## 1. Problem & User  
Financial statements are complex and difficult to interpret quickly.  
This project helps **investors, finance students, and analysts** efficiently evaluate company performance through a clean, interactive dashboard.

---

## 2. Data  

- **Source:**  
  - Shanghai Stock Exchange (SSE)  
  - Shenzhen Stock Exchange (SZSE)  
  - Hong Kong Exchanges and Clearing (HKEX)  
- **Access Date:** March 2025  
- **Dataset:** `financial_data.csv`  

**Key Fields:**
- Company: `coname`, `stkcd`, `industry`  
- Financials: Revenue & Net Profit (2020–2024)  
- Balance Sheet: Total assets, liabilities, equity  
- Ratios: ROE, Debt ratio  
- Market Data: Stock price (2020–2024)  
- Dividends: Dividend per share  

All data comes from **official audited annual reports**, ensuring accuracy and traceability.

---

## 3. Methods  

### Tech Stack
- `pandas`, `numpy` → data processing  
- `matplotlib` → financial visualization  
- `streamlit` → interactive dashboard  

### Core Implementation
- Data cleaning and transformation from CSV  
- Financial metric calculations:
  - ROE, ROA  
  - Net Profit Margin  
  - Debt ratio & leverage classification  
- Interactive dashboard with **8 analysis modules**:
  1. Stock Price Trend  
  2. Core Financial Metrics  
  3. Revenue & Profit Trend  
  4. Asset Structure  
  5. Dividend History  
  6. Industry Ranking  
  7. Profitability Analysis  
  8. Debt & Solvency Risk  

### UI/UX Features
- Dark-mode professional financial theme  
- Custom CSS styling  
- Dynamic filtering (industry & company)  
- High-quality chart rendering  

---

## 4. Key Findings  

- High **ROE (>20%) with positive profit** indicates strong investment potential  
- Revenue growth does not guarantee profitability → margin analysis is essential  
- Debt ratio above 70% signals elevated financial risk  
- Industry ranking highlights relative competitive positioning  
- Profit margin trends reflect long-term operational stability  

---

## 5. How to Run  

### 1. Clone the repository
```bash
git clone https://github.com/jiahuili2402/acc102-financial-analysis-tool.git
cd acc102-financial-analysis-tool
2. Install dependencies
pip install -r requirements.txt
3. Run the app
streamlit run app.py
4. Open in browser
http://localhost:8501
6. Product Link

(Optional) Add your deployed Streamlit app link here

7. Limitations & Next Steps
Limitations
Dataset limited to 50 companies
No real-time data updates
Focused on China & Hong Kong markets
Next Steps
Integrate real-time financial APIs
Expand dataset coverage
Add valuation models (DCF, P/E)
Enhance interactivity and benchmarking features
📂 Project Structure
acc102-financial-analysis-tool/
│
├── app.py
├── financial_data.csv
├── requirements.txt
└── README.md
