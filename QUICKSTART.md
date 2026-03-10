# 🚀 Quick Start Guide

## Installation

1. **Navigate to the project folder:**
   ```bash
   cd ai-startup-scout-agent
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

The system is ready to run! There are two ways to interact with it:

### Option 1: Web Interface (Recommended)

Run the interactive Streamlit web application:

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501` and enter your search queries like:
- "Find promising AI startups in Europe"
- "Show top fintech opportunities globally"
- "What about security startups in the UK?"

### Option 2: Python Script

Use the agent directly in Python:

```python
from agent import StartupScoutAgent

# Initialize the agent
agent = StartupScoutAgent()

# Run a search
def handle_progress(step, message):
    print(f"[Step {step}] {message}")

report = agent.run(
    "Find AI startups in Europe",
    progress_callback=handle_progress
)

# Display results
print(report["summary"])
for rec in report["recommendations"]:
    print(f"  {rec['rank']}. {rec['name']} - Score: {rec['investment_score']:.2f}")
```

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** 2GB minimum (4GB+ recommended)
- **Disk Space:** ~500MB for dependencies

## Optional: Using Ollama for AI Insights

For enhanced AI-powered analysis (not required, but recommended):

1. **Download Ollama:** https://ollama.ai

2. **Install a model:**
   ```bash
   ollama pull mistral
   ```

3. **Start the Ollama server:**
   ```bash
   ollama serve
   ```

4. **Run the app** - It will automatically use Ollama if available

If Ollama is not installed, the system uses intelligent fallback responses.

## Project Structure

```
ai-startup-scout-agent/
├── app.py                 # Web interface (run this!)
├── agent.py               # Main orchestrator
├── agents/                # Individual agents
├── llm/                   # LLM integration
├── data/                  # Startup dataset
└── requirements.txt       # Dependencies
```

## Examples

### Example 1: Search by Sector
```
Query: "Find AI startups"
Result: Shows all AI companies sorted by investment potential
```

### Example 2: Geographic Filter
```
Query: "Show startups in Europe"
Result: Filters to European companies across all sectors
```

### Example 3: Combined Search
```
Query: "Find promising fintech companies in the UK"
Result: Returns UK-based fintech companies ranked by score
```

## How It Works

1. **You enter a query** → Planner analyzes it
2. **Research agent** → Finds matching startups
3. **Analysis agent** → Generates AI insights
4. **Scoring agent** → Calculates investment scores
5. **Report agent** → Formats final report
6. **You see results** → Ranked recommendations with details

## Dataset

The system comes with 20 well-known startups including:
- **Mistral AI** - France
- **HuggingFace** - France  
- **Stability AI** - UK
- **Stripe** - USA
- **Notion** - USA
- **Figma** - USA
- And 14 more...

## Scoring Formula

```
Investment Score = (Growth×0.5 + Funding×0.3 + Employees×0.2) / 100
```

Scores range from 0-5.0:
- **4.0+** = ⭐⭐⭐ Strong Buy
- **3.0-4.0** = ⭐⭐ Buy
- **2.0-3.0** = ⭐ Interesting
- **<2.0** = Monitor

## Troubleshooting

### ImportError: No module named 'streamlit'
```bash
pip install -r requirements.txt
```

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

### Ollama not responding
- Make sure Ollama is installed and running: `ollama serve`
- The system works fine without Ollama - it will use fallback responses

## Next Steps

1. Start the web interface: `streamlit run app.py`
2. Try different search queries
3. Explore the recommendation details
4. Experiment with different sector/geographic combinations

---

For more details, see [README.md](README.md)

**Happy exploring! 🚀**
