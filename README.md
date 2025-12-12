# Career Compass: AI-Powered Job Filtering & Analysis

Career Compass is an innovative project designed to streamline the job application process by leveraging AI and automation. It allows users to upload their resumes (PDF, DOCX, or TXT) and receive instant, intelligent analysis, job matching, and workflow orchestration.

## Features

- **AI-Powered Skill Extraction (Cline):** Automatically identifies key skills from your resume.
- **Oumi Inference Engine Integration:** Performs in-depth model analysis on your resume to assess job fit and confidence.
- **Kestra Workflow Orchestration:** Manages a pipeline of tasks, including data fetching, AI analysis, and result logging.
- **CodeRabbit Code Quality Checks:** Ensures high code quality throughout the project.
- **Vercel API Endpoints:** Provides seamless integration for all backend services and external APIs.
- **Interactive Web Interface:** A user-friendly drag-and-drop interface for resume uploads and result visualization.

## Project Structure

```
.github/
├── workflows/           # GitHub Actions workflows
├── PULL_REQUEST_TEMPLATE.md
.env.example             # Example environment variables
.gitignore               # Files ignored by Git
.vercelignore             # Files ignored by Vercel deployments
AWARD_CRITERIA.md        # Criteria for project awards (if applicable)
cline_workflow.js        # Cline (AI) related workflow logic
compass_cli.py           # Command-line interface for Career Compass
CONTRIBUTING.md          # Guidelines for contributions
index.html               # Main web application interface
kestra_flow.yaml         # Kestra workflow definition
oumi_contribution.md     # Oumi (AI) related contribution guidelines
oumi_train.yaml          # Oumi (AI) training configurations
package.json             # Node.js project dependencies
README.md                # Project README file
requirements.txt         # Python project dependencies
resume.txt               # Example resume file
salary_data.csv          # Sample salary data for analysis
salary_data.txt          # Sample salary data for analysis
SECURITY.md              # Security guidelines
train_model.py           # Script for training AI models
api/
├── analyze.js           # API endpoint for combined analysis
├── coderabbit.js        # API endpoint for CodeRabbit integration
├── kestra.js            # API endpoint for Kestra integration
└── oumi.js              # API endpoint for Oumi integration
mlruns/                  # MLflow experiment tracking data
oumi-training/           # Oumi model training resources
output/                  # Output directory
wandb/                   # Weights & Biases experiment tracking data
```

## Setup Instructions

### Prerequisites

- Git
- Node.js (for frontend and API endpoints)
- Python 3.x (for AI/ML components)
- `npm` or `yarn` (for Node.js package management)
- `pip` (for Python package management)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/devrangoonwala/career-compass.git
   cd career-compass
   ```

2. **Install Node.js dependencies:**

   ```bash
   npm install
   # or yarn install
   ```

3. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**

   Copy `.env.example` to `.env` and fill in any required API keys (e.g., Groq API key for AI inference) and other configurations. **Do not commit your `.env` file to version control.**

   ```bash
   cp .env.example .env
   ```

## Usage

1. **Start the development server:**

   This project is designed to be deployed on Vercel, but you can run the API endpoints locally using Node.js:

   ```bash
   npm run start
   ```

   For the full experience, it is recommended to deploy to Vercel.

2. **Open `index.html` in your browser:**

   The main application interface is `index.html`. You can open it directly in your web browser to start using Career Compass.

3. **Upload your Resume:**

   Drag and drop your resume (PDF, DOCX, or TXT) into the designated area on the web interface. The system will automatically process and analyze your resume.

4. **Review Job Matches:**

   After analysis, the dashboard will display top job matches and relevant insights based on your skills and the AI's assessment.

## Contributing

We welcome contributions to Career Compass! Please refer to `CONTRIBUTING.md` for guidelines on how to contribute.

## Security

For information on security practices and how to report vulnerabilities, please see `SECURITY.md`.

## License

This project is licensed under the [MIT License](LICENSE).
