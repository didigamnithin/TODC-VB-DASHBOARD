import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import numpy as np

# Page configuration
st.set_page_config(
    page_title="TODC - VB Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for branding
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B35 0%, #F7931E 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    .main-header h1 {
        margin: 0;
        font-size: 3rem;
        font-weight: bold;
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.2rem;
        opacity: 0.9;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #FF6B35;
        margin-bottom: 1rem;
    }
    .section-header {
        color: #FF6B35;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #FF6B35;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    .roas-low {
        color: #dc3545;
        font-weight: bold;
    }
    .roas-good {
        color: #28a745;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_data():
    """Load and cache the marketing and financial data"""
    try:
        # Load marketing data
        marketing_df = pd.read_csv('marketing_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z/MARKETING_PROMOTION_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z.csv')
        marketing_df['Date'] = pd.to_datetime(marketing_df['Date'])
        
        # Load financial data
        financial_df = pd.read_csv('financial_2025-09-30_2025-10-06_VR2th_2025-10-07T11-19-19Z/FINANCIAL_DETAILED_TRANSACTIONS_2025-09-30_2025-10-06_VR2th_2025-10-07T11-19-19Z.csv')
        financial_df['Timestamp local date'] = pd.to_datetime(financial_df['Timestamp local date'])
        
        return marketing_df, financial_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

# Main header
st.markdown("""
<div class="main-header">
    <h1>🚀 TODC - VB Dashboard</h1>
    <p>Comprehensive Analytics for Marketing Performance & Financial Insights</p>
</div>
""", unsafe_allow_html=True)

# Platform selection buttons
st.markdown("### Select Platform")
col1, col2, col3 = st.columns(3)

with col1:
    doordash_btn = st.button("🚀 DoorDash", key="doordash", type="primary")
with col2:
    ubereats_btn = st.button("🍔 UberEats", key="ubereats", disabled=True)
with col3:
    grubhub_btn = st.button("🍕 GrubHub", key="grubhub", disabled=True)

# Show coming soon message for other platforms
if ubereats_btn or grubhub_btn:
    st.info("🚧 Coming Soon! This platform analysis will be available in future updates.")

# Only show DoorDash analysis for now
if not doordash_btn and not ubereats_btn and not grubhub_btn:
    doordash_btn = True  # Default to DoorDash

# Load data
marketing_df, financial_df = load_data()

if marketing_df is not None and financial_df is not None:
    
    # Sidebar filters
    st.sidebar.markdown("## 🎛️ Dashboard Controls")
    
    # Marketing filters
    st.sidebar.markdown("### 📊 Marketing Analysis Filters")
    
    # Date range for marketing
    marketing_date_min = marketing_df['Date'].min().date()
    marketing_date_max = marketing_df['Date'].max().date()
    marketing_date_range = st.sidebar.date_input(
        "Marketing Date Range",
        value=(marketing_date_min, marketing_date_max),
        min_value=marketing_date_min,
        max_value=marketing_date_max
    )
    
    # Self-serve filter
    self_serve_options = ['All', 'True', 'False']
    selected_self_serve = st.sidebar.selectbox("Self-Serve Campaign", self_serve_options)
    
    # Store filter for marketing
    marketing_stores = ['All'] + sorted(marketing_df['Store name'].unique().tolist())
    selected_marketing_store = st.sidebar.selectbox("Select Store (Marketing)", marketing_stores)
    
    # Financial filters
    st.sidebar.markdown("### 💰 Financial Analysis Filters")
    
    # Date range for financial
    financial_date_min = financial_df['Timestamp local date'].min().date()
    financial_date_max = financial_df['Timestamp local date'].max().date()
    financial_date_range = st.sidebar.date_input(
        "Financial Date Range",
        value=(financial_date_min, financial_date_max),
        min_value=financial_date_min,
        max_value=financial_date_max
    )
    
    # Store filter for financial
    financial_stores = ['All'] + sorted(financial_df['Store name'].unique().tolist())
    selected_financial_store = st.sidebar.selectbox("Select Store (Financial)", financial_stores)
    
    # Apply filters to marketing data
    marketing_filtered = marketing_df.copy()
    
    if len(marketing_date_range) == 2:
        marketing_filtered = marketing_filtered[
            (marketing_filtered['Date'].dt.date >= marketing_date_range[0]) &
            (marketing_filtered['Date'].dt.date <= marketing_date_range[1])
        ]
    
    if selected_self_serve != 'All':
        self_serve_bool = selected_self_serve == 'True'
        marketing_filtered = marketing_filtered[marketing_filtered['Is self serve campaign'] == self_serve_bool]
    
    if selected_marketing_store != 'All':
        marketing_filtered = marketing_filtered[marketing_filtered['Store name'] == selected_marketing_store]
    
    # Apply filters to financial data
    financial_filtered = financial_df.copy()
    
    # Apply transaction type and status filters
    financial_filtered = financial_filtered[
        (financial_filtered['Transaction type'] == 'Order') &
        (financial_filtered['Final order status'] == 'Delivered')
    ]
    
    if len(financial_date_range) == 2:
        financial_filtered = financial_filtered[
            (financial_filtered['Timestamp local date'].dt.date >= financial_date_range[0]) &
            (financial_filtered['Timestamp local date'].dt.date <= financial_date_range[1])
        ]
    
    if selected_financial_store != 'All':
        financial_filtered = financial_filtered[financial_filtered['Store name'] == selected_financial_store]
    
    # Two column layout
    col1, col2 = st.columns(2)
    
    # Financial Analysis Column
    with col1:
        st.markdown('<div class="section-header">💰 Financial Analysis</div>', unsafe_allow_html=True)
        
        # Financial metrics
        overall_subtotal = financial_filtered['Subtotal'].sum()
        net_total = financial_filtered['Net total'].sum()
        
        st.metric(
            label="💵 Overall Subtotal",
            value=f"${overall_subtotal:,.2f}",
            delta=None
        )
        
        st.metric(
            label="💰 Net Total",
            value=f"${net_total:,.2f}",
            delta=None
        )
        
        # Store performance for financial
        if selected_financial_store == 'All':
            financial_store_performance = financial_filtered.groupby('Store name').agg({
                'Subtotal': 'sum',
                'Net total': 'sum'
            }).reset_index()
            financial_store_performance = financial_store_performance.sort_values('Subtotal', ascending=False).head(10)
            
            fig_financial_stores = px.bar(financial_store_performance, x='Store name', y='Subtotal',
                                         title='Top 10 Stores by Subtotal',
                                         color='Subtotal',
                                         color_continuous_scale='Oranges')
            fig_financial_stores.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig_financial_stores, use_container_width=True)
    
    # Marketing Analysis Column
    with col2:
        st.markdown('<div class="section-header">📊 Marketing Analysis</div>', unsafe_allow_html=True)
        
        # Marketing metrics
        marketing_sales = marketing_filtered['Sales'].sum()
        avg_roas = marketing_filtered['ROAS'].mean() if len(marketing_filtered) > 0 else 0
        marketing_orders = marketing_filtered['Orders'].sum()
        new_customers = marketing_filtered['New customers acquired'].sum()
        new_dp_customers = marketing_filtered['New DP customers acquired'].sum()
        avg_order_value = marketing_filtered['Average order value'].mean() if len(marketing_filtered) > 0 else 0
        
        st.metric(
            label="💰 Marketing Sales",
            value=f"${marketing_sales:,.2f}",
            delta=None
        )
        
        st.metric(
            label="📈 Average ROAS",
            value=f"{avg_roas:.2f}x",
            delta=None
        )
        
        st.metric(
            label="📦 Marketing Orders",
            value=f"{marketing_orders:,}",
            delta=None
        )
        
        st.metric(
            label="👥 New Customers",
            value=f"{new_customers:,}",
            delta=None
        )
        
        st.metric(
            label="⭐ New DP Customers",
            value=f"{new_dp_customers:,}",
            delta=None
        )
        
        st.metric(
            label="💵 Average Order Value",
            value=f"${avg_order_value:.2f}",
            delta=None
        )
        
        # Store performance for marketing
        if selected_marketing_store == 'All':
            marketing_store_performance = marketing_filtered.groupby('Store name').agg({
                'Sales': 'sum',
                'Orders': 'sum',
                'ROAS': 'mean',
                'New customers acquired': 'sum'
            }).reset_index()
            marketing_store_performance = marketing_store_performance.sort_values('Sales', ascending=False).head(10)
            
            fig_marketing_stores = px.bar(marketing_store_performance, x='Store name', y='Sales',
                                         title='Top 10 Stores by Marketing Sales',
                                         color='Sales',
                                         color_continuous_scale='Oranges')
            fig_marketing_stores.update_layout(xaxis_tickangle=-45, height=400)
            st.plotly_chart(fig_marketing_stores, use_container_width=True)
    
    # Campaign Level Analysis (only show when a specific store is selected)
    if selected_marketing_store != 'All':
        st.markdown('<div class="section-header">📋 Campaign Level Analysis - ' + selected_marketing_store + '</div>', unsafe_allow_html=True)
        
        # Get campaign data for selected store
        store_campaigns = marketing_filtered[marketing_filtered['Store name'] == selected_marketing_store].copy()
        
        if len(store_campaigns) > 0:
            # Prepare campaign data for display
            campaign_data = store_campaigns[['Campaign name', 'Type of promotion', 'Date', 'Orders', 'Sales', 'ROAS', 
                                           'New customers acquired', 'New DP customers acquired', 'Average order value']].copy()
            
            # Sort by date
            campaign_data = campaign_data.sort_values('Date', ascending=False)
            
            # Format the data for display
            campaign_display = campaign_data.copy()
            campaign_display['Date'] = campaign_display['Date'].dt.strftime('%Y-%m-%d')
            campaign_display['Sales'] = campaign_display['Sales'].apply(lambda x: f"${x:,.2f}")
            campaign_display['Average order value'] = campaign_display['Average order value'].apply(lambda x: f"${x:,.2f}")
            
            # Create a styled dataframe with ROAS highlighting
            def highlight_roas(val):
                if isinstance(val, (int, float)) and val < 4:
                    return 'background-color: #ffebee; color: #c62828; font-weight: bold'
                return ''
            
            # Display the table
            st.dataframe(
                campaign_display.style.applymap(highlight_roas, subset=['ROAS']),
                use_container_width=True,
                height=400
            )
            
            # Summary metrics for the selected store
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric(
                    label="Total Campaigns",
                    value=f"{len(store_campaigns)}",
                    delta=None
                )
            
            with col2:
                store_total_sales = store_campaigns['Sales'].sum()
                st.metric(
                    label="Store Total Sales",
                    value=f"${store_total_sales:,.2f}",
                    delta=None
                )
            
            with col3:
                store_avg_roas = store_campaigns['ROAS'].mean()
                st.metric(
                    label="Store Average ROAS",
                    value=f"{store_avg_roas:.2f}x",
                    delta=None
                )
            
            with col4:
                store_total_orders = store_campaigns['Orders'].sum()
                st.metric(
                    label="Store Total Orders",
                    value=f"{store_total_orders:,}",
                    delta=None
                )
        else:
            st.info(f"No campaign data found for {selected_marketing_store} in the selected date range.")
    
    # Data summary
    st.markdown('<div class="section-header">📋 Data Summary</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Marketing Data Summary:**")
        if len(marketing_filtered) > 0:
            st.write(f"- Total Records: {len(marketing_filtered):,}")
            st.write(f"- Date Range: {marketing_filtered['Date'].min().strftime('%Y-%m-%d')} to {marketing_filtered['Date'].max().strftime('%Y-%m-%d')}")
            st.write(f"- Unique Stores: {marketing_filtered['Store name'].nunique()}")
            st.write(f"- Campaign Types: {marketing_filtered['Type of promotion'].nunique()}")
        else:
            st.write("- No data available for selected filters")
    
    with col2:
        st.markdown("**Financial Data Summary:**")
        if len(financial_filtered) > 0:
            st.write(f"- Total Records: {len(financial_filtered):,}")
            st.write(f"- Date Range: {financial_filtered['Timestamp local date'].min().strftime('%Y-%m-%d')} to {financial_filtered['Timestamp local date'].max().strftime('%Y-%m-%d')}")
            st.write(f"- Unique Stores: {financial_filtered['Store name'].nunique()}")
            st.write(f"- Total Subtotal: ${financial_filtered['Subtotal'].sum():,.2f}")
        else:
            st.write("- No data available for selected filters")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p><strong>TODC - VB Dashboard</strong> | Powered by Streamlit</p>
        <p>Data Analysis & Visualization Platform</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("❌ Unable to load data. Please check that the CSV files are in the correct location.")
    st.info("""
    **Required files:**
    - `marketing_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z/MARKETING_PROMOTION_2025-09-22_2025-10-05_IeW4u_2025-10-07T11-22-22Z.csv`
    - `financial_2025-09-30_2025-10-06_VR2th_2025-10-07T11-19-19Z/FINANCIAL_DETAILED_TRANSACTIONS_2025-09-30_2025-10-06_VR2th_2025-10-07T11-19-19Z.csv`
    """)
