# Career Compass

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

```bash
# Install dependencies
pip install -r requirements.txt

# Train model
python3 train_model.py

# Start CLI
python3 compass_cli.py

# Deploy
npx vercel --prod
```

## Project Structure

```
career-compass/
├── api/              # Vercel serverless functions
├── compass_cli.py    # CLI interface
├── train_model.py    # Model training
├── index.html        # Web interface
└── kestra_flow.yaml  # Workflow configuration
```

## API Endpoints

- `/api/analyze` - Combined analysis using all tools
- `/api/kestra` - Workflow execution
- `/api/oumi` - Model inference
- `/api/coderabbit` - Code quality status

## Documentation

- [API Documentation](./API_DOCUMENTATION.md)
- [Award Criteria](./AWARD_CRITERIA.md)
- [Contributing](./CONTRIBUTING.md)

## License

MIT
