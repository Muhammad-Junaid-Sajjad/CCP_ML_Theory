#!/bin/bash
# CKD Prediction System - Setup Script
# This script sets up the entire project environment

set -e  # Exit on error

echo "🚀 CKD Prediction System - Setup"
echo "=================================="
echo ""

# Check Python version
echo "📌 Checking Python version..."
python3 --version || { echo "❌ Python 3 not found. Please install Python 3.8+"; exit 1; }

# Create virtual environment
echo "📦 Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip --quiet

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Train models: ./scripts/train.sh"
echo "  2. Run server: ./scripts/run.sh"
echo "  3. Or use quick start: ./scripts/quickstart.sh"
echo ""
