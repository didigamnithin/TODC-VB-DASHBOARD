# TODC - VB Dashboard

A comprehensive Streamlit dashboard for analyzing multi-platform marketing and financial data with interactive filters and visualizations. Currently supports DoorDash with UberEats and GrubHub coming soon.

## 🚀 Features

### Marketing Analysis

- **Overall Marketing Sales**: Total sales from all marketing campaigns
- **Average ROAS**: Return on Ad Spend across all campaigns
- **Marketing Orders**: Total orders driven by marketing campaigns
- **New Customers Acquired**: Number of new customers gained
- **New DP Customers**: New DoorDash Pass customers acquired
- **Average Order Value**: Overall AOV from marketing campaigns

### Financial Analysis

- **Overall Subtotal**: Total subtotal from delivered orders
- **Net Total**: Final amount after all fees and adjustments
- **Daily Performance**: Time-series analysis of financial metrics
- **Store Performance**: Top-performing stores by revenue

### Interactive Features

- **Platform Selection**: Choose between DoorDash, UberEats, and GrubHub (DoorDash active, others coming soon)
- **Two-Column Layout**: Financial Analysis and Marketing Analysis displayed side by side
- **Campaign Level Analysis**: Detailed campaign metrics when a specific store is selected
- **ROAS Highlighting**: Campaigns with ROAS < 4 are highlighted in red
- **Date Range**: Filter data by custom date ranges
- **Store Selection**: Analyze specific stores or view all
- **Self-Serve Campaigns**: Filter by campaign type (True/False)
- **Transaction Status**: Automatically filters for delivered orders only

## 📊 Data Sources

### Marketing Data

- **File**: `MARKETING_PROMOTION_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z.csv`
- **Records**: 3,546 marketing campaign records
- **Date Range**: 2025-09-22 to 2025-10-05
- **Key Metrics**: Sales, ROAS, Orders, Customer Acquisition

### Financial Data

- **File**: `FINANCIAL_DETAILED_TRANSACTIONS_2025-09-22_2025-10-05_fZY06_2025-10-07T13-11-16Z.csv`
- **Records**: 3,318 transaction records
- **Date Range**: 2025-09-22 to 2025-10-05
- **Key Metrics**: Subtotal, Net Total, Transaction Details

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Clone or download the project files**

   ```bash
   # Ensure you have the following files in your directory:
   # - doordash_dashboard.py
   # - requirements.txt
   # - data.md
   # - README.md
   # - marketing_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z/ (folder)
   # - financial_2025-09-22_2025-10-05_fZY06_2025-10-07T13-11-16Z/ (folder)
   ```
2. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the dashboard**

   ```bash
   streamlit run doordash_dashboard.py
   ```
4. **Access the dashboard**

   - The dashboard will open in yosur default web browser
   - Default URL: `http://localhost:8501`

## 📁 File Structure

```
TODC-VB-Dashboard/
├── doordash_dashboard.py          # Main Streamlit application
├── requirements.txt               # Python dependencies
├── data.md                       # Data documentation
├── README.md                     # This file
├── marketing_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z/
│   └── MARKETING_PROMOTION_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z.csv
└── financial_2025-09-22_2025-10-05_fZY06_2025-10-07T13-11-16Z/
    └── FINANCIAL_DETAILED_TRANSACTIONS_2025-09-22_2025-10-05_fZY06_2025-10-07T13-11-16Z.csv
```

## 🎨 Dashboard Features

### Visualizations

- **Line Charts**: Daily sales, ROAS, and financial metrics
- **Bar Charts**: Top-performing stores by revenue
- **Metrics Cards**: Key performance indicators with color-coded styling
- **Interactive Filters**: Real-time data filtering in sidebar

### Branding & Styling

- **TODC Branding**: Custom header with gradient styling
- **DoorDash Colors**: Orange and red color scheme (#FF6B35, #F7931E)
- **Responsive Design**: Optimized for different screen sizes
- **Professional Layout**: Clean, modern interface

### Data Processing

- **Automatic Filtering**: Financial data filtered for Order type and Delivered status
- **Date Handling**: Proper datetime conversion and filtering
- **Aggregation**: Smart grouping by date, store, and other dimensions
- **Error Handling**: Graceful handling of missing data

## 📈 Key Metrics Explained

### Marketing Metrics

- **ROAS (Return on Ad Spend)**: Sales generated per dollar spent on marketing
- **AOV (Average Order Value)**: Average value per order from marketing campaigns
- **Customer Acquisition**: New vs. existing customer breakdown
- **DP Customers**: DoorDash Pass subscribers

### Financial Metrics

- **Subtotal**: Order value before fees and adjustments
- **Net Total**: Final amount after all DoorDash fees and adjustments
- **Transaction Types**: Orders, fees, adjustments, error charges
- **Order Status**: Delivered, cancelled, picked up, etc.

## 🔧 Customization

### Adding New Metrics

1. Modify the data loading section to include new columns
2. Add new metric calculations in the dashboard
3. Update the data documentation in `data.md`

### Changing Styling

1. Modify the CSS in the `st.markdown()` section
2. Update color schemes in the `color_discrete_sequence` parameters
3. Adjust layout using Streamlit's column system

### Adding New Filters

1. Add new sidebar widgets using `st.sidebar.*`
2. Apply filters to the dataframes
3. Update the filtered data usage throughout the dashboard

## 🐛 Troubleshooting

### Common Issues

1. **File Not Found Error**

   - Ensure CSV files are in the correct directories
   - Check file names match exactly (case-sensitive)
2. **Import Errors**

   - Run `pip install -r requirements.txt`
   - Check Python version compatibility
3. **Data Loading Issues**

   - Verify CSV file format and encoding
   - Check for missing or corrupted data
4. **Performance Issues**

   - Use `@st.cache_data` for data loading
   - Consider data sampling for large datasets

## 📞 Support

For issues or questions:

1. Check the `data.md` file for data structure information
2. Review the console output for error messages
3. Ensure all dependencies are properly installed

## 🔄 Updates

To update the dashboard with new data:

1. Replace the CSV files with new data
2. Update date ranges in the dashboard if needed
3. Restart the Streamlit application

---

**TODC - DoorDash Dashboard** | Built with Streamlit | Data Analysis & Visualization Platform
