"""
Report Agent - Generates final investment recommendation reports.
"""

import pandas as pd
from typing import Dict, List


class ReportAgent:
    """Agent responsible for generating investment recommendation reports."""

    def __init__(self):
        """Initialize report agent."""
        self.report = None

    def generate_report(
        self,
        startups_df: pd.DataFrame,
        analyses: Dict[str, str],
        query: str = "",
    ) -> Dict:
        """
        Generate a comprehensive investment report.

        Args:
            startups_df: DataFrame with scored startups (must have 'investment_score')
            analyses: Dictionary mapping startup names to AI insights
            query: Original user query

        Returns:
            Dictionary containing report data
        """
        # Check if we have any startups to analyze
        if startups_df.empty:
            return {
                "query": query,
                "startups_analyzed": 0,
                "recommendations": [],
                "top_pick": None,
                "summary": "No startups found matching your search criteria. The requested data may not be available in our database.",
            }

        # Validate input
        if "investment_score" not in startups_df.columns:
            raise ValueError("Startups DataFrame must have 'investment_score' column")

        # Sort by score (descending)
        ranked = startups_df.sort_values("investment_score", ascending=False)

        # Build recommendations
        recommendations = []
        for idx, (_, row) in enumerate(ranked.iterrows(), 1):
            name = row["name"]
            insight = analyses.get(name, "No insight available")

            recommendation = {
                "rank": idx,
                "name": name,
                "sector": row["sector"],
                "country": row["country"],
                "founding_year": row["founded"],
                "employees": int(row["employees"]),
                "funding_million": float(row["funding_million"]),
                "growth_score": int(row["growth_score"]),
                "investment_score": float(row["investment_score"]),
                "insight": insight,
                "recommendation": self._get_recommendation_level(
                    row["investment_score"]
                ),
            }
            recommendations.append(recommendation)

        # Build report
        self.report = {
            "query": query,
            "startups_analyzed": len(ranked),
            "recommendations": recommendations,
            "top_pick": recommendations[0] if recommendations else None,
            "summary": self._generate_summary(recommendations),
        }

        return self.report

    def _get_recommendation_level(self, score: float) -> str:
        """Determine recommendation level based on score."""
        if score >= 4.0:
            return "⭐⭐⭐ Strong Buy"
        elif score >= 3.0:
            return "⭐⭐ Buy"
        elif score >= 2.0:
            return "⭐ Interesting"
        else:
            return "Monitor"

    def _generate_summary(self, recommendations: List[Dict]) -> str:
        """Generate executive summary."""
        if not recommendations:
            return "No startups found matching criteria."

        top_3 = recommendations[:3]
        top_names = ", ".join([r["name"] for r in top_3])
        top_score = recommendations[0]["investment_score"]

        return (
            f"Top recommendations: {top_names}. "
            f"Best opportunity has investment score of {top_score}/5.0"
        )

    def export_summary(self) -> str:
        """Export report as formatted text."""
        if not self.report:
            return "No report generated yet."

        output = []
        output.append("=" * 70)
        output.append("AI STARTUP SCOUTING AGENT - INVESTMENT REPORT")
        output.append("=" * 70)
        output.append("")

        if self.report["query"]:
            output.append(f"Query: {self.report['query']}")
            output.append("")

        output.append(f"Startups Analyzed: {self.report['startups_analyzed']}")
        output.append("")

        if self.report["top_pick"]:
            output.append("🎯 TOP RECOMMENDATION")
            output.append("-" * 70)
            top = self.report["top_pick"]
            output.append(f"{top['rank']}. {top['name']} - {top['recommendation']}")
            output.append(
                f"   Score: {top['investment_score']:.2f}/5.0 | "
                f"Sector: {top['sector']} | Country: {top['country']}"
            )
            output.append("   " + top["insight"])
            output.append("")

        if len(self.report["recommendations"]) > 1:
            output.append("📊 ALL RECOMMENDATIONS")
            output.append("-" * 70)
            for rec in self.report["recommendations"]:
                output.append(f"{rec['rank']}. {rec['name']} - {rec['recommendation']}")
                output.append(
                    f"   Score: {rec['investment_score']:.2f}/5.0 | "
                    f"Funding: ${rec['funding_million']:.0f}M | "
                    f"Employees: {rec['employees']}"
                )

        output.append("")
        output.append("=" * 70)

        return "\n".join(output)
