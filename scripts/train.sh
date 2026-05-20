#!/bin/bash
# CKD Prediction System - Training Script
# Trains all 5 ensemble models and generates visualizations

set -e

echo "🎯 Training CKD Prediction Models"
echo "=================================="
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run ./scripts/setup.sh first"
    exit 1
fi

# Check if dataset exists
if [ ! -f "kidney_disease.csv" ]; then
    echo "❌ Dataset not found: kidney_disease.csv"
    exit 1
fi

echo "📊 Starting model training..."
echo "This will take approximately 45-60 seconds..."
echo ""

# Run training pipeline
python ckd_pipeline.py

echo ""
echo "✅ Training complete!"
echo ""
echo "Generated files:"
echo "  📁 models/ - 12 trained model files (5.0 MB)"
echo "  📁 static/plots/ - 10 visualization files (976 KB)"
echo "  📄 results_summary.json - Performance metrics"
echo ""
echo "Next step: Run server with ./scripts/run.sh"
echo ""
