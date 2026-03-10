# 🚀 AI Startup Scouting Agent - Complete Setup Guide

## ✨ What You've Built

You now have a professional, production-ready **multi-agent AI system** that demonstrates advanced AI architecture for startup evaluation. This is a portfolio-quality demo project showcasing:

- ✅ Multi-agent architecture (Planner, Research, Analysis, Scoring, Reporter)
- ✅ Professional code structure and modularity
- ✅ Local LLM integration (Ollama support)
- ✅ Interactive web interface (Streamlit)
- ✅ Data filtering and analysis pipeline
- ✅ Investment scoring algorithm
- ✅ AI-powered insights generation

## 📦 Project Contents

```
ai-startup-scout-agent/
├── 📄 README.md                      # Full documentation
├── 📄 QUICKSTART.md                  # Quick start guide
├── 📄 SETUP.md                       # This file
├── 📄 requirements.txt                # Python dependencies
│
├── 🚀 app.py                          # Streamlit web interface
├── 🤖 agent.py                        # Main agent orchestrator
├── 🏃 run.bat                        # Quick launcher (Windows)
├── 🏃 run.sh                         # Quick launcher (Mac/Linux)
│
├── 📁 agents/                        # Agent modules
│   ├── planner_agent.py              # Query analysis
│   ├── research_agent.py             # Database search
│   ├── analysis_agent.py             # AI analysis
│   ├── scoring_agent.py              # Investment scoring
│   └── report_agent.py               # Report generation
│
├── 📁 llm/                           # LLM integration
│   └── ollama_client.py              # Local LLM client
│
└── 📁 data/                          # Datasets
    └── startups.csv                  # Startup database (20 startups)
```

## 🎯 Quick Start (3 Steps)

### Step 1: Install Python Dependencies

```bash
cd ai-startup-scout-agent
pip install -r requirements.txt
```

This installs:
- Streamlit (web interface)
- Pandas (data manipulation)
- Numpy (numerical computing)
- Requests (HTTP client)

### Step 2: Run the Application

Choose ONE of these options:

**Option A: Windows (Easy)**
```bash
run.bat
```

**Option B: Mac/Linux**
```bash
bash run.sh
```

**Option C: Manual**
```bash
streamlit run app.py
```

### Step 3: Open in Browser

The application automatically opens at: **http://localhost:8501**

## 🔍 How to Use

### 1. Enter a Search Query

Type natural language queries like:
- "Find AI startups in Europe"
- "Show me the best fintech opportunities"
- "What promising companies are in the UK?"

### 2. Click "Run Agent"

The system will:
1. **Plan** - Understand your query
2. **Research** - Find matching startups
3. **Analyze** - Generate AI insights
4. **Score** - Calculate investment potential
5. **Report** - Present recommendations

### 3. Review Results

See:
- Investment scores (0-5.0)
- AI-generated insights
- Company metrics
- Recommendation levels

## 🤖 Understanding the Agent System

### 1. **Planner Agent** 📋
- Analyzes your natural language query
- Extracts sector and geographic filters
- Examples: "AI" ➜ `["AI"]`, "Europe" ➜ `["UK", "France", "Germany", ...]`

### 2. **Research Agent** 🔍
- Searches the startup database
- Filters by sector and region
- Returns sorted results by growth potential

### 3. **Analysis Agent** 🤖
- Uses AI to generate investment insights
- Works with Ollama (local LLM) if available
- Fallback to intelligent responses otherwise

### 4. **Scoring Agent** 📊
- Calculates investment potential using formula:
  ```
  Score = (Growth×0.5 + Funding×0.3 + Employees×0.2) / 100
  ```
- Normalizes to 0-5.0 scale
- Ranks startups by score

### 5. **Report Agent** 📑
- Formats results
- Generates recommendations
- Assigns confidence levels

## 🎓 Example Queries

Try these to explore:

```
"Find AI startups"
"Look for cybersecurity companies in Europe"
"Show top-funded startups globally"
"What promising startups are in the UK?"
"Find well-funded automation companies"
```

## 📊 Sample Dataset

Includes 20 real startups across:

- **AI/ML**: Mistral AI, HuggingFace, DeepL, Stability AI
- **Security**: Snyk
- **Fintech**: Stripe, Wise, Revolut, Klarna
- **Design**: Canva, Figma
- **Productivity**: Notion, Linear
- **Hardware**: SpaceX
- And more...

## 🚀 Advanced Features

### Enable Ollama for Enhanced AI

For better AI insights, install Ollama:

1. **Download**: https://ollama.ai
2. **Install a model**: `ollama pull mistral`
3. **Start server**: `ollama serve`
4. **Run app**: Application automatically uses Ollama

If Ollama is unavailable, the system uses intelligent fallbacks.

### Programmatic Usage

Use the agent directly in Python:

```python
from agent import StartupScoutAgent

agent = StartupScoutAgent()
report = agent.run("Find AI startups in Europe")

print(f"Found {report['startups_analyzed']} startups")
for rec in report["recommendations"]:
    print(f"  {rec['name']}: {rec['investment_score']:.2f}/5.0")
```

### Export Reports

Download results as formatted text files with full details.

## 📈 Investment Scoring Explained

```
Formula: Score = (Growth×0.5 + Funding×0.3 + Employees×0.2) / 100

Weight Distribution:
- Growth Score (50%)  → Most important growth indicator
- Funding (30%)       → Capital available
- Team Size (20%)     → Operational maturity

Recommendation Levels:
- ⭐⭐⭐ Strong Buy (4.0+)
- ⭐⭐ Buy (3.0-4.0)
- ⭐ Interesting (2.0-3.0)
- Monitor (<2.0)
```

## 🐛 Troubleshooting

### Issue: "Module not found" error

**Solution**:
```bash
pip install -r requirements.txt
```

### Issue: Port 8501 already in use

**Solution**:
```bash
streamlit run app.py --server.port 8502
```

### Issue: No AI insights (just using fallbacks)

**Solution**: 
Make sure Ollama is installed and running:
```bash
ollama serve
```

The system works perfectly without Ollama - it uses intelligent fallback responses.

### Issue: Streamlit not found

**Solution**:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 🏗️ Project Architecture

```
USER INTERFACE
    ↓
STREAMLIT APP (app.py)
    ↓
AGENT ORCHESTRATOR (agent.py)
    ├─→ PLANNER AGENT (understand query)
    ├─→ RESEARCH AGENT (find startups)
    ├─→ ANALYSIS AGENT (generate insights)
    ├─→ SCORING AGENT (calculate scores)
    └─→ REPORT AGENT (format results)
    ↓
LLM CLIENT (ollama_client.py)
    ├─→ Ollama (if available)
    └─→ Intelligent Fallback (if not)
    ↓
DATA LAYER
    └─→ Startup Database (startups.csv)
```

## 💻 System Requirements

- **Python**: 3.8+ (3.10+ recommended)
- **RAM**: 2GB minimum (4GB+ for smooth operation)
- **Disk**: ~500MB for dependencies
- **Internet**: Optional (all processing is local)

## 🔐 Security & Privacy

- ✅ **No cloud dependencies** - Everything runs locally
- ✅ **No API keys required** - No external services
- ✅ **No data transmission** - Your data stays on your computer
- ✅ **Privacy-first** - No tracking or telemetry

## 📚 Code Quality

The codebase features:

- **Type hints** for all functions
- **Docstrings** for all modules
- **Error handling** with graceful fallbacks
- **Modular design** - each agent is independent
- **Clean code** - PEP 8 compliant
- **Production-ready** - suitable for portfolio/demo

## 🎯 Use Cases

This system showcases:

1. **Portfolio project** - Demonstrates AI system design
2. **Learning tool** - Understand multi-agent architecture
3. **Demo application** - Show investors/clients your skills
4. **Prototype** - Basis for real startup evaluation tool
5. **Research** - Experiment with agent systems

## 🚀 Next Steps

### Immediate (Running the App)
1. Run `streamlit run app.py` or `run.bat`
2. Try different searches
3. Explore the recommendations

### Short-term (Extend the System)
1. Add more startups to `data/startups.csv`
2. Modify the scoring formula
3. Add new sectors/regions
4. Customize UI styling

### Medium-term (Production)
1. Connect to real startup APIs
2. Add database persistence
3. Implement user accounts
4. Add export/reporting features

## 📞 Support & Documentation

- **README.md** - Complete documentation
- **QUICKSTART.md** - Quick reference guide
- **Code docstrings** - All functions have detailed documentation
- **demo.py** - Shows example usage patterns

## ✨ Key Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Multi-agent system | ✅ | 5 specialized agents |
| Web interface | ✅ | Streamlit-based |
| Data filtering | ✅ | By sector & region |
| AI analysis | ✅ | Ollama integration |
| Investment scoring | ✅ | Weighted formula |
| Report generation | ✅ | Formatted output |
| Local only | ✅ | No cloud required |
| No API keys | ✅ | Fully self-contained |
| Export feature | ✅ | Download reports |

## 🎉 You're All Set!

Your AI Startup Scouting Agent is ready to impress!

### Quick Links:
- **Run it**: `streamlit run app.py`
- **Demo**: `python demo.py`
- **Test**: `python quicktest.py`
- **Debug**: `python debug_query.py`

---

**Built with ❤️ as a professional demonstration of multi-agent AI architecture**

Happy exploring! 🚀✨
