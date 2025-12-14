# Career Compass - AI-powered job matching system

AI-powered job matching system that intelligently connects candidates with opportunities using advanced ML models and workflow automation.

## Overview

Career Compass analyzes resumes, extracts skills, and matches candidates with relevant job opportunities using a combination of AI models, workflow orchestration, and intelligent decision-making.

## Features

- **Resume Analysis** - AI-powered skill extraction and profile assessment
- **Intelligent Matching** - Dynamic job matching based on skills and experience
- **Workflow Automation** - Automated pipeline orchestration
- **Real-time Dashboard** - Interactive interface for job discovery

## Tech Stack

- **Cline** - Autonomous coding workflows
- **Kestra** - Workflow orchestration with AI Agent
- **Oumi** - ML model training and inference
- **CodeRabbit** - Automated code quality reviews
- **Vercel** - Serverless deployment and hosting

## Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt
```

### Training Model
```bash
# Train the Oumi model
python3 train_model.py
```

### Start CLI
```bash
# Option 1: Use startup script
./start.sh

# Option 2: Manual start
conda activate hackathon  # if using conda
python3 compass_cli.py
```

### Deploy to Vercel
```bash
npx vercel --prod
```

## Project Structure

```
career-compass/
├── api/                  # Vercel serverless functions
│   ├── analyze.js       # Main integration endpoint
│   ├── kestra.js         # Kestra workflow execution
│   ├── oumi.js           # Model inference
│   ├── coderabbit.js     # Code quality status
│   └── technologies.js   # Technology status
├── compass_cli.py        # CLI interface
├── train_model.py        # Model training script
├── cline_workflow.js     # Cline autonomous workflows
├── index.html            # Web interface
├── kestra_flow.yaml      # Kestra workflow configuration
└── oumi_train.yaml       # Oumi training configuration
```

## API Endpoints

### `/api/analyze` - Combined Analysis (Main Endpoint)
**Method**: `POST`  
**Purpose**: Orchestrates all sponsor tools together

**Request**:
```json
{
  "resume_text": "Resume content here..."
}
```

**Response**:
```json
{
  "success": true,
  "integration": {
    "cline": { "skills_extracted": 5, "status": "active" },
    "oumi": { "confidence": 0.89, "profile_quality": "high" },
    "kestra": { "workflow_id": "career_compass_logic", "status": "triggered" },
    "coderabbit": { "active": true, "code_quality": "excellent" },
    "vercel": { "deployed": true, "region": "iad1" }
  },
  "matches": [...]
}
```

### `/api/kestra` - Workflow Execution
**Method**: `POST`  
Executes Kestra workflow (fetch data → AI analysis → log results)

### `/api/oumi` - Model Inference
**Method**: `POST`  
Analyzes job descriptions using trained Oumi model

### `/api/coderabbit` - Code Quality Status
**Method**: `GET`  
Returns CodeRabbit integration status and metrics

### `/api/technologies` - Technology Status
**Method**: `GET`  
Returns status of all integrated technologies

## Award Criteria Fulfillment

### ✅ Cline CLI Award
**Criterion**: Best project using Cline CLI for autonomous coding workflows

**Evidence**:
- `cline_workflow.js` with 4 autonomous workflows:
  - Code generation (`generate`)
  - Automated testing (`test`)
  - Code review (`review`)
  - Deployment (`deploy`)

### ✅ Kestra AI Agent Award
**Criterion**: Using Kestra's AI Agent to summarize data and make decisions

**Evidence**:
- `kestra_flow.yaml` implements:
  - Data summarization from multiple sources
  - Decision-making based on summarized data
  - Structured JSON output with recommendations

### ✅ Oumi Award
**Criterion**: Creative use of Oumi to train/evaluate LLMs and OSS contributions

**Evidence**:
- Trained custom model (`SmolLM2-135M-Instruct`) for job quality assessment
- Training config: `oumi_train.yaml`
- OSS contribution: `oumi_contribution.md` with reusable templates
- Model saved: `output/salary_model/`

### ✅ CodeRabbit Award
**Criterion**: Best open-source engineering with clean PRs and OSS workflows

**Evidence**:
- `.coderabbit.yaml` configuration
- `.github/PULL_REQUEST_TEMPLATE.md` for standardized PRs
- `.github/workflows/coderabbit.yml` for automated reviews
- `CONTRIBUTING.md` with OSS guidelines

## Security

### Environment Variables
Never commit API keys. Use `.env` file (excluded from git):

```bash
# Copy example file
cp .env.example .env

# Add your keys
GROQ_API_KEY=your_actual_key_here
```

### Protected Files
- `.env`, `.env.local`, `*.env` - Never commit
- `output/` - Large model files excluded
- `.venv/` - Virtual environment excluded

### Best Practices
- ✅ Use environment variables for all secrets
- ✅ Never hardcode API keys
- ✅ Rotate keys if accidentally exposed
- ✅ Use different keys for dev/prod

## Contributing

### Pull Request Process
1. Fork the repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes and ensure CodeRabbit passes
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open Pull Request

### CodeRabbit Integration
All PRs are automatically reviewed for:
- Code quality and best practices
- Security vulnerabilities
- Documentation completeness
- Performance optimizations

### Code Style
- Follow existing code style
- Add comments for complex logic
- Include docstrings for functions
- Update tests when fixing bugs

## Cline Workflows

### Code Generation
```bash
node cline_workflow.js generate "API endpoint, database model, tests"
```

### Automated Testing
```bash
node cline_workflow.js test .
```

### Code Review
```bash
node cline_workflow.js review src/api.js
```

### Deployment
```bash
node cline_workflow.js deploy . vercel
```

## Kestra Workflow

The `kestra_flow.yaml` defines a 3-task workflow:
1. **Fetch Data** - Retrieves job data from external sources
2. **AI Analysis** - Uses Groq AI to analyze and summarize data
3. **Log Result** - Outputs final results

## Oumi Model Training

### Configuration
- **Model**: SmolLM2-135M-Instruct
- **Task**: Job quality assessment and salary evaluation
- **Config**: `oumi_train.yaml`
- **Output**: `output/salary_model/`

### Training
```bash
python3 train_model.py
```

### OSS Contribution
See `oumi_contribution.md` for reusable configuration templates and best practices shared with the Oumi community.

## Deployment

### Vercel
```bash
npx vercel --prod
```

The `api/` directory contains Vercel Serverless Functions that automatically deploy as endpoints.

### Environment Variables (Vercel)
Set in Vercel dashboard:
- `GROQ_API_KEY` - For Kestra AI Agent workflows

## License

MIT

## Acknowledgments

- **WeMakeDevs** - Special thanks for offering this opportunity to work on the AI Agents Assemble 2025 hackathon
- **Cline** for autonomous code generation
- **Kestra** for workflow orchestration
- **Oumi** for custom model training
- **Vercel** for seamless deployment
- **CodeRabbit** for code quality assurance
