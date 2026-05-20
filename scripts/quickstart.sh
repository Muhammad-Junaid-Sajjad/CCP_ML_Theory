#!/bin/bash
# CKD Prediction System - Quick Start
# One command to set up, train, and run everything!

set -e

echo "⚡ CKD Prediction System - Quick Start"
echo "======================================"
echo ""
echo "This will:"
echo "  1. Set up virtual environment"
echo "  2. Install dependencies"
echo "  3. Train all 5 ensemble models"
echo "  4. Start the web server"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 1
fi

# Step 1: Setup
echo ""
echo "📦 Step 1/3: Setting up environment..."
./scripts/setup.sh

# Step 2: Train models
echo ""
echo "🎯 Step 2/3: Training models..."
./scripts/train.sh

# Step 3: Start server
echo ""
echo "🌐 Step 3/3: Starting server..."
echo ""
./scripts/run.sh
