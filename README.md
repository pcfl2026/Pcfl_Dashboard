import streamlit as st
import pandas as pd

# 1. Page Configuration & Custom CSS Injection for Dark Theme
st.set_page_config(page_title="PCFL Stats", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
    }
    h1, h2, h3, p, span, div {
        font-family: 'Inter', sans-serif;
    }
    
    /* Top PCFL Branded Header Bar */
    .brand-header {
        background-color: #161b22;
        padding: 15px;
        border-radius: 8px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        border-bottom: 2px solid #21262d;
    }
    .brand-logo {
        background-color: #da1e28;
        color: white;
        padding: 6px 12px;
        font-weight: 800;
        border-radius: 4px;
        font-size: 1.1rem;
    }
    
    /* Preseason Matchup Cards (Completely Clean - No Times/Scores/Stats) */
    .score-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }
    .score-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 12px 0;
    }
    .score-team {
        font-size: 1.1rem;
        font-weight: 600;
    }
    .vs-badge {
        background-color: #21262d;
        color: #8b949e;
        padding: 3px 8px;
        font-size: 0.8rem;
        font-weight: 700;
        border-radius: 4px;
    }
    
    /* Clean Roster Layout List */
    .leader-row {
        background-color: #161b22;
        border-bottom: 1px solid #21262d;
        padding: 14px 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .player-info {
        flex-grow: 1;
    }
    .player-name {
        font-weight: 700;
        color: #ffffff;
        margin: 0;
    }
    .player-meta {
        font-size: 0.85rem;
        color: #8b949e;
    }
    .preseason-status {
        color: #8b949e;
        font-weight: 600;
        font-size: 0.85rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. PCFL Top Navigation Banner
st.markdown("""
    <div class="brand-header">
        <div>
            <span class="brand-logo">PCFL</span>
            <span style="margin-left: 10px; font-weight: 600; font-size: 1.2rem; color: #8b949e;">Preseason</span>
        </div>
        <div style="color: #8b949e; font-weight: 500;">2026 Registration 🔍 ☰</div>
    </div>
    """, unsafe_allow_html=True)

st.title("PCFL FOOTBALL")
st.caption("Preseason Team Rosters and Scheduled Matchups")

# 3. Session State Databases for Preseason (No stats or metrics columns)
if 'matchups_db' not in st.session_state:
    st.session_state.matchups_db = pd.DataFrame([
        {"Home Team": "🌵 Arizona State", "Away Team": "🐯 Missouri Tigers"},
        {"Home Team": "🐻 California Golden Bears", "Away Team": "🛡️ Rutgers Scarlet Knights"}
    ])

if 'players_db' not in st.session_state:
    st.session_state.players_db = pd.DataFrame([
        {"Player": "Hellraiser000", "Team": "BUF", "Position": "QB"},
        {"Player": "BTN_Demonte", "Team": "IOWA", "Position": "QB"},
        {"Player": "drago376", "Team": "STAN", "Position": "QB/CB"},
        {"Player": "tevinveil", "Team": "SMU", "Position": "QB"},
        {"Player": "Chcjenc", "Team": "GSE", "Position": "QB"}
    ])

# 4. Display Preseason Dashboard Layout
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🏈 UPCOMING MATCHUPS")
    for _, row in st.session_state.matchups_db.iterrows():
        st.markdown(f"""
            <div class="score-card">
                <div style="font-size: 0.8rem; color: #da1e28; font-weight: 700; margin-bottom: 4px;">PRESEASON • MATCHUP</div>
                <div class="score-row">
                    <span class="score-team">{row['Home Team']}</span>
                    <span class="vs-badge">VS</span>
                    <span class="score-team">{row['Away Team']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

with col_right:
    st.subheader("📋 REGISTERED LEAGUE ROSTERS")
    st.markdown('<div style="background-color: #161b22; border-radius: 12px; overflow: hidden; border: 1px solid #30363d;">', unsafe_allow_html=True)
    st.markdown('<div style="padding: 12px 16px; background-color: #21262d; font-weight: 700; color: #8b949e;">OFFICIAL ROSTER</div>', unsafe_allow_html=True)
    
    for _, row in st.session_state.players_db.iterrows():
        st.markdown(f"""
            <div class="leader-row">
                <div class="player-info">
                    <p class="player-name">{row['Player']}</p>
                    <span class="player-meta">{row['Team']} • {row['Position']}</span>
                </div>
                <span class="preseason-status">PRESEASON</span>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. Live Management Engine (Editable Panel)
st.markdown("---")
st.subheader("🛠️ LIVE PCFL COMMISSIONER PANEL")
st.caption("Double-click cells below to change team formats, edit rosters, or insert new matchups over time.")

tab1, tab2 = st.tabs(["✏️ Manage Matchups Screen", "✏️ Manage Roster Screen"])

with tab1:
    edited_matchups = st.st.data_editor(st.session_state.matchups_db, num_rows="dynamic", use_container_width=True, key="edit_match")
    if st.button("Save Changes & Refresh Matchups"):
        st.session_state.matchups_db = edited_matchups
        st.rerun()

with tab2:
    edited_players = st.st.data_editor(st.session_state.players_db, num_rows="dynamic", use_container_width=True, key="edit_play")
    if st.button("Save Changes & Refresh Rosters"):
        st.session_state.players_db = edited_players
        st.rerun()
        
