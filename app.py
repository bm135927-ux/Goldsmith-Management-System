import streamlit as st
import pandas as pd
import datetime

# Page Configuration - Premium Dark/Gold Vibe
st.set_page_config(page_title="AurumPro - Goldsmith ERP & Analytics", page_icon="✨", layout="wide")

# Custom CSS for Premium Styling
st.markdown("""
    <style>
    .main-header { text-align: center; color: #D4AF37; font-family: 'Helvetica Neue', sans-serif; font-weight: 700; margin-bottom: 5px; }
    .sub-header { text-align: center; color: #888; font-size: 16px; margin-bottom: 30px; }
    .invoice-card { background-color: #1E1E1E; padding: 25px; border-radius: 15px; border: 1px solid #D4AF37; box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1); }
    .metric-box { background-color: #262626; padding: 15px; border-radius: 10px; text-align: center; border-bottom: 3px solid #D4AF37; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='main-header'>✨ AurumPro Suite</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Advanced Goldsmith Analytics, Purity Matrix & Smart Billing System</p>", unsafe_allow_html=True)

# Sidebar for Quick Conversions (Tola to Grams)
st.sidebar.markdown("<h2 style='color: #D4AF37;'>⚖️ Weight Converter</h2>", unsafe_allow_html=True)
tola_input = st.sidebar.number_input("Enter Weight in Tola", min_value=0.0, value=1.0, step=0.1)
calculated_grams = tola_input * 11.664
st.sidebar.info(f"💡 {tola_input} Tola = **{calculated_grams:.3f} Grams**")
st.sidebar.write("---")
st.sidebar.markdown("### 📅 System Logistics")
st.sidebar.write(f"**Date:** {datetime.date.today().strftime('%B %d, %Y')}")

# Layout Columns: Input Parameters vs Live Analytics
col_inputs, col_analytics = st.columns([1, 1.2], gap="large")

with col_inputs:
    st.markdown("### ⚙️ Order Specifications")
    
    customer_name = st.text_input("Client Full Name", placeholder="e.g., Awan Jewellers")
    invoice_number = st.text_input("Invoice / Order ID", value="AP-2026-001")
    
    col_w, col_r = st.columns(2)
    with col_w:
        gold_weight = st.number_input("Gold Weight (Grams)", min_value=0.01, value=11.66, step=0.1, help="Enter weight in grams directly or use sidebar converter.")
    with col_r:
        gold_rate_per_gram = st.number_input("Market Rate (PKR / Gram)", min_value=1000, value=22500, step=100)
        
    gold_purity = st.selectbox("Gold Purity (Karat Standard)", ["24K (99.9% Pure)", "22K (91.6% Pure)", "21K (87.5% Pure)", "18K (75.0% Pure)"])
    labor_charges = st.number_input("Making Charges / Labor (per Gram PKR)", min_value=0, value=1800, step=50)
    discount = st.number_input("Special Discount (PKR)", min_value=0, value=0, step=500)

# Core Actuarial & Financial Calculations
purity_multipliers = {
    "24K (99.9% Pure)": 1.0,
    "22K (91.6% Pure)": 0.916,
    "21K (87.5% Pure)": 0.875,
    "18K (75.0% Pure)": 0.750
}

multiplier = purity_multipliers[gold_purity]
pure_gold_content = gold_weight * multiplier
raw_gold_price = gold_weight * gold_rate_per_gram
total_labor = gold_weight * labor_charges
gross_total = raw_gold_price + total_labor
net_payable = gross_total - discount

with col_analytics:
    st.markdown("### 📊 Real-Time Financial Grid")
    
    # Premium Invoice Component
    st.markdown(f"""
    <div class='invoice-card'>
        <div style='display: flex; justify-content: space-between; align-items: center;'>
            <span style='color: #888; font-size: 14px;'>INVOICE: {invoice_number}</span>
            <span style='background-color: #D4AF37; color: black; padding: 2px 8px; border-radius: 5px; font-size: 12px; font-weight: bold;'>ACTIVE ORDER</span>
        </div>
        <h2 style='margin: 15px 0 5px 0; color: #FFF; font-size: 18px;'>TOTAL NET PAYABLE</h2>
        <h1 style='margin: 0; color: #D4AF37; font-size: 42px; font-weight: 700;'>Rs. {net_payable:,.2f}</h1>
        <p style='margin: 15px 0 0 0; font-size: 14px; color: #AAA;'>Client Asset Track: <b>{customer_name if customer_name else "Counter Cash Client"}</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write(" ")
    
    # 3-Way Metric Grid
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='metric-box'><span style='color: #888; font-size: 12px;'>Pure Metal Content</span><br><b style='color: #D4AF37; font-size: 18px;'>{pure_gold_content:.3f} g</b></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='metric-box'><span style='color: #888; font-size: 12px;'>Raw Gold Value</span><br><b style='color: #FFF; font-size: 18px;'>Rs. {raw_gold_price:,.0f}</b></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='metric-box'><span style='color: #888; font-size: 12px;'>Total Labor Matrix</span><br><b style='color: #FFF; font-size: 18px;'>Rs. {total_labor:,.0f}</b></div>", unsafe_allow_html=True)

st.write("---")

# Bottom Section: Advanced Forecasting & Purity Vectors
st.markdown("### 📈 Multi-Karat Valuation & Compounding Vectors")

# Generate dynamic data for the matrix table
matrix_data = {
    "Karat Grade": list(purity_multipliers.keys()),
    "Pure Gold Content (Grams)": [gold_weight * m for m in purity_multipliers.values()],
    "Raw Material Cost (PKR)": [gold_weight * gold_rate_per_gram * m for m in purity_multipliers.values()],
    "Total Project Valuation (With Labor)": [(gold_weight * gold_rate_per_gram * m) + total_labor - discount for m in purity_multipliers.values()]
}
df_matrix = pd.DataFrame(matrix_data)

# Interactive Data Frame Display
st.dataframe(
    df_matrix.style.format({
        "Pure Gold Content (Grams)": "{:.3f} g",
        "Raw Material Cost (PKR)": "Rs. {:,.2f}",
        "Total Project Valuation (With Labor)": "Rs. {:,.2f}"
    }), 
    use_container_width=True, 
    hide_index=True
)
