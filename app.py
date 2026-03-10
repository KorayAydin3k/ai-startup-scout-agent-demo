"""
Streamlit Web Interface for AI Startup Scouting Agent.
Run with: streamlit run app.py
"""

import streamlit as st
import time
from typing import Dict
from agent import StartupScoutAgent

# Page configuration
st.set_page_config(
    page_title="AI Startup Scouting Agent",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    .main {
        padding-top: 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stMetric > div {
        color: #1f1f1f !important;
    }
    h1, h2, h3, h4, h5 {
        color: #ffffff !important;
    }
    .stButton>button {
        background-color: #4e4eaa;
        color: #ffffff;
        border: none;
        border-radius: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #6a6ae0;
    }
    .stProgress>div>div>div>div {
        background-color: #8f92ff !important;
    }
    .stProgress>div>div {
        background-color: #444488 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #0d47a1 !important;
        font-weight: bold;
    }
    div[data-testid="stMetricLabel"] {
        color: #424242 !important;
    }
    /* dark background and improved card style */
    .recommendation-card, .rec-card {
        background-color: #2c2c54;
        padding: 1.5rem;
        border-radius: 1rem;
        margin: 1rem 0;
        color: #ffffff;
    }
    .rec-card h2 {
        margin: 0 0 0.5rem 0;
        color: #ffffff;
    }
    .rec-card p {
        margin: 0.2rem 0;
        color: #e0e0e0;
        font-size: 0.9rem;
    }
    .score-bar {
        background-color: #444488;
        border-radius: 10px;
        overflow: hidden;
        height: 12px;
        margin: 0.5rem 0;
    }
    .score-fill {
        background-color: #8f92ff;
        height: 100%;
    }
    body {
        background-color: #1a1a2e;
    }
    .stApp {
        background-color: #1a1a2e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state
if "agent" not in st.session_state:
    st.session_state.agent = StartupScoutAgent()
if "report" not in st.session_state:
    st.session_state.report = None
if "running" not in st.session_state:
    st.session_state.running = False


def render_hero():
    """Render the hero section."""
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🚀 AI Startup Scouting Agent")
        st.markdown(
            "Discover promising startups using multi-agent AI analysis",
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown("### Multi-Agent System")
        agents = ["📋 Planner", "🔍 Research", "🤖 Analysis", "📊 Scorer", "📑 Reporter"]
        for agent in agents:
            st.caption(agent)


def render_input_section():
    """Render the input section."""
    st.markdown("---")
    st.markdown("### 🎯 Search for Startups")

    col1, col2 = st.columns([4, 1])

    with col1:
        query = st.text_input(
            "Enter your search query:",
            placeholder="e.g., Find promising AI startups in Europe",
            label_visibility="collapsed",
        )

    with col2:
        run_button = st.button("🔍 Run Agent", key="run_button", use_container_width=True)

    return query, run_button


def render_progress_section(placeholder):
    """Create progress indicator."""
    steps = [
        ("1", "Understanding the query"),
        ("2", "Searching startup database"),
        ("3", "Analyzing startups with AI"),
        ("4", "Calculating investment scores"),
        ("5", "Generating report"),
    ]

    progress_text = "Agent Thinking..."
    progress_bar = st.progress(0)

    return progress_text, progress_bar, steps


def run_agent_pipeline(query: str):
    """Run the complete agent pipeline."""
    # Create containers for progress
    progress_container = st.container()

    with progress_container:
        st.markdown("### 🤖 Agent Thinking...")

        # Create progress columns
        progress_col = st.columns(5)
        step_indicators = progress_col

        def progress_callback(step_num: str, message: str):
            """Update progress indicators."""
            step_idx = int(step_num) - 1

            for i in range(5):
                with step_indicators[i]:
                    if i < step_idx:
                        st.success(f"Step {i + 1}\n✓")
                    elif i == step_idx:
                        with st.spinner():
                            st.info(f"Step {i + 1}\n⏳")
                    else:
                        st.write(f"Step {i + 1}\n⏱")

            time.sleep(0.3)

        # Run the agent
        st.session_state.report = st.session_state.agent.run(
            query, progress_callback=progress_callback
        )

        # Mark all steps as complete
        for i in range(5):
            with step_indicators[i]:
                st.success(f"Step {i + 1}\n✓")

    st.success("✅ Analysis Complete!")


def render_results(report: Dict):
    """Render the results section."""
    st.markdown("---")
    st.markdown("### 📊 Investment Recommendations")

    if not report or not report.get("recommendations"):
        st.warning("No startups found matching your criteria.")
        return

    # Summary statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Startups Analyzed", report["startups_analyzed"])
    with col2:
        if report["top_pick"]:
            st.metric("Top Score", f"{report['top_pick']['investment_score']:.2f}/5.0")
    with col3:
        st.metric("Recommendations", len(report["recommendations"]))

    st.markdown("")

    # Top recommendation highlight
    if report["top_pick"]:
        top = report["top_pick"]
        pct_top = (top['investment_score'] / 5.0) * 100
        st.markdown("#### 🎯 Top Recommendation")
        st.markdown(f"""
        <div class="rec-card">
            <h2>1. {top['name']}</h2>
            <p>📍 {top['country']} &nbsp; • &nbsp; 🏷️ {top['sector']} &nbsp; • &nbsp; 💰 ${top['funding_million']:.0f}M &nbsp; • &nbsp; 👥 {top['employees']} &nbsp; • &nbsp; 🏛️ Founded {top['founding_year']}</p>
            <div class="score-bar"><div class="score-fill" style="width: {pct_top:.1f}%;"></div></div>
            <p><strong>Investment Score:</strong> {top['investment_score']:.2f} / 5.00</p>
            <p>💡 {top['insight']}</p>
            <p>⭐ {top['recommendation']}</p>
        </div>
        """, unsafe_allow_html=True)

    # All recommendations
    if len(report["recommendations"]) > 1:
        st.markdown("#### 📋 All Recommendations")

        for rec in report["recommendations"]:
            # compute width percentage for score bar
            pct = (rec['investment_score'] / 5.0) * 100
            st.markdown(f"""
            <div class="rec-card">
                <h2>{rec['rank']}. {rec['name']}</h2>
                <p>📍 {rec['country']} &nbsp; • &nbsp; 🏷️ {rec['sector']} &nbsp; • &nbsp; 💰 ${rec['funding_million']:.0f}M &nbsp; • &nbsp; 👥 {rec['employees']} &nbsp; • &nbsp; 🏛️ Founded {rec['founding_year']}</p>
                <div class="score-bar"><div class="score-fill" style="width: {pct:.1f}%;"></div></div>
                <p><strong>Investment Score:</strong> {rec['investment_score']:.2f} / 5.00</p>
                <p>💡 {rec['insight']}</p>
                <p>⭐ {rec['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)


def main():
    """Main Streamlit app."""
    # Header
    render_hero()

    # Input section
    query, run_button = render_input_section()

    # Handle agent execution
    if run_button and query:
        with st.spinner("Running agent pipeline..."):
            run_agent_pipeline(query)

    # Display results
    if st.session_state.report:
        render_results(st.session_state.report)

        # Export option
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 1, 2])

        with col1:
            if st.button("📥 Download Report"):
                report_text = st.session_state.agent.reporter.export_summary()
                st.download_button(
                    label="Download as Text",
                    data=report_text,
                    file_name="startup_report.txt",
                    mime="text/plain",
                )

        with col2:
            if st.button("🔄 New Search"):
                st.session_state.report = None
                st.rerun()

    # Footer
    st.markdown("---")
    st.markdown(
        "**AI Startup Scouting Agent** • Multi-Agent AI System | "
        "Powered by Ollama + Streamlit"
    )


if __name__ == "__main__":
    main()
