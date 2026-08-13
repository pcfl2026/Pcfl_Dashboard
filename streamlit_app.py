import streamlit as st
import pandas as pd

# 1. Initialize Dynamic Navigation Labels in State
if 'nav_home' not in st.session_state: st.session_state.nav_home = "HOME"
if 'nav_scores' not in st.session_state: st.session_state.nav_scores = "SCORES"
if 'nav_standings' not in st.session_state: st.session_state.nav_standings = "STANDINGS"
if 'nav_stats' not in st.session_state: st.session_state.nav_stats = "STATS"
if 'nav_teams' not in st.session_state: st.session_state.nav_teams = "TEAMS"
if 'nav_staff' not in st.session_state: st.session_state.nav_staff = "OFFICIALS & STAFF"
if 'nav_admin' not in st.session_state: st.session_state.nav_admin = "COMMISSIONER CONTROL"

# 2. Page Configuration & Premium Application UI Styling Overrides
st.set_page_config(page_title="PCFL Executive Hub", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    /* Dark Theme Grid Layout Engine */
    .stApp {
        background-color: #0b0e14;
        color: #f0f6fc;
    }
    h1, h2, h3, p, span, div {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    
    /* Premium Application Navigation Top Header Bar */
    .brand-header {
        background-color: #12161f;
        padding: 16px 20px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
        border: 1px solid #21262d;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
    .brand-logo {
        background: linear-gradient(135deg, #da1e28 0%, #a2131a 100%);
        color: white;
        padding: 6px 14px;
        font-weight: 800;
        border-radius: 6px;
        font-size: 1.15rem;
        letter-spacing: 0.5px;
    }
    
    /* Structured Card Layouts */
    .app-section-box {
        background-color: #12161f;
        border: 1px solid #21262d;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    .score-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 12px;
    }
    .score-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 10px 0;
    }
    .score-team {
        font-size: 1.05rem;
        font-weight: 600;
        color: #c9d1d9;
    }
    .vs-badge {
        background-color: #21262d;
        color: #8b949e;
        padding: 4px 10px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 4px;
    }
    .no-data-msg {
        background-color: #161b22;
        border: 1px dashed #30363d;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        color: #8b949e;
        font-size: 0.95rem;
    }
    
    /* Metrics Directory Rows Layout styling */
    .leader-row {
        background-color: #161b22;
        border-bottom: 1px solid #21262d;
        padding: 14px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .rank-num {
        font-weight: 800;
        width: 24px;
        font-size: 1.1rem;
    }
    .rank-1 { color: #da1e28; }
    .rank-rest { color: #8b949e; }
    
    /* Custom Badges */
    .badge-conf {
        background-color: #21262d;
        color: #c9d1d9;
        font-size: 0.75rem;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 600;
    }
    .badge-media {
        background-color: #da1e28;
        color: white;
        font-size: 0.75rem;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 700;
        text-transform: uppercase;
    }
    .highlight-box {
        background-color: #161b22;
        border-left: 4px solid #da1e28;
        border-radius: 6px;
        padding: 16px;
        margin-bottom: 12px;
        border-top: 1px solid #30363d;
        border-right: 1px solid #30363d;
        border-bottom: 1px solid #30363d;
    }
    
    /* App Menu Native Categories List styling */
    .menu-item-container {
        display: flex;
        align-items: center;
        padding: 8px 0;
    }
    .menu-icon {
        font-size: 1.25rem;
        margin-right: 12px;
        display: inline-block;
        width: 24px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize True Empty Databases (Absolutely No Sample Teams/Players Loaded)
if 'players_db' not in st.session_state:
    st.session_state.players_db = pd.DataFrame(columns=[
        "Player Name", "Team Name", "Position", "Conference", 
        "Passing Yds", "Passing TDs", "Rushing Yds", "Rushing TDs", 
        "Receptions", "Receiving Yds", "Tackles", "Sacks", "Interceptions"
    ])

if 'matchups_db' not in st.session_state:
    st.session_state.matchups_db = pd.DataFrame(columns=["Home Team", "Away Team", "Week Track", "Time/Status"])

if 'streamers_db' not in st.session_state:
    st.session_state.streamers_db = pd.DataFrame(columns=["Channel/Host Name", "Media Outlet", "Broadcast Coverage Details"])

if 'referees_db' not in st.session_state:
    st.session_state.referees_db = pd.DataFrame(columns=["Official Name", "Assigned Crew Lineup"])

if 'ads_db' not in st.session_state:
    st.session_state.ads_db = pd.DataFrame(columns=["Director Name", "Assigned Member School"])

if 'highlights_db' not in st.session_state:
    st.session_state.highlights_db = pd.DataFrame(columns=["Headline Info", "Details Narrative", "Date String"])

# 4. App Sidebar Directory Panel Engine with Custom Icon Mapping Font Layouts
st.sidebar.markdown("<h2 style='color:#da1e28; font-weight:800; margin-bottom:4px;'>PCFL EXECUTIVE</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#8b949e; font-size:0.85rem; margin-top:0;'>Preseason Central Suite</p>", unsafe_allow_html=True)
st.sidebar.write("---")

# Format Selection Map Keys to enforce visual icon rendering layout blocks
opt_home = f"🏠 {st.session_state.nav_home}"
opt_scores = f"📅 {st.session_state.nav_scores}"
opt_standings = f"🏆 {st.session_state.nav_standings}"
opt_stats = f"📊 {st.session_state.nav_stats}"
opt_teams = f"🛡️ {st.session_state.nav_teams}"
opt_staff = f"👥 {st.session_state.nav_staff}"
opt_admin = f"🛠️ {st.session_state.nav_admin}"

selected_menu_label = st.sidebar.radio(
    "NAVIGATION HUB DIRECTORY:",
    [opt_home, opt_scores, opt_standings, opt_stats, opt_teams, opt_staff, opt_admin]
)

# 5. Top App Header Navigation Bar Rendering - Enforces Complete PCFL Identity
st.markdown(f"""
    <div class="brand-header">
        <div>
            <span class="brand-logo">PCFL</span>
            <span style="margin-left: 12px; font-weight: 600; font-size: 1.2rem; color: #8b949e;">Core Portal</span>
        </div>
        <div style="color: #8b949e; font-weight: 500; font-size: 0.95rem;">2026 Preseason Operations 🔍 ☰</div>
    </div>
    """, unsafe_allow_html=True)


# --- 🏠 COMPONENT 1: HOME PAGE ---
if selected_menu_label == opt_home:
    st.title("COLLEGE FOOTBALL")
    st.caption("Scores, standings, leaders, and awards • Powered by PCFL")
    
    col_signup, col_highlights = st.columns(2)
    
    with col_signup:
        st.markdown('<div class="app-section-box">', unsafe_allow_html=True)
        st.subheader("Roster Preseason Sign Up")
        with st.form("public_signup_form", clear_on_submit=True):
            reg_name = st.text_input("Owner / Player Handle Name:")
            reg_team = st.text_input("Desired Franchise Team Shorthand Tag:")
            reg_pos = st.selectbox("Primary Assigned Position Group:", ["QB", "RB", "WR", "TE", "DE", "DT", "LB", "CB", "S"])
            reg_conf = st.selectbox("League Conference Grouping Assignment:", ["SEC", "ACC", "BIG 10", "BIG 12", "FBS Independents"])
            
            submit_reg = st.form_submit_button("Submit Registration Package")
            if submit_reg:
                if reg_name and reg_team:
                    new_player = {
                        "Player Name": reg_name, "Team Name": reg_team, "Position": reg_pos, "Conference": reg_conf,
                        "Passing Yds": 0, "Passing TDs": 0, "Rushing Yds": 0, "Rushing TDs": 0, 
                        "Receptions": 0, "Receiving Yds": 0, "Tackles": 0, "Sacks": 0, "Interceptions": 0
                    }
                    st.session_state.players_db = pd.concat([st.session_state.players_db, pd.DataFrame([new_player])], ignore_index=True)
                    st.success(f"Registration processed for {reg_name}!")
                else:
                    st.error("Fields cannot run empty.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_highlights:
        st.markdown('<div class="app-section-box">', unsafe_allow_html=True)
        st.subheader("Daily Media Highlights Feed")
        if st.session_state.highlights_db.empty:
            st.markdown('<div class="no-data-msg">No entries compiled. Updates stream here dynamically throughout the preseason schedule.</div>', unsafe_allow_html=True)
        else:
            for _, row in st.session_state.highlights_db.iterrows():
                st.markdown(f"""
                    <div class="highlight-box">
                        <span style="font-size:0.75rem; color:#da1e28; font-weight:700;">{row['Date String']} • BULLETIN</span>
                        <h4 style="margin:4px 0; color:#fff;">{row['Headline Info']}</h4>
                        <p style="margin:0; color:#8b949e; font-size:0.9rem;">{row['Details Narrative']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)


# --- 📅 COMPONENT 2: SCORES ---
elif selected_menu_label == opt_scores:
    st.title("WEEKLY PRESEASON SCHEDULE")
    st.caption("Live matchups status trackers")
    
    st.markdown('<div class="app-section-box">', unsafe_allow_html=True)
    
