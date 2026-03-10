#!/usr/bin/env python3
"""Quick system test - verifies all components work"""

from agent import StartupScoutAgent

print("=" * 70)
print("AI STARTUP SCOUTING AGENT - SYSTEM TEST")
print("=" * 70)

try:
    # Test 1: Agent initialization
    print("\n[Test 1] Initializing agent...")
    agent = StartupScoutAgent()
    print("✓ Agent initialized successfully")

    # Test 2: Dataset loading
    print(f"[Test 2] Loading dataset...")
    print(f"✓ Loaded {len(agent.startups_df)} startups")

    # Test 3: Run a quick search
    print("\n[Test 3] Running a test search (AI startups in Europe)...")

    def progress(step, msg):
        print(f"  Step {step}: {msg}")

    report = agent.run("Find AI startups in Europe", progress_callback=progress)

    # Test 4: Verify results
    print("\n[Test 4] Verifying results...")
    assert report is not None, "Report is None"
    assert report["startups_analyzed"] > 0, "No startups found"
    assert report["top_pick"] is not None, "No top pick"
    print(f"✓ Found {report['startups_analyzed']} startups")
    print(f"✓ Top pick: {report['top_pick']['name']}")
    print(f"✓ Top score: {report['top_pick']['investment_score']:.2f}/5.0")

    # Test 5: Test agents individually
    print("\n[Test 5] Testing individual agents...")

    plan = agent.planner.analyze_query("AI startups")
    print(f"✓ Planner: Detected sectors = {plan['sectors']}")

    results = agent.research.search_startups(["AI"])
    print(f"✓ Research: Found {len(results)} results")

    analyses = agent.analyzer.analyze_batch(results.head(2))
    print(f"✓ Analysis: Generated {len(analyses)} insights")

    scored = agent.scorer.score_batch(results)
    print(f"✓ Scorer: Calculated {len(scored)} scores")

    print("\n" + "=" * 70)
    print("✓✓✓ ALL TESTS PASSED ✓✓✓")
    print("=" * 70)
    print("\nSystem is ready to use!")
    print("\nRun the web interface with:")
    print("  streamlit run app.py")
    print("\nOr run the demo with:")
    print("  python demo.py")

except Exception as e:
    print(f"\n❌ TEST FAILED: {e}")
    import traceback

    traceback.print_exc()
    exit(1)
