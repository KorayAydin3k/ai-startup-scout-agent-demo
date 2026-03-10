"""
Planner Agent - Analyzes user query and extracts sector information.
"""

from typing import Dict, List
import re


class PlannerAgent:
    """Agent responsible for understanding and planning the search query."""

    SECTOR_KEYWORDS = {
        "ai": ["ai", "artificial intelligence", "ml", "machine learning", "llm", "nlp"],
        "security": ["security", "cyber", "cybersecurity", "infosec"],
        "automation": ["automation", "rpa", "workflow"],
        "fintech": ["fintech", "finance", "financial", "payment", "banking"],
        "biotech": ["biotech", "bio", "healthcare", "medical", "pharma"],
        "climate": ["climate", "green", "sustainability", "energy"],
        "web3": ["web3", "crypto", "blockchain", "nft", "defi"],
    }

    REGIONS = {
        "europe": ["europe", "uk", "france", "germany", "netherlands", "switzerland", "italy"],
        "us": ["us", "usa", "united states", "america"],
        "asia": ["asia", "singapore", "japan", "china", "india"],
        "global": ["global", "worldwide", "all"],
        "italy": ["italy", "italian"],
        "uk": ["uk", "united kingdom", "britain"],
        "france": ["france", "french"],
        "germany": ["germany", "german"],
        "australia": ["australia", "australian"],
        "romania": ["romania", "romanian"],
    }

    def analyze_query(self, query: str) -> Dict:
        """
        Analyze user query and extract sector and region filters.

        Args:
            query: User input query

        Returns:
            Dictionary with extracted filters
        """
        query_lower = query.lower()

        # Extract sectors
        detected_sectors = []
        for sector, keywords in self.SECTOR_KEYWORDS.items():
            if any(keyword in query_lower for keyword in keywords):
                detected_sectors.append(sector)

        # Extract regions with priority logic
        detected_regions = []

        # Check for specific countries first
        for region, keywords in self.REGIONS.items():
            if region != "europe" and region != "global":  # Skip broad regions
                if any(keyword in query_lower for keyword in keywords):
                    detected_regions.append(region)

        # If no specific regions found, check for broad regions
        if not detected_regions:
            for region, keywords in self.REGIONS.items():
                if region in ["europe", "global"]:
                    if any(keyword in query_lower for keyword in keywords):
                        detected_regions.append(region)

        # If no sectors detected, search all
        if not detected_sectors:
            detected_sectors = list(self.SECTOR_KEYWORDS.keys())

        # If no regions detected, try to extract country names from query
        if not detected_regions:
            detected_regions = self._extract_countries_from_query(query_lower)

        # If still no regions detected, search all
        if not detected_regions:
            detected_regions = ["global"]

        return {
            "original_query": query,
            "sectors": detected_sectors,
            "regions": detected_regions,
            "search_all": len(detected_sectors) == len(self.SECTOR_KEYWORDS),
        }

    def _extract_countries_from_query(self, query_lower: str) -> List[str]:
        """
        Extract country names directly from the query.
        
        Args:
            query_lower: Lowercase query string
            
        Returns:
            List of extracted country names
        """
        # Common country names that might appear in queries
        known_countries = [
            "brazil", "canada", "mexico", "argentina", "chile", "colombia", "peru",
            "spain", "portugal", "belgium", "austria", "denmark", "finland", "norway",
            "poland", "czech", "hungary", "greece", "turkey", "russia", "israel",
            "south korea", "taiwan", "vietnam", "indonesia", "malaysia", "thailand",
            "philippines", "south africa", "nigeria", "kenya", "egypt", "uae", "saudi arabia"
        ]
        
        extracted = []
        for country in known_countries:
            if country in query_lower:
                extracted.append(country)
                
        return extracted

    def get_plan_summary(self, analysis: Dict) -> str:
        """Get a human-readable summary of the search plan."""
        sectors_str = ", ".join(analysis["sectors"]) if analysis["sectors"] else "all sectors"
        regions_str = ", ".join(analysis["regions"]) if analysis["regions"] else "global"

        return f"Plan: Search for startups in {sectors_str} across {regions_str}"
