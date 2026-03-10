#!/usr/bin/env python3
"""Quick system test - minimal version"""

from agent import StartupScoutAgent

print("Testing AI Startup Scouting Agent...")
print("=" * 60)

try:
    # Initialize
    agent = StartupScoutAgent()
    print("✓ Agent initialized")
    print(f"✓ Dataset: {len(agent.startups_df)} startups loaded")

    # Test individual agents without full pipeline
    print("\nTesting individual agent components:")

    # Test planner
    plan = agent.planner.analyze_query("AI startups in Europe")
    print(f"✓ Planner: {len(plan['sectors'])} sectors, {len(plan['regions'])} regions")

    # Test research
    results = agent.research.search_startups(["ai"], ["europe"])
    print(f"✓ Research: Found {len(results)} startups")

    # Test scorer
    scored = agent.scorer.score_batch(results)
    print(f"✓ Scorer: Calculated {len(scored)} scores")

    # Test reporter (minimal)
    analyses = {row["name"]: "Good startup" for _, row in results.head(3).iterrows()}
    report = agent.reporter.generate_report(scored, analyses, "Test query")
    print(f"✓ Reporter: Generated report with {len(report['recommendations'])} items")

    print("\n" + "=" * 60)
    print("✅ SYSTEM IS OPERATIONAL AND READY TO USE!")
    print("=" * 60)
    print("\nRun the web interface with:")
    print("  streamlit run app.py")

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback

    traceback.print_exc()
    exit(1)
