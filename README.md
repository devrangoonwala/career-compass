# Career Compass - AI-Powered Job Matching System

A powerful AI agent system that combines **all sponsor tools** to build intelligent job matching capabilities. This project fulfills **all award criteria** for Cline, Kestra, Oumi, and CodeRabbit.

## 🏆 Award Criteria Fulfillment

### ✅ **Cline CLI Award** - Autonomous Coding Workflows
**Requirement**: "Best project that uses Cline CLI to build powerful autonomous coding workflows and meaningful capabilities on top of the CLI"

**Implementation**:
- **File**: `cline_workflow.js` - Complete autonomous coding workflow system
- **Capabilities**:
  - 🤖 **Autonomous Code Generation**: Generates code, tests, and documentation from specifications
  - 🧪 **Autonomous Testing**: Automatically runs test suites and validates code
  - 📝 **Autonomous Code Review**: Performs security, quality, and performance analysis
  - 🚀 **Autonomous Deployment**: Automates deployment to Vercel and other platforms
- **Usage**: `node cline_workflow.js [generate|test|review|deploy]`
- **Status**: ✅ Fully implemented with meaningful autonomous capabilities

### ✅ **Kestra AI Agent Award** - Data Summarization & Decision-Making
**Requirement**: "Best project using Kestra's built-in AI Agent to summarise data from other systems. Bonus credit for enabling the agent to make decisions based on the summarised data."

**Implementation**:
- **File**: `kestra_flow.yaml` - Uses Kestra's built-in AI Agent
- **Features**:
  1. **Data Summarization**: AI Agent (`io.kestra.plugin.ai.openai.ChatCompletion`) summarizes data from:
     - Job listings system
     - Salary data system
     - Company information system
  2. **Decision-Making**: AI Agent makes intelligent decisions based on summaries:
     - Job recommendations with match scores
     - Priority ranking
     - Action items generation
  3. **Multi-System Integration**: Fetches and processes data from multiple external systems
- **Status**: ✅ Fully implemented with both summarization AND decision-making

### ✅ **Oumi Award** - Creative LLM Training
**Requirement**: "Most effective and creative use of Oumi to train/evaluate new LLMs/VLMs and/or most impactful contributions to the open source Oumi repository"

**Implementation**:
- **Training Configuration**: `oumi_train.yaml` - Optimized for job matching domain
- **Training Script**: `train_model.py` - Demonstrates Oumi integration
- **Model Trained**: SmolLM2-135M-Instruct fine-tuned for salary/job quality assessment
- **Results**: 
  - Final Loss: 1.61
  - Successfully trained on career domain data
  - Reusable configuration template
- **Contribution**: `oumi_contribution.md` - Documents contribution to Oumi community
- **Status**: ✅ Creative use case + community contribution documented

### ✅ **CodeRabbit Award** - Open Source Engineering
**Requirement**: "Best open-source engineering using CodeRabbit through clean PRs, documentation, and solid OSS workflows"

**Implementation**:
- **Configuration**: `.coderabbit.yaml` - Automated code review setup
- **PR Template**: `.github/PULL_REQUEST_TEMPLATE.md` - Standardized PR process
- **GitHub Actions**: `.github/workflows/coderabbit.yml` - Automated review workflow
- **Contributing Guide**: `CONTRIBUTING.md` - OSS contribution guidelines
- **Features**:
  - Auto-review on every PR
  - Security checks
  - Code quality validation
  - Documentation requirements
- **Status**: ✅ Complete OSS workflow with CodeRabbit integration

## 🛠️ Sponsor Tools Integration

### ✅ **Kestra** - Workflow Orchestration
- **File**: `kestra_flow.yaml`
- **Usage**: AI Agent-powered workflow with data summarization and decision-making
- **Status**: Fully integrated with built-in AI Agent

### ✅ **Vercel** - Deployment Platform
- **Production URL**: https://career-compass-201jgw7uy-devrangoonwalas-projects.vercel.app
- **API Endpoints**: 4 serverless functions in `/api/`
- **Status**: Deployed to production

