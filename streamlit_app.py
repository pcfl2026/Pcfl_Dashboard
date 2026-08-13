import streamlit as st
import pandas as pd

# 1. Navigation Panel Header States (Can be modified via Admin Panel)
if 'nav_home' not in st.session_state: st.session_state.nav_home = "HOME"
if 'nav_scores' not in st.session_state: st.session_state.nav_scores = "SCORES"
if 'nav_standings' not in st.session_state: st.session_state.nav_standings = "STANDINGS"
if 'nav_stats' not in st.session_state: st.session_state.nav_stats = "STATS"
if 'nav_teams' not in st.session_state: st.session_state.nav_teams = "TEAMS"
if 'nav_staff' not in st.session_state: st.session_state.nav_staff = "OFFICIALS & STAFF"
if 'nav_admin' not in st.session_state: st.session_state.nav_admin = "COMMISSIONER CONTROL"

# 2. Strict Application Visual Layout Styling
st.set_page_config(page_title="PCFL Hub", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0e14;
        color: #f0f6fc;
    }
    h1, h2, h3, p, span, div {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    .brand-header {
        background-color: #12161f;
        padding: 16px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 24px;
        border-bottom: 1px solid #21262d;
    }
    .brand-logo {
        background-color: #da1e28;
        color: white;
        padding: 6px 14px;
        font-weight: 800;
        border-radius: 4px;
        font-size: 1.15rem;
    }
    .score-card {
        background-color: #12161f;
        border: 1px solid #21262d;
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 16px;
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
        color: #c9d1d9;
    }
    .vs-badge {
        background-color: #1f242e;
        color: #8b949e;
        padding: 4px 10px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 4px;
    }
    .no-data-msg {
        background-color: #12161f;
        border: 1px dashed #21262d;
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        color: #8b949e;
    }
    .leader-row {
        background-color: #12161f;
        border-bottom: 1px solid #1f242e;
        padding: 14px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .rank-num { font-weight: 800; width: 24px; font-size: 1.1rem; }
    .rank-1 { color: #da1e28; }
    .rank-rest { color: #8b949e; }
    .badge-conf { background-color: #1f242e; color: #c9d1d9; font-size: 0.75rem; padding: 4px 12px; border-radius: 4px; }
    .badge-media { background-color: #da1e28; color: white; font-size: 0.75rem; padding: 4px 12px; border-radius: 4px; font-weight: 700; }
    .stat-val-text { font-weight: 800; font-size: 1.2rem; text-align: right; }
    .stat-val-1 { color: #da1e28; }
    .stat-val-rest { color: #f0f6fc; }
    </style>
    """, unsafe_allow_html=True)

# 3. Initialize True Blank Starter Databases (No Default Entries Loaded)
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

# 4. App Navigation Hub Sidebar Panel
st.sidebar.markdown("<h2 style='color:#da1e28; font-weight:800; margin-bottom:4px;'>PCFL APPS</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#8b949e; font-size:0.85rem; margin-top:0;'>Preseason Central Engine</p>", unsafe_allow_html=True)
st.sidebar.write("---")

app_section = st.sidebar.radio(
    "NAVIGATION HUB:",
    [
        st.session_state.nav_home, st.session_state.nav_scores, st.session_state.nav_standings, 
        st.session_state.nav_stats, st.session_state.nav_teams, st.session_state.nav_staff, st.session_state.nav_admin
    ]
)

# Top Bar Core Banner Component
st.markdown(f"""
    <div class="brand-header">
        <div>
            <span class="brand-logo">PCFL</span>
            <span style="margin-left: 12px; font-weight: 600; font-size: 1.2rem; color: #8b949e;">Stats & Info Suite</span>
        </div>
        <div style="color: #8b949e; font-weight: 500; font-size: 0.95rem;">2026 Preseason Suite 🔍 ☰</div>
    </div>
    """, unsafe_allow_html=True)

# --- 🏠 HOME PAGE PANEL ---
if app_section == st.session_state.nav_home:
    st.title("COLLEGE FOOTBALL")
    st.caption("Scores, standings, leaders, and awards • Powered by PCFL")
    
    col_signup, col_highlights = st.columns(2)
    with col_signup:
        st.subheader("Roster Preseason Sign Up")
        with st.form("public_signup_form", clear_on_submit=True):
            reg_name = st.text_input("Owner / Player Handle Name:")
            reg_team = st.text_input("Desired Franchise Team Shorthand Tag:")
            reg_pos = st.selectbox("Primary Assigned Position Group:", ["QB", "RB", "WR", "TE", "DE", "DT", "LB", "CB", "S"])
            reg_conf = st.selectbox("League Conference Grouping Assignment:", ["SEC", "ACC", "BIG 10", "BIG 12", "FBS Independents"])
            submit_reg = st.form_submit_button("Submit Registration Package")
            if submit_reg and reg_name and reg_team:
                new_player = {
                    "Player Name": reg_name, "Team Name": reg_team, "Position": reg_pos, "Conference": reg_conf,
                    "Passing Yds": 0, "Passing TDs": 0, "Rushing Yds": 0, "Rushing TDs": 0, 
                    "Receptions": 0, "Receiving Yds": 0, "Tackles": 0, "Sacks": 0, "Interceptions": 0
                }
                st.session_state.players_db = pd.concat([st.session_state.players_db, pd.DataFrame([new_player])], ignore_index=True)
                st.success("Registration processed successfully!")

    with col_highlights:
        st.subheader("Daily Media Highlights Feed")
        if st.session_state.highlights_db.empty:
            st.markdown('<div class="no-data-msg">No entries compiled. Updates stream here dynamically throughout the preseason.</div>', unsafe_allow_html=True)
        else:
            for _, row in st.session_state.highlights_db.iterrows():
                st.markdown(f'<div class="highlight-box"><h4>{row["Headline Info"]}</h4><p>{row["Details Narrative"]}</p></div>', unsafe_allow_html=True)

# --- 📅 SCORES PANEL ---
elif app_section == st.session_state.nav_scores:
    st.title("WEEKLY PRESEASON SCHEDULE")
    if st.session_state.matchups_db.empty:
        st.markdown('<div class="no-data-msg">No exhibition matches scheduled yet.</div>', unsafe_allow_html=True)
    else:
        for _, row in st.session_state.matchups_db.iterrows():
            st.markdown(f'<div class="score-card"><div class="score-row"><span>{row["Home Team"]}</span><b>VS</b><span>{row["Away Team"]}</span></div></div>', unsafe_allow_html=True)

# --- 🏆 STANDINGS PANEL ---
elif app_section == st.session_state.nav_standings:
    st.title("CONFERENCE STANDINGS")
    conf_tabs = st.tabs(["SEC", "ACC", "BIG 10", "BIG 12", "FBS Independents"])
    for idx, tab_name in enumerate(["SEC", "ACC", "BIG 10", "BIG 12", "FBS Independents"]):
        with conf_tabs[idx]:
            sub_df = st.session_state.players_db[st.session_state.players_db["Conference"] == tab_name]
            if sub_df.empty:
                st.markdown('<div class="no-data-msg">No franchises registered under this conference layer yet.</div>', unsafe_allow_html=True)
            else:
                st.dataframe(sub_df[["Team Name", "Player Name", "Position"]], use_container_width=True)

# --- 📊 STATS PANEL (TOP 5 LEADERBOARD GENERATOR) ---
elif app_section == st.session_state.nav_stats:
    st.title("COLLEGE FOOTBALL LEADERS")
    stat_selection = st.segmented_control("Select Stat Category View Panel:", ["Passing Yards", "Rushing Yards", "Receiving Yards", "Defensive Tackles"], default="Passing Yards")
    
    target_col, unit_label = ("Passing Yds", "YDS") if stat_selection == "Passing Yards" else ("Rushing Yds", "YDS") if stat_selection == "Rushing Yards" else ("Receiving Yds", "YDS") if stat_selection == "Receiving Yards" else ("Tackles", "TKLS")
    
    if not st.session_state.players_db.empty:
        df_sorted = st.session_state.players_db.copy()
        df_sorted[target_col] = pd.to_numeric(df_sorted[target_col], errors='coerce').fillna(0)
        top_5 = df_sorted.sort_values(by=target_col, ascending=False).head(5)
    else:
        top_5 = pd.DataFrame()

    if top_5.empty or (top_5[target_col].sum() == 0):
        st.markdown('<div class="no-data-msg">Roster dataset active. Top 5 tracking will populate here sequentially.</div>', unsafe_allow_html=True)
    else:
        for idx, (_, row) in enumerate(top_5.iterrows(), start=1):
            rank_style = "rank-1" if idx == 1 else "rank-rest"
            val_style = "stat-val-1" if idx == 1 else "stat-val-rest"
    
