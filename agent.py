"""
Main Agent Orchestrator - Coordinates all agents to execute startup search and analysis.
"""

import pandas as pd
import time
from typing import Dict, Tuple, Callable

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.scoring_agent import ScoringAgent
from agents.report_agent import ReportAgent


def load_startups() -> pd.DataFrame:
    """Load startup dataset."""
    return pd.read_csv("data/startups.csv")


class StartupScoutAgent:
    """Main orchestrator for the startup scouting system."""

    def __init__(self, data_path: str = "data/startups.csv"):
        """
        Initialize the agent system.

        Args:
            data_path: Path to startup dataset
        """
        self.startups_df = pd.read_csv(data_path)
        self.planner = PlannerAgent()
        self.research = ResearchAgent(self.startups_df)
        self.analyzer = AnalysisAgent()
        self.scorer = ScoringAgent()
        self.reporter = ReportAgent()

    def run(
        self, query: str, progress_callback: Callable[[str, str], None] = None
    ) -> Dict:
        """
        Execute the complete startup scouting workflow.

        Args:
            query: User query
            progress_callback: Function to call with progress updates (step_number, message)

        Returns:
            Final investment report
        """
        if progress_callback is None:
            progress_callback = lambda step, msg: None

        # Step 1: Plan
        progress_callback("1", "Understanding the query")
        time.sleep(0.5)  # Simulate thinking
        plan = self.planner.analyze_query(query)
        plan_summary = self.planner.get_plan_summary(plan)

        # Step 2: Research
        progress_callback("2", "Searching startup database")
        time.sleep(0.5)
        search_results = self.research.search_startups(
            sectors=plan["sectors"], regions=plan["regions"]
        )
        research_summary = self.research.get_search_summary()

        # Step 3: Analyze
        progress_callback("3", "Analyzing startups with AI")
        time.sleep(1)
        analyses = self.analyzer.analyze_batch(search_results)

        # Step 4: Score
        progress_callback("4", "Calculating investment scores")
        time.sleep(0.5)
        scored = self.scorer.score_batch(search_results)

        # Step 5: Report
        progress_callback("5", "Generating report")
        time.sleep(0.5)
        report = self.reporter.generate_report(scored, analyses, query=query)

        return report

    def get_plan_summary(self, query: str) -> str:
        """Get plan summary without running the full pipeline."""
        plan = self.planner.analyze_query(query)
        return self.planner.get_plan_summary(plan)