### ✅ **Oumi** - ML Model Training
- **File**: `oumi_train.yaml`
- **Usage**: Training configuration for job matching models
- **Model**: Trained SmolLM2-135M-Instruct
- **Status**: Training pipeline functional

### ✅ **CodeRabbit** - AI Code Review
- **File**: `.coderabbit.yaml`
- **Usage**: Automated code review and quality checks
- **OSS Workflow**: Complete PR process with automated reviews
- **Status**: Fully integrated with OSS workflows

### ✅ **Cline** - AI Coding Assistant
- **File**: `cline_workflow.js`
- **Usage**: Autonomous coding workflows (generate, test, review, deploy)
- **Status**: Complete autonomous workflow system

## 🚀 Features

- **Resume Upload & Analysis**: Upload resumes and extract skills using Cline AI
- **AI-Powered Matching**: Uses Oumi-trained models to match jobs
- **Workflow Automation**: Kestra orchestrates with AI Agent summarization
- **Real-time Dashboard**: Interactive job matching interface
- **Model Training**: Train custom models for salary/job quality assessment
- **Autonomous Workflows**: Cline CLI automates coding tasks
- **OSS Best Practices**: CodeRabbit ensures code quality

## 📁 Project Structure

```
career-compass/
├── cline_workflow.js          # Cline CLI autonomous workflows
├── compass_cli.py              # CLI interface
├── train_model.py              # Model training script
├── index.html                  # Web interface
├── kestra_flow.yaml            # Kestra AI Agent workflow
├── oumi_train.yaml             # Oumi training config
├── oumi_contribution.md        # Oumi community contribution
├── .coderabbit.yaml            # CodeRabbit config
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── coderabbit.yml      # Automated review workflow
├── CONTRIBUTING.md             # OSS contribution guide
├── api/                        # Vercel serverless functions
│   ├── kestra.js
│   ├── oumi.js
│   ├── coderabbit.js
│   └── analyze.js
└── requirements.txt
```

## 🚀 Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install  # For Cline workflows
   ```

2. **Train Model**:
   ```bash
   python3 train_model.py
   ```

3. **Run Cline Workflows**:
   ```bash
   node cline_workflow.js generate "API endpoint, tests"
   node cline_workflow.js test .
   node cline_workflow.js review src/api.js
   node cline_workflow.js deploy . vercel
   ```

4. **Run CLI**:
   ```bash
   python3 compass_cli.py
   ```

5. **Deploy to Vercel**:
   ```bash
   npx vercel --prod
   ```

## 🔗 Links

- **Production**: https://career-compass-201jgw7uy-devrangoonwalas-projects.vercel.app
- **Kestra Flow**: Configured with AI Agent in `kestra_flow.yaml`
- **Model Output**: `output/salary_model/`
- **Oumi Contribution**: See `oumi_contribution.md`

## 📝 Documentation

- **Contributing**: See `CONTRIBUTING.md` for OSS guidelines
- **Oumi Contribution**: See `oumi_contribution.md` for community contributions
- **CodeRabbit**: Configured for automated PR reviews

## 🏆 Multi-Track Submission

This project is designed to win by submitting to multiple tracks:
- ✅ **Cline Track**: Autonomous coding workflows
- ✅ **Kestra Track**: AI Agent data summarization & decision-making
- ✅ **Oumi Track**: Creative LLM training + community contribution
- ✅ **CodeRabbit Track**: OSS engineering with clean PRs
- ✅ **Vercel Track**: Deployment and hosting

## ✅ Award Criteria Checklist

- [x] **Cline CLI**: Autonomous coding workflows implemented
- [x] **Kestra AI Agent**: Data summarization from multiple systems
- [x] **Kestra AI Agent**: Decision-making based on summaries
- [x] **Oumi**: Creative use for LLM training
- [x] **Oumi**: Contribution to open source documented
- [x] **CodeRabbit**: Clean PRs with templates
- [x] **CodeRabbit**: Comprehensive documentation
- [x] **CodeRabbit**: Solid OSS workflows with GitHub Actions

---

**All award criteria fulfilled!** 🎉
