#!/bin/bash
# Launch script for AI Startup Scouting Agent
# Usage: ./run.sh

echo "========================================"
echo "  AI Startup Scouting Agent"
echo "========================================"
echo ""
echo "Starting web interface..."
echo ""

# Check if venv exists
if [ ! -f "venv/bin/python" ]; then
    echo "Error: Virtual environment not found."
    echo "Please run: pip install -r requirements.txt"
    exit 1
fi

# Launch Streamlit
./venv/bin/python -m streamlit run app.py
