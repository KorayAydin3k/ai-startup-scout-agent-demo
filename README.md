# 🚀 AI Startup Scouting Agent

A sophisticated multi-agent AI system for discovering and analyzing promising startups using local LLM integration.

## 🌟 Features

- **Multi-Agent Architecture**: 5 specialized AI agents working together
  - 📋 **Planner Agent**: Analyzes user queries and extracts search parameters
  - 🔍 **Research Agent**: Searches and filters startup database
  - 🤖 **Analysis Agent**: Provides AI-powered insights using Ollama
  - 📊 **Scoring Agent**: Calculates investment scores using weighted metrics
  - 📑 **Report Agent**: Generates comprehensive investment reports

- **Local AI Integration**: Uses Ollama for privacy-preserving, local LLM analysis
- **Modern Web Interface**: Streamlit-based UI with professional design
- **Intelligent Query Processing**: Supports natural language queries for sectors and regions
- **Investment Scoring**: Weighted formula combining growth, funding, and team size
- **Fast Fallback**: 1-second timeout ensures responsive user experience

## 🛠️ Technology Stack

- **Backend**: Python 3.8+
- **AI**: Ollama (local LLM integration)
- **Web UI**: Streamlit
- **Data Processing**: Pandas
- **Environment**: Virtual environment support

## 📊 Scoring Formula

```
Investment Score = (Growth × 0.5) + (Funding × 0.3) + (Employees × 0.2)
```

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed
2. **Ollama** installed and running locally
3. **Git** for version control

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-startup-scout-agent.git
   cd ai-startup-scout-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama** (in another terminal)
   ```bash
   ollama serve
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📝 Usage Examples

### Natural Language Queries
- "Find promising AI startups in Europe"
- "Show me fintech companies in the US"
- "Best healthcare startups in Asia"
- "AI companies in Italy"

### Supported Sectors
- AI, Security, Automation, Fintech, Biotech, Climate, Web3

### Supported Regions
- Europe, US, Asia, and specific countries (Italy, UK, France, Germany, etc.)

## 🏗️ Project Structure

```
ai-startup-scout-agent/
├── app.py                 # Streamlit web interface
├── agent.py              # Main orchestrator class
├── requirements.txt      # Python dependencies
├── data/
│   └── startups.csv      # Startup database
├── agents/
│   ├── planner_agent.py  # Query analysis
│   ├── research_agent.py # Database filtering
│   ├── analysis_agent.py # AI insights
│   ├── scoring_agent.py  # Investment scoring
│   └── report_agent.py   # Report generation
├── llm/
│   └── ollama_client.py  # Local LLM client
└── README.md
```

## 🤖 Agent Architecture

```
User Query → Planner → Research → Analysis → Scoring → Report → UI
```

Each agent specializes in one aspect of the startup discovery process, ensuring comprehensive and accurate results.

## 📈 Sample Output

For query: "Find AI startups in Italy"

**Results:**
1. **Musixmatch** (Italy) - Score: 1.28/5.0
   - AI sector, $150M funding, 200 employees
   - Founded 2010, strong growth trajectory

2. **Reply** (Italy) - Score: 0.95/5.0
   - AI sector, $80M funding, 150 employees
   - Founded 2012, emerging player

## 🔧 Configuration

### Ollama Models
The system uses Ollama's default model. For best results, ensure you have a capable model like:
- llama2:7b
- mistral:7b
- codellama:7b

### Timeout Settings
Analysis requests timeout after 1 second for responsive UX.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify.

## 🙏 Acknowledgments

- Built with Streamlit for the web interface
- Powered by Ollama for local AI capabilities
- Inspired by modern AI agent architectures

---

**AI Startup Scouting Agent** - Discover the next unicorn with AI-powered analysis! 🚀
- **Score** investments using a weighted formula
- **Report** findings in a professional format

## 🏗️ Architecture

### Multi-Agent System

The system consists of 5 specialized agents:

1. **Planner Agent** 📋
   - Analyzes user queries to extract sector and region filters
   - Creates search strategy based on input
   - Maps natural language to structured parameters

2. **Research Agent** 🔍
   - Searches and filters startup database
   - Handles sector and geographic filtering
   - Returns sorted results by growth potential

3. **Analysis Agent** 🤖
   - Generates AI-powered investment insights
   - Uses Ollama (local LLM) integration
   - Provides contextual analysis for each startup

4. **Scoring Agent** 📊
   - Calculates investment scores using formula:
     ```
     Score = (Growth×0.5 + Funding×0.3 + Employees×0.2) / 100
     ```
   - Normalizes scores to 0-5.0 scale
   - Ranks startups by investment potential

5. **Report Agent** 📑
   - Generates comprehensive investment reports
   - Provides recommendations with confidence levels
   - Exports structured and human-readable formats

## 💻 Tech Stack

- **Python 3.8+** - Core language
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Ollama** - Local LLM integration (optional)
- **Requests** - HTTP client for Ollama

## 📋 Project Structure

```
ai-startup-scout-agent/
├── app.py                          # Streamlit web interface
├── agent.py                        # Main orchestrator
├── requirements.txt                # Python dependencies
│
├── agents/                         # Agent modules
│   ├── __init__.py
│   ├── planner_agent.py           # Query planning
│   ├── research_agent.py          # Database search
│   ├── analysis_agent.py          # AI analysis
│   ├── scoring_agent.py           # Investment scoring
│   └── report_agent.py            # Report generation
│
├── llm/                           # LLM integration
│   ├── __init__.py
│   └── ollama_client.py           # Ollama client
│
└── data/                          # Datasets
    └── startups.csv               # Startup database
