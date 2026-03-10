#!/usr/bin/env python3
"""
Demo script showing how to use the AI Startup Scouting Agent programmatically.
Run with: python demo.py
"""

from agent import StartupScoutAgent
from datetime import datetime


def print_header(text: str):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)


def print_progress(step: str, message: str):
    """Print progress updates."""
    print(f"[Step {step}] {message}")


def demo_simple_search():
    """Demo 1: Simple sector search."""
    print_header("DEMO 1: Simple AI Startup Search")

    agent = StartupScoutAgent()

    print("\nRunning Query: 'Find promising AI startups'")
    print("-" * 70)

    report = agent.run("Find promising AI startups", progress_callback=print_progress)

    print("\n📊 RESULTS:")
    print(f"Startups analyzed: {report['startups_analyzed']}")
    print(f"Summary: {report['summary']}\n")

    for rec in report["recommendations"]:
        print(f"{rec['rank']}. {rec['name']}")
        print(f"   Score: {rec['investment_score']:.2f}/5.0 | {rec['recommendation']}")
        print(f"   Sector: {rec['sector']} | Country: {rec['country']}")
        print(f"   Insight: {rec['insight'][:100]}...\n")


def demo_geographic_filter():
    """Demo 2: Geographic filtering."""
    print_header("DEMO 2: European Startup Discovery")

    agent = StartupScoutAgent()

    print("\nRunning Query: 'Find startups in Europe'")
    print("-" * 70)

    report = agent.run("Find startups in Europe", progress_callback=print_progress)

    print("\n📊 RESULTS:")
    print(f"European startups found: {report['startups_analyzed']}\n")

    # Group by country
    by_country = {}
    for rec in report["recommendations"]:
        country = rec["country"]
        if country not in by_country:
            by_country[country] = []
        by_country[country].append(rec)

    for country in sorted(by_country.keys()):
        companies = by_country[country]
        print(f"\n{country}: {len(companies)} company/companies")
        for rec in companies:
            print(f"  • {rec['name']} ({rec['sector']}) - Score: {rec['investment_score']:.2f}")


def demo_advanced_search():
    """Demo 3: Advanced combined search."""
    print_header("DEMO 3: Advanced Combined Search")

    agent = StartupScoutAgent()

    query = "Find top-funded AI companies in Europe"
    print(f"\nRunning Query: '{query}'")
    print("-" * 70)

    report = agent.run(query, progress_callback=print_progress)

    if report["recommendations"]:
        top = report["top_pick"]
        print("\n🎯 TOP RECOMMENDATION:")
        print(f"   Name: {top['name']}")
        print(f"   Country: {top['country']}")
        print(f"   Sector: {top['sector']}")
        print(f"   Funding: ${top['funding_million']:.0f}M")
        print(f"   Employees: {top['employees']}")
        print(f"   Growth Score: {top['growth_score']}/100")
        print(f"   Investment Score: {top['investment_score']:.2f}/5.0")
        print(f"   \n💡 AI Insight: {top['insight']}")


def demo_programmatic_usage():
    """Demo 4: Programmatic usage patterns."""
    print_header("DEMO 4: Programmatic Usage Patterns")

    agent = StartupScoutAgent()

    print("\n1. Access agents individually:")
    print("-" * 70)

    # Use planner directly
    plan = agent.planner.analyze_query("AI startups in Germany")
    print(f"Analyzed query: sectors={plan['sectors']}, regions={plan['regions']}")

    # Use research directly
    results = agent.research.search_startups(sectors=["AI"], regions=["Germany"])
    print(f"\nFound {len(results)} AI startups in Germany:")
    for name in results["name"]:
        print(f"  • {name}")

    print("\n2. Chain operations:")
    print("-" * 70)

    # Score startups manually
    scored = agent.scorer.score_batch(results)
    top_5 = agent.scorer.get_top_startups(results, top_n=5)

    print(f"Top 5 AI startups in Germany:")
    for idx, (_, row) in enumerate(top_5.iterrows(), 1):
        print(f"  {idx}. {row['name']} - Score: {row['investment_score']:.2f}")


def demo_export():
    """Demo 5: Generate a professional report."""
    print_header("DEMO 5: Professional Report Export")

    agent = StartupScoutAgent()

    query = "Find security companies globally"
    print(f"\nGenerating report for: '{query}'")
    print("-" * 70)

    report = agent.run(query)

    # Export as formatted text
    report_text = agent.reporter.export_summary()
    print(report_text)

    # Save to file
    filename = f"startup_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(report_text)
    print(f"\n✓ Report saved to: {filename}")


def main():
    """Run all demos."""
    print("\n" + "🚀 " * 20)
    print("     AI STARTUP SCOUTING AGENT - DEMO")
    print("🚀 " * 20 + "\n")

    try:
        # Run demos
        demo_simple_search()
        input("\nPress Enter to continue to Demo 2...")

        demo_geographic_filter()
        input("\nPress Enter to continue to Demo 3...")

        demo_advanced_search()
        input("\nPress Enter to continue to Demo 4...")

        demo_programmatic_usage()
        input("\nPress Enter to continue to Demo 5...")

        demo_export()

        print_header("ALL DEMOS COMPLETED ✨")
        print("\nThe system is ready for use!")
        print("\nFor interactive web interface, run:")
        print("  streamlit run app.py\n")

    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
