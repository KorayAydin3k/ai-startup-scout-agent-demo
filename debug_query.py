#!/usr/bin/env python3
"""Debug script to test query parsing"""

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agent import load_startups

# Test planner
planner = PlannerAgent()
plan = planner.analyze_query("Find AI startups in Europe")

print("Query Analysis:")
print(f"  Original: 'Find AI startups in Europe'")
print(f"  Sectors detected: {plan['sectors']}")
print(f"  Regions detected: {plan['regions']}")
print()

# Test research
df = load_startups()
print(f"Dataset has {len(df)} startups")
print(f"Sectors in dataset: {df['sector'].unique().tolist()}")
print(f"Countries in dataset: {df['country'].unique().tolist()}")
print()

# Test search
research = ResearchAgent(df)
results = research.search_startups(sectors=plan['sectors'], regions=plan['regions'])

print(f"Search results: {len(results)} startups found")
if len(results) > 0:
    print("Results:")
    for name in results['name']:
        print(f"  - {name}")
else:
    print("No results found!")
    
    # Debug: test individual filters
    print("\nDebug individual filters:")
    
    # Test by sector only
    sector_filter = df[df["sector"].str.lower().isin([s.lower() for s in plan["sectors"]])]
    print(f"  Filter by sectors {plan['sectors']}: {len(sector_filter)} results")
    
    # Test by region only
    region_filter = df[df["country"].str.lower().isin([r.lower() for r in plan["regions"]])]
    print(f"  Filter by regions {plan['regions']}: {len(region_filter)} results")