```

## 📊 Dataset

The system includes a curated dataset of 20 real startups across multiple sectors:

**Sectors:**
- AI & Machine Learning
- Security
- Fintech
- Design & Productivity
- Hardware
- HR & Automation
- Communication

**Features:**
- Company name
- Industry sector
- Country
- Funding (millions USD)
- Employee count
- Growth score (0-100)
- Founded year

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project:**
   ```bash
   cd ai-startup-scout-agent
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the Streamlit web interface:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💡 Usage

1. **Enter a search query** in the input field:
   - "Find promising AI startups in Europe"
   - "Show me Security companies in the UK"
   - "What are the best fintech opportunities globally?"

2. **Click "Run Agent"** to start the analysis

3. **Watch the agent think** through all 5 steps:
   - Step 1: Understanding your query
   - Step 2: Searching the database
   - Step 3: Analyzing startups with AI
   - Step 4: Calculating investment scores
   - Step 5: Generating your report

4. **Review the recommendations** including:
   - Investment scores (0-5.0)
   - AI-generated insights
   - Recommendation levels
   - Company metrics

## 🤖 LLM Integration

### Using Ollama (Local LLM)

The system can use Ollama for AI-powered analysis. To enable advanced AI insights:

1. **Download Ollama** from https://ollama.ai

2. **Install a model:**
   ```bash
   ollama pull mistral  # or llama2, neural-chat, etc.
   ```

3. **Start Ollama server:**
   ```bash
   ollama serve
   ```

4. **Run the app** - it will automatically use Ollama if available

### Fallback Mode

If Ollama is not installed or running, the system automatically uses intelligent fallback responses based on startup metrics. The application works perfectly without Ollama for demonstration purposes.

## 📈 Scoring Formula

The investment score is calculated as:

```
Score = [(Growth_Score × 0.5) + (Funding_Million × 0.3) + (Employees × 0.2)] / 100
```

**Weights:**
- Growth Score: 50% - Most important growth indicator
- Funding: 30% - Capital available for scaling
- Employees: 20% - Team strength indicator

**Recommendation Levels:**
- ⭐⭐⭐ Strong Buy: Score ≥ 4.0
- ⭐⭐ Buy: Score ≥ 3.0
- ⭐ Interesting: Score ≥ 2.0
- Monitor: Score < 2.0

## 🎯 Example Queries

Try these queries to explore the system:

- "Find AI startups in Europe"
- "Show top fintech opportunities"
- "Find well-funded startups globally"
- "What security companies are promising?"
- "Find startups in the UK"

## 📝 Code Quality

The codebase features:

✅ **Modular Design** - Each agent is independent and reusable
✅ **Type Hints** - Full Python type annotations
✅ **Documentation** - Comprehensive docstrings
✅ **Error Handling** - Graceful fallbacks and error management
✅ **Clean Architecture** - Separation of concerns
✅ **Professional Code** - Production-ready quality

## 🔄 Agent Workflow

```
User Query
    ↓
Planner Agent (Extract intent, sectors, regions)
    ↓
Research Agent (Filter startups by criteria)
    ↓
Analysis Agent (Generate AI insights)
    ↓
Scoring Agent (Calculate investment scores)
    ↓
Report Agent (Format and present results)
    ↓
Investment Recommendations
```

## 🎨 User Interface

The Streamlit interface provides:

- **Clean, professional design** - Modern UI with agent visualization
- **Real-time progress** - See each agent working step-by-step
- **Interactive results** - Detailed startup cards with metrics
- **Export options** - Download reports as text files
- **Responsive layout** - Works on desktop and tablet

## 🧪 Testing the System

Run a quick test without Ollama:

```bash
python agent.py  # Or run app.py and use the interface
```

## 📚 Key Files

### Core Orchestrator
- **agent.py** - `StartupScoutAgent` class orchestrates the pipeline

### Agent Implementations
- **agents/planner_agent.py** - Query analysis and planning
- **agents/research_agent.py** - Database search and filtering
- **agents/analysis_agent.py** - AI-powered analysis
- **agents/scoring_agent.py** - Investment score calculation
- **agents/report_agent.py** - Report generation

### UI & Integration
- **app.py** - Streamlit web interface
- **llm/ollama_client.py** - Local LLM integration

## 🚀 Performance

- Query execution: ~3-5 seconds
- Supports up to 20+ startups in dataset
- Easily scalable to larger datasets
- Streaming progress updates for better UX

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to extend this system with:

- Additional startup datasets
- More sophisticated scoring algorithms
- Export to CSV/Excel functionality
- Email report delivery
- Real startup API integration
- Advanced filtering options

## 🔮 Future Enhancements

Potential improvements:

- [ ] Real startup data integration (Crunchbase API)
- [ ] User portfolio tracking
- [ ] Comparative analysis reports
- [ ] Risk assessment scoring
- [ ] Market trend analysis
- [ ] Notification system
- [ ] Database persistence
- [ ] Multi-user support

## 📞 Support

For issues or questions, refer to the code documentation. Each module includes detailed docstrings explaining functionality.

---

**Built with ❤️ as a professional AI agent system demonstration**
