import streamlit as st
import datetime
import pytz
import json
import hashlib

# --- HARDENING FIX: The Constitution is now directly in the main file to avoid import errors ---
DAO_CONSTITUTION = {
    "name": "The Global Payment Network",
    "token_ticker": "AXM",
    "total_supply": 250_000_000_000.0,
    "treasury_allocation": 35_000_000_000.0,
    "investment_fund_allocation": 10_000_000_000.0,
    "legal_defense_fund_allocation": 5_000_000_000.0,
    "transaction_fee": 0.01,
    "proposal_fee": 100.0
}

# --- Initialize Application ---
st.set_page_config(page_title="The Global Payment Network", layout="wide")
st.title("🌐 The Global Payment Network")

# --- Context-Aware Configuration ---
TIMEZONE = pytz.timezone("Asia/Baghdad")
current_time = datetime.datetime.now(TIMEZONE)
st.caption(f"**Operational Context:** Baghdad, Iraq | **Time:** {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# --- Initialize Core Services ---
if 'dao_constitution' not in st.session_state:
    st.session_state.dao_constitution = DAO_CONSTITUTION

# --- UI Tabs & Application Logic ---
tab1, tab2 = st.tabs(["🏛️ Governance Dashboard", "👥 Network Participants (Conceptual)"])

with tab1:
    st.header("DAO Constitution & Treasury")
    st.info("The network is governed by its participants according to the rules of its immutable constitution.")

    col1, col2, col3 = st.columns(3)
    col1.metric("DAO Treasury (AXM)", f"{st.session_state.dao_constitution['treasury_allocation']:,.0f}")
    col2.metric("Investment Fund (AXM)", f"{st.session_state.dao_constitution['investment_fund_allocation']:,.0f}")
    col3.metric("Legal Defense Fund (AXM)",
                f"{st.session_state.dao_constitution['legal_defense_fund_allocation']:,.0f}")

    with st.expander("View Full Constitution"):
        st.json(st.session_state.dao_constitution)

with tab2:
    st.header("Agent Roster")
    st.write("- The Founder")
    st.write("- Central Bank of Iraq")
    st.write("- Basra Oil Company")