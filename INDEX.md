# 📚 Project Index & Documentation Map

## 🎯 Welcome to AI Startup Scouting Agent

This is a **professional, production-ready multi-agent AI system** for discovering and evaluating startups. Choose your path below:

## 🚀 Quick Start (Pick One)

### ⚡ I Just Want to Run It (5 minutes)
```bash
pip install -r requirements.txt
streamlit run app.py
```
**Then**: Open http://localhost:8501 and start searching!

📖 **More details**: See [QUICKSTART.md](QUICKSTART.md)

### 🎓 I Want to Understand It (30 minutes)
1. Read [README.md](README.md) - Full system overview
2. Run `python quicktest.py` - See it in action
3. Explore the code in `agents/` directory

### 🔬 I Want to Experiment (1-2 hours)
1. Review [SETUP.md](SETUP.md) - Complete setup guide
2. Run `python demo.py` - 5 different examples
3. Try `python debug_query.py` - Understand query parsing
4. Modify `agents/` to customize behavior

### 💼 I Want to Use It for a Project (see below)

## 📖 Documentation Guide

| Document | Purpose | Read Time |
|----------|---------|-----------|
| [README.md](README.md) | Complete system documentation | 15 min |
| [QUICKSTART.md](QUICKSTART.md) | Get running in minutes | 5 min |
| [SETUP.md](SETUP.md) | Detailed setup & troubleshooting | 10 min |
| [SUMMARY.md](SUMMARY.md) | Project overview & metrics | 5 min |
| [This File] | Navigation & index | 5 min |

## 🏗️ Project Structure Overview

```
ai-startup-scout-agent/
│
├── 🎯 START HERE
│   ├── run.bat              ← Windows: Double-click to run
│   ├── run.sh               ← Mac/Linux: bash run.sh
│   └── app.py               ← Manual: streamlit run app.py
│
├── 📖 DOCUMENTATION
│   ├── README.md            ← Full documentation (start here)
│   ├── QUICKSTART.md        ← Quick reference
│   ├── SETUP.md             ← Installation & troubleshooting
│   ├── SUMMARY.md           ← Project overview
│   └── This file             ← Navigation guide
│
├── 🤖 CORE APPLICATION
│   ├── app.py               ← Streamlit web interface
│   ├── agent.py             ← Main orchestrator
│   └── requirements.txt      ← Dependencies
│
├── 🧠 AGENTS (Multi-Agent System)
│   ├── agents/
│   │   ├── planner_agent.py     ← Query analysis
│   │   ├── research_agent.py    ← Database search
│   │   ├── analysis_agent.py    ← AI analysis
│   │   ├── scoring_agent.py     ← Investment scoring
│   │   └── report_agent.py      ← Report generation
│   │
│   └── llm/
│       └── ollama_client.py     ← LLM integration
│
├── 📊 DATA
│   └── data/startups.csv    ← Startup database (20 entries)
│
└── 🧪 TESTING & DEMO
    ├── quicktest.py         ← Fast validation test
    ├── test_system.py       ← Full system test
    ├── demo.py              ← 5 example demos
    └── debug_query.py       ← Query debugging tool
```

## 🎯 Common Tasks

### "I want to run the web app"
```bash
streamlit run app.py
```
Then open http://localhost:8501

### "I want to see it work"
```bash
python quicktest.py        # Fast validation
python demo.py             # Full demo with examples
```

### "I want to install dependencies"
```bash
pip install -r requirements.txt
```

### "I want to understand the agents"
See: [agents/README.md](agents/) - Each agent explained

### "I want to add more startups"
Edit: [data/startups.csv](data/startups.csv)

### "I want to customize the scoring"
Edit: [agents/scoring_agent.py](agents/scoring_agent.py)

### "I want to change the UI"
Edit: [app.py](app.py)

## ✨ Key Features

### 🤖 Multi-Agent System
- Planner Agent (query understanding)
- Research Agent (database search)
- Analysis Agent (AI insights)
- Scoring Agent (investment scores)
- Report Agent (formatting)

### 🎨 Web Interface
- Clean Streamlit UI
- Real-time progress
- Interactive cards
- Export functionality

### 🧠 AI Integration
- Ollama support (optional)
- Intelligent fallbacks
- Works offline

### 📊 Data Pipeline
- Natural language parsing
- Flexible filtering
- Smart scoring
- Professional reports

## 🚀 Running the Application

### Option 1: Easiest (Windows)
Double-click: `run.bat`

### Option 2: Easy (Mac/Linux)
```bash
bash run.sh
```

