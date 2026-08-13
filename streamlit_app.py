import streamlit as st
import pandas as pd

st.set_page_config(page_title="PCFL Stats", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #f0f6fc; }
    h1, h2, h3, p, span, div { font-family: 'Inter', sans-serif; }
    .brand-header { background-color: #161b22; padding: 15px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 2px solid #21262d; }
    .brand-logo { background-color: #da1e28; color: white; padding: 6px 12px; font-weight: 800; border-radius: 4px; font-size: 1.1rem; }
    .no-data-box { background-color: #161b22; border: 1px dashed #30363d; border-radius: 12px; padding: 30px; text-align: center; color: #8b949e; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

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
st.caption("Preseason Layout Engine")

if 'matchups_db' not in st.session_state:
    st.session_state.matchups_db = pd.DataFrame(columns=["Home Team", "Away Team"])

if 'players_db' not in st.session_state:
    st.session_state.players_db = pd.DataFrame(columns=["Player", "Team", "Position"])

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("🏈 UPCOMING MATCHUPS")
    if st.session_state.matchups_db.empty:
        st.markdown("""
            <div class="no-data-box">
                <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 4px;">No Matchups Scheduled</p>
                <span style="font-size: 0.85rem;">Preseason schedule is currently empty.</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        for _, row in st.session_state.matchups_db.iterrows():
            st.markdown(f"""
                <div style="background-color: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; margin-bottom: 15px;">
                    <div style="font-size: 0.8rem; color: #da1e28; font-weight: 700; margin-bottom: 4px;">PRESEASON • MATCHUP</div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin: 12px 0;">
                        <span style="font-size: 1.1rem; font-weight: 600;">{row['Home Team']}</span>
                        <span style="background-color: #21262d; color: #8b949e; padding: 3px 8px; font-size: 0.8rem; font-weight: 700; border-radius: 4px;">VS</span>
                        <span style="font-size: 1.1rem; font-weight: 600;">{row['Away Team']}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

with col_right:
    st.subheader("📋 REGISTERED LEAGUE ROSTERS")
    if st.session_state.players_db.empty:
        st.markdown("""
            <div class="no-data-box">
                <p style="font-size: 1.1rem; font-weight: 600; margin-bottom: 4px;">Rosters Empty</p>
                <span style="font-size: 0.85rem;">Preseason player registrations have not started yet.</span>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown('<div style="background-color: #161b22; border-radius: 12px; overflow: hidden; border: 1px solid #30363d;">', unsafe_allow_html=True)
        st.markdown('<div style="padding: 12px 16px; background-color: #21262d; font-weight: 700; color: #8b949e;">OFFICIAL ROSTER</div>', unsafe_allow_html=True)
        for _, row in st.session_state.players_db.iterrows():
            st.markdown(f"""
                <div style="background-color: #161b22; border-bottom: 1px solid #21262d; padding: 14px 16px; display: flex; align-items: center; justify-content: space-between;">
                    <div style="flex-grow: 1;">
                        <p style="font-weight: 700; color: #ffffff; margin: 0;">{row['Player']}</p>
                        <span style="font-size: 0.85rem; color: #8b949e;">{row['Team']} • {row['Position']}</span>
                    </div>
                    <span style="color: #8b949e; font-weight: 600; font-size: 0.85rem;">PRESEASON</span>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.subheader("🛠️ LIVE PCFL COMMISSIONER PANEL")

tab1, tab2 = st.tabs(["✏️ Manage Matchups Screen", "✏️ Manage Roster Screen"])

with tab1:
    edited_matchups = st.data_editor(st.session_state.matchups_db, num_rows="dynamic", use_container_width=True, key="edit_match")
    if st.button("Save Changes & Refresh Matchups"):
        st.session_state.matchups_db = edited_matchups
        st.rerun()

with tab2:
    edited_players = st.data_editor(st.session_state.players_db, num_rows="dynamic", use_container_width=True, key="edit_play")
    if st.button("Save Changes & Refresh Rosters"):
        st.session_state.players_db = edited_players
        st.rerun()
