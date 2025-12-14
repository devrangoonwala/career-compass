#!/bin/bash

# Career Compass - Project Startup Script
# This script starts all components of the Career Compass project

echo "🚀 Starting Career Compass Project..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+"
    exit 1
fi

# Check Node.js (for Cline workflows)
if ! command -v node &> /dev/null; then
    echo "⚠️  Node.js not found. Cline workflows will not work."
    echo "   Install Node.js for full functionality."
fi

# Activate conda environment if available
if command -v conda &> /dev/null; then
    echo "📦 Activating conda environment 'hackathon'..."
    conda activate hackathon 2>/dev/null || echo "   (hackathon environment not found, using system Python)"
fi

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip3 install -r requirements.txt --quiet

# Install Node dependencies if package.json exists
if [ -f "package.json" ]; then
    echo "📥 Installing Node.js dependencies..."
    npm install --silent 2>/dev/null || echo "   (npm install skipped)"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Available commands:"
echo "  1. python3 compass_cli.py          - Start CLI interface"
echo "  2. python3 train_model.py           - Train the model"
echo "  3. node cline_workflow.js generate  - Run Cline workflow"
echo "  4. npx vercel --prod                - Deploy to Vercel"
echo ""
echo "Starting CLI..."
echo ""

python3 compass_cli.py