### Option 3: Manual (All platforms)
```bash
streamlit run app.py
```

All open the app at: http://localhost:8501

## 🧪 Testing

```bash
# Quick validation (1 sec)
python quicktest.py

# Full system test (10 sec)
python test_system.py

# Run all 5 demos (5 min)
python demo.py

# Debug query parsing
python debug_query.py
```

## 🎓 Learning Paths

### Beginner: Just Want to Use It
1. Run `streamlit run app.py`
2. Try example queries
3. Explore results

📖 **Read**: [QUICKSTART.md](QUICKSTART.md)

### Intermediate: Understand the Code
1. Read [README.md](README.md)
2. Explore `agents/` directory
3. Run `python demo.py`
4. Examine `agent.py`

📖 **Read**: [SETUP.md](SETUP.md)

### Advanced: Modify & Extend
1. Study each agent in detail
2. Customize `scoring_agent.py`
3. Modify `app.py` styling
4. Add features in your own agents

📖 **Read**: Code comments and docstrings

## 💡 Example Queries to Try

```
"Find AI startups in Europe"
"Show top fintech opportunities"
"What about security companies globally"
"Find well-funded startup in the UK"
"Show promising automation startups"
```

## 🔒 System Characteristics

- ✅ **Local Processing** - Everything runs on your machine
- ✅ **No API Keys** - No external services needed
- ✅ **No Cloud** - 100% offline capable
- ✅ **No Tracking** - Complete privacy
- ✅ **Production Ready** - Clean, professional code

## 📊 What's Included

- 20 real, well-known startups
- 9 different sectors
- 7 geographic regions
- Smart filtering system
- Investment scoring formula
- AI-powered analysis (optional)
- Professional UI
- Complete documentation

## 🎁 Bonus Scripts

- `quicktest.py` - Validate system works
- `test_system.py` - Full test suite
- `demo.py` - Comprehensive examples
- `debug_query.py` - Query analysis tool

## 🚀 Next Steps

### Immediate
1. Choose your run method above
2. Start the application
3. Try a few searches

### Short-term
1. Read the documentation
2. Explore the code
3. Modify scoring/filtering

### Long-term
1. Add more startup data
2. Connect real APIs
3. Deploy as production app

## 📞 Getting Help

### For Setup Issues
→ See [SETUP.md](SETUP.md) "Troubleshooting" section

### For Understanding the System
→ See [README.md](README.md) "Architecture" section

### For Quick Start
→ See [QUICKSTART.md](QUICKSTART.md)

### For Code Explanation
→ Read docstrings in the `.py` files

## ✨ What You'll Learn

By exploring this project, you'll understand:
- ✅ Multi-agent AI architecture
- ✅ Streamlit web development
- ✅ Data processing pipelines
- ✅ LLM integration patterns
- ✅ Professional Python code structure
- ✅ API design principles

## 🎉 Ready to Start?

### Choose Your Path:

```
┌─────────────────────────────────────┬──────────────┬─────────┐
│ Path                                │ Time         │ Command │
├─────────────────────────────────────┼──────────────┼─────────┤
│ 1. Run the web app                  │ 5 min        │ See ⬇️  │
│ 2. Quick test                       │ 1 min        │ See ⬇️  │
│ 3. See full demo                    │ 5 min        │ See ⬇️  │
│ 4. Read documentation               │ 15 min       │ See ⬇️  │
│ 5. Customize the system             │ 30+ min      │ See ⬇️  │
└─────────────────────────────────────┴──────────────┴─────────┘
```

## 🚀 Quick Commands

```bash
# Run the web interface
streamlit run app.py

# Quick validation
python quicktest.py

# Full demo
python demo.py

# Check query parsing
python debug_query.py

# Install dependencies
pip install -r requirements.txt
```

## 📡 System Status

- ✅ All agent modules working
- ✅ Web interface operational
- ✅ Data pipeline functional
- ✅ Scoring algorithm tested
- ✅ LLM integration ready
- ✅ Documentation complete

## 🎊 Project Built Successfully!

**Everything is ready to use. Pick a command above and get started!**

---

### 🔗 Quick Links to Key Files

| Purpose | File |
|---------|------|
| Start here | [README.md](README.md) |
| Quick reference | [QUICKSTART.md](QUICKSTART.md) |
| Setup help | [SETUP.md](SETUP.md) |
| Run web app | [app.py](app.py) |
| Main logic | [agent.py](agent.py) |
| See demo | [demo.py](demo.py) |

---

**Built as a professional demonstration of multi-agent AI architecture**

🚀 **Let's discover some startups!** 🚀
