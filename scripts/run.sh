#!/bin/bash
# CKD Prediction System - Server Script
# Starts the Flask web application

set -e

echo "🌐 Starting CKD Prediction Server"
echo "=================================="
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first"
    exit 1
fi

# Check if models exist
if [ ! -d "models" ] || [ ! -f "models/best_model.pkl" ]; then
    echo "❌ Models not found. Run ./scripts/train.sh first"
    exit 1
fi

echo "✅ Models loaded successfully"
echo "🚀 Starting Flask server..."
echo ""
echo "Server will be available at:"
echo "  🔗 http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start Flask server
python app.py
