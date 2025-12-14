# Quick Start Guide - Career Compass

## 🚀 Starting the Project

### Option 1: Use Startup Script (Recommended)
```bash
./start.sh
```

### Option 2: Manual Start
```bash
# Activate conda environment (if using)
conda activate hackathon

# Start CLI
python3 compass_cli.py
```

## 📋 Available Commands

### 1. Train the Model
```bash
python3 train_model.py
```

### 2. Run Cline Workflows
```bash
# Generate code
node cline_workflow.js generate "API endpoint, tests"

# Run tests
node cline_workflow.js test .

# Review code
node cline_workflow.js review src/api.js

# Deploy
node cline_workflow.js deploy . vercel
```

### 3. Deploy to Vercel
```bash
npx vercel --prod
```

## 🏆 Award Criteria Status

✅ **All 4 award criteria are fulfilled:**

1. ✅ **Cline CLI**: Autonomous workflows in `cline_workflow.js`
2. ✅ **Kestra AI Agent**: Data summarization + decision-making in `kestra_flow.yaml`
3. ✅ **Oumi**: Training config + OSS contribution documented
4. ✅ **CodeRabbit**: PR templates + OSS workflows configured

## 📁 Key Files

- `compass_cli.py` - Main CLI interface
- `cline_workflow.js` - Cline autonomous workflows
- `kestra_flow.yaml` - Kestra AI Agent workflow
- `train_model.py` - Model training script
- `index.html` - Web interface
- `api/` - Vercel serverless functions

## 🔗 Production URL

https://career-compass-201jgw7uy-devrangoonwalas-projects.vercel.app

## 📚 Documentation

- `README.md` - Full project documentation
- `AWARD_CRITERIA.md` - Detailed award fulfillment
- `CONTRIBUTING.md` - OSS contribution guidelines
- `oumi_contribution.md` - Oumi community contribution

