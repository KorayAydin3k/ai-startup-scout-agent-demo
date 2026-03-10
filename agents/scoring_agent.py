"""
Scoring Agent - Calculates investment scores for startups.
"""

import pandas as pd
import numpy as np


class ScoringAgent:
    """Agent responsible for calculating investment scores."""

    # Score weights
    GROWTH_WEIGHT = 0.5  # 50% - Growth score is most important
    FUNDING_WEIGHT = 0.3  # 30% - Funding amount
    EMPLOYEES_WEIGHT = 0.2  # 20% - Team size

    def calculate_score(self, startup: pd.Series) -> float:
        """
        Calculate investment score for a startup.

        Formula: score = (growth_score * 0.5) + (funding_million * 0.3) + (employees * 0.2)
        Then normalize to 0-100 scale.

        Args:
            startup: Pandas series with startup data

        Returns:
            Normalized investment score (0-100)
        """
        growth = startup["growth_score"]
        funding = startup["funding_million"]
        employees = startup["employees"]

        # Raw calculation
        raw_score = (
            growth * self.GROWTH_WEIGHT
            + funding * self.FUNDING_WEIGHT
            + employees * self.EMPLOYEES_WEIGHT
        )

        return round(raw_score / 100, 2)

    def score_batch(self, startups_df: pd.DataFrame) -> pd.DataFrame:
        """
        Score multiple startups.

        Args:
            startups_df: DataFrame with startup data

        Returns:
            DataFrame with added 'investment_score' column
        """
        results = startups_df.copy()
        results["investment_score"] = results.apply(self.calculate_score, axis=1)

        # Sort by investment score (descending)
        results = results.sort_values("investment_score", ascending=False)

        return results

    def get_top_startups(
        self, startups_df: pd.DataFrame, top_n: int = 5
    ) -> pd.DataFrame:
        """
        Get top N startups by investment score.

        Args:
            startups_df: DataFrame with startup data
            top_n: Number of top startups to return

        Returns:
            Top N startups sorted by score
        """
        scored = self.score_batch(startups_df)
        return scored.head(top_n)