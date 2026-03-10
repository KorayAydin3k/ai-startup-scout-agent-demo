"""
Research Agent - Searches and filters startups from the database.
"""

import pandas as pd
from typing import List, Dict, Tuple


class ResearchAgent:
    """Agent responsible for searching and filtering startup data."""

    # Region to country mapping
    REGION_TO_COUNTRIES = {
        "europe": ["France", "UK", "Germany", "Netherlands", "Switzerland", "Sweden", "Italy"],
        "us": ["USA"],
        "asia": ["Singapore", "Japan", "China", "India"],
        "australia": ["Australia"],
        "romania": ["Romania"],
        "italy": ["Italy"],
    }

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize research agent with startup data.

        Args:
            dataframe: Pandas DataFrame with startup data
        """
        self.df = dataframe.copy()
        self.search_results = None

    def _expand_regions_to_countries(self, regions: List[str]) -> List[str]:
        """
        Expand region names to actual country names.

        Args:
            regions: List of regions (e.g., ['europe', 'us'])

        Returns:
            List of country names
        """
        countries = set()

        for region in regions:
            region_lower = region.lower()

            # Check if it's a region that maps to countries
            if region_lower in self.REGION_TO_COUNTRIES:
                countries.update(self.REGION_TO_COUNTRIES[region_lower])
            else:
                # If not a known region, treat it as a direct country name
                # Capitalize first letter for matching with CSV data
                countries.add(region_lower.capitalize())
                # Assume it's a country name directly
                countries.add(region)

        return list(countries)

    def search_startups(
        self, sectors: List[str] = None, regions: List[str] = None
    ) -> pd.DataFrame:
        """
        Search startups by sector and region.

        Args:
            sectors: List of sectors to filter by
            regions: List of regions to filter by

        Returns:
            Filtered DataFrame of startups
        """
        results = self.df.copy()

        # Filter by sectors
        if sectors and sectors != ["all sectors"]:
            results = results[
                results["sector"].str.lower().isin([s.lower() for s in sectors])
            ]

        # Filter by regions (convert regions to countries first)
        if regions and regions != ["global"]:
            countries = self._expand_regions_to_countries(regions)
            results = results[results["country"].isin(countries)]

        # Sort by growth score (descending)
        results = results.sort_values("growth_score", ascending=False)

        self.search_results = results
        return results

    def get_search_summary(self) -> str:
        """Get summary of search results."""
        if self.search_results is None or len(self.search_results) == 0:
            return "No startups found matching your criteria. The requested data may not be available in our database."

        count = len(self.search_results)
        sectors = self.search_results["sector"].unique()
        countries = self.search_results["country"].unique()

        # Special message for specific country searches
        if len(countries) == 1 and countries[0] != "Global":
            country = countries[0]
            return f"Found {count} startup{'s' if count != 1 else ''} in {country}"

        return f"Found {count} startups in sectors: {', '.join(sectors)}"
