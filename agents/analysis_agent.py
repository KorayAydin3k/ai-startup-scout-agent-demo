"""
Analysis Agent - Generates AI-powered investment insights for startups.
"""

from llm.ollama_client import OllamaClient
from typing import Dict
import pandas as pd


class AnalysisAgent:
    """Agent responsible for generating AI-powered investment analysis."""

    def __init__(self, model: str = "mistral"):
        """
        Initialize analysis agent with LLM client.

        Args:
            model: LLM model to use
        """
        self.llm = OllamaClient(model=model)
        self.analyses = {}

    def analyze_startup(self, startup_row: pd.Series) -> str:
        """
        Generate investment insight for a startup using LLM.

        Args:
            startup_row: Pandas series with startup data

        Returns:
            AI-generated investment insight
        """
        name = startup_row["name"]

        # Check cache
        if name in self.analyses:
            return self.analyses[name]

        # Build prompt
        prompt = f"""Provide a brief professional investment insight (1-2 sentences) for this startup:

Name: {startup_row["name"]}
Sector: {startup_row["sector"]}
Country: {startup_row["country"]}
Funding: ${startup_row["funding_million"]}M
Employees: {startup_row["employees"]}
Growth Score: {startup_row["growth_score"]}/100
Founded: {startup_row["founded"]}

Focus on investment potential and market position. Be concise and professional."""

        insight = self.llm.generate(prompt, max_tokens=150)

        self.analyses[name] = insight
        return insight

    def analyze_batch(self, startups_df: pd.DataFrame) -> Dict[str, str]:
        """
        Analyze multiple startups.

        Args:
            startups_df: DataFrame with startup data

        Returns:
            Dictionary mapping startup name to insight
        """
        results = {}
        for idx, row in startups_df.iterrows():
            results[row["name"]] = self.analyze_startup(row)

        return results
