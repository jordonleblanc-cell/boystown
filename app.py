import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Boys Town PEM Learning Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- SESSION STATE INITIALIZATION ---
if 'point_log' not in st.session_state:
    st.session_state.point_log = pd.DataFrame(columns=[
        "Time", "Skill", "Type", "Behavior", "Points"
    ])

if 'total_points' not in st.session_state:
    st.session_state.total_points = 0

# --- STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .status-box {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 PEM Curriculum")
selection = st.sidebar.radio(
    "Go to Module:",
    [
        "Dashboard",
        "1. Foundations & Hallmarks",
        "2. The ABCs of Behavior",
        "3. Teaching Interactions",
        "4. Motivation System Lab",
        "5. Professionalism & Boundaries"
    ]
)

# --- MODULE 0: DASHBOARD ---
if selection == "Dashboard":
    st.title("🚀 PEM Staff Training Dashboard")
    st.write(f"Welcome to the interactive portal for the **Psychoeducational Treatment Model (PEM)**.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Balance", f"{st.session_state.total_points} pts")
    with col2:
        level = "Level I"
        if st.session_state.total_points >= 50000: level = "Level II"
        if st.session_state.total_points >= 75000: level = "Level III"
        st.metric("Current Level", level)
    with col3:
        status = "Active" if st.session_state.total_points >= 0 else "Privileges Suspended"
        st.metric("Status (Zero Rule)", status)

    st.subheader("Level Advancement Progress")
    progress_val = min(st.session_state.total_points / 50000.0, 1.0)
    st.progress(progress_val)
    st.caption(f"{int(progress_val*100)}% towards Level II criteria (50,000 pts)")

    st.info("""
    **Core Principles Recap:**
    * Behavior is learned.
    * Insight is helpful but not sufficient.
    * Rewards and punishers are individualized.
    """)

# --- MODULE 1: FOUNDATIONS ---
elif selection == "1. Foundations & Hallmarks":
    st.title("🏛️ PEM Foundations")
    
    tab1, tab2 = st.tabs(["The Bio-Psycho-Social Approach", "The Hallmarks"])
    
    with tab1:
        st.subheader("Interdisciplinary Treatment")
        st.write("""
        PEM is based on the **Bio-Psycho-Social** approach, addressing needs simultaneously:
        * **Biological:** Medical needs and physiological influences.
        * **Psychological:** Individual, family, and group therapy.
        * **Social:** Social skills, modeling, and teaching interactions.
        """)
        st.image("https://img.icons8.com/color/96/000000/mind-map.png", width=100)
    
    with tab2:
        st.subheader("Philosophical Hallmarks")
        hallmarks = {
            "Safety, Permanency, Well-being": "Children must feel safe before goals can be met.",
            "Family Engagement": "Parents are experts of their own family.",
            "Primary Change Agents": "Staff who spend the most time with youth (60%) are the primary teachers.",
            "Behavioral Orientation": "Positive, measurable impact based on actual change.",
            "Individualized Skill Acquisition": "Methods adapted to the learner's characteristics."
        }
        for h, d in hallmarks.items():
            st.markdown(f"**{h}:** {d}")

# --- MODULE 2: ABC ANALYZER ---
elif selection == "2. The ABCs of Behavior":
    st.title("🔍 The ABC Analyzer")
    st.write("Behavior does not occur in a vacuum. Analyze the pattern below.")
    
    with st.expander("Definitions"):
        st.markdown("""
        - **A (Antecedent):** Internal or external events present *before* behavior.
        - **B (Behavior):** Anything a person says/does that is observable and measurable.
        - **C (Consequence):** Events that occur *after* behavior.
        """)

    st.divider()
    st.subheader("Practice Scenario Creator")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        a_input = st.selectbox("Antecedent (A)", ["Staff gives instruction", "Peer teases", "Bedtime", "Lunch time"])
    with col_b:
        b_raw = st.text_input("Describe Behavior (B)", placeholder="Avoid labels like 'rude'...")
        # Simple objective behavior check
        labels = ['rude', 'mean', 'lazy', 'brat', 'stupid', 'aggressive', 'attitude']
        if any(word in b_raw.lower() for word in labels):
            st.warning("⚠️ Warning: You used a judgmental label. Describe exactly what you SEE or HEAR (e.g., 'shouted', 'slammed door').")
    with col_c:
        c_type = st.radio("Consequence Type (C)", ["Positive Reinforcement", "Negative Reinforcement", "Response Cost"])

    if st.button("Analyze Pattern"):
        st.success(f"**Analysis:** Because the antecedent was '{a_input}', the youth chose to '{b_raw}'. By applying '{c_type}', you are influencing the likelihood this happens again.")

# --- MODULE 3: TEACHING INTERACTIONS ---
elif selection == "3. Teaching Interactions":
    st.title("🤝 Teaching Interactions")
    
    st.write("Staff use structured interactions to shape behavior.")
    
    interaction = st.selectbox("Select Interaction Type:", ["Proactive Teaching", "Effective Praise", "Corrective Teaching"])
    
    if interaction == "Proactive Teaching":
        st.info("Goal: Set them up for success *before* the behavior occurs.")
        st.markdown("1. Describe situation\n2. State expectations\n3. Give rationales\n4. Practice")
    elif interaction == "Effective Praise":
        st.success("Goal: Reinforce specific positive behaviors.")
        st.markdown("1. Show approval\n2. Describe behavior specifically\n3. Give rationales\n4. Positive consequence")
    else:
        st.error("Goal: Decrease inappropriate behavior and provide an alternative.")
        st.markdown("1. Initial praise/approval\n2. Description of inappropriate behavior\n3. Consequence\n4. Alternative behavior/Practice")

    st.subheader("The Rationale Generator")
    skill = st.selectbox("Skill to teach:", ["Following Instructions", "Accepting 'No'", "Disagreeing Appropriately"])
    r_type = st.radio("Rationale Type:", ["Benefit to Youth", "Concern for Others", "Negative Outcome"])
    
    if st.button("Generate Rationale"):
        if skill == "Following Instructions" and r_type == "Benefit to Youth":
            st.write("*'If you follow instructions now, you might finish sooner and have more time for video games.'*")
        elif skill == "Accepting 'No'" and r_type == "Negative Outcome":
            st.write("*'If you don't accept no, you might lose more points and stay on Level I longer.'*")
        else:
            st.write("*'Using this skill shows maturity and helps others feel respected.'*")

# --- MODULE 4: MOTIVATION SYSTEM ---
elif selection == "4. Motivation System Lab":
    st.title("💳 Digital Point Card Lab")
    
    st.subheader("Manual Point Entry")
    with st.form("point_entry"):
        col1, col2, col3 = st.columns(3)
        with col1:
            skill_input = st.selectbox("Skill", ["Following Instructions", "Accepting Criticism", "Task Completion", "Self-Control"])
        with col2:
            type_input = st.selectbox("Interaction Type", ["Effective Praise", "Corrective Teaching", "Proactive Teaching"])
        with col3:
            point_mod = st.radio("Target Skill?", ["Yes (+100/-200)", "No (+50/-100)"])
        
        behavior_note = st.text_input("Specific Behavior (e.g., 'said okay')")
        
        # Logic for values
        is_target = (point_mod == "Yes (+100/-200)")
        
        c1, c2 = st.columns(2)
        add_pos = c1.form_submit_button("Add Positive Points")
        add_neg = c2.form_submit_button("Add Negative Points")
        
        if add_pos:
            pts = 100 if is_target else 50
            new_row = {"Time": datetime.now().strftime("%H:%M"), "Skill": skill_input, "Type": type_input, "Behavior": behavior_note, "Points": pts}
            st.session_state.point_log = pd.concat([st.session_state.point_log, pd.DataFrame([new_row])], ignore_index=True)
            st.session_state.total_points += pts
            
        if add_neg:
            pts = -200 if is_target else -100
            new_row = {"Time": datetime.now().strftime("%H:%M"), "Skill": skill_input, "Type": type_input, "Behavior": behavior_note, "Points": pts}
            st.session_state.point_log = pd.concat([st.session_state.point_log, pd.DataFrame([new_row])], ignore_index=True)
            st.session_state.total_points += pts

    st.divider()
    st.subheader("Current Session Log")
    st.dataframe(st.session_state.point_log, use_container_width=True)
    
    if st.button("Clear Log"):
        st.session_state.point_log = pd.DataFrame(columns=["Time", "Skill", "Type", "Behavior", "Points"])
        st.session_state.total_points = 0
        st.rerun()

# --- MODULE 5: PROFESSIONALISM ---
elif selection == "5. Professionalism & Boundaries":
    st.title("⚖️ Professionalism & Boundaries")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("The Quality Components")
        st.write("93% of communication is non-verbal.")
        data = pd.DataFrame({
            'Component': ['Body Language', 'Voice Tone', 'Word Choice'],
            'Impact': [58, 35, 7]
        })
        st.bar_chart(data, x='Component', y='Impact')
    
    with col_right:
        st.subheader("Boundary Danger Signals")
        signals = [
            "Spending disproportionate time with one youth",
            "Feeling you are the only one who understands them",
            "Treating them differently based on your feelings",
            "Disclosing personal information without therapeutic value",
            "Defensiveness when questioned about interactions"
        ]
        for s in signals:
            st.checkbox(s)
            
    st.divider()
    st.subheader("Aversives & Prohibited Practices")
    st.warning("""
    **The Following are PROHIBITED in PEM:**
    * Corporal Punishment
    * Unreasonable Restitution
    * Violating Rights (food, privacy, communication)
    * Seclusion/Restraint (except for immediate safety)
    """)

st.sidebar.divider()
st.sidebar.caption("Boys Town PEM Framework - Staff Training Tool v1.0")
