# 🧭 Career Compass: The Autonomous Job Agent

**"I stopped searching for jobs. I built a robot to do it for me."**

Career Compass is an intelligent multi-agent system that automates the job hunt. Instead of scrolling through thousands of generic listings, you simply drag-and-drop your resume, and the agent orchestrates a complex pipeline to find, filter, and rank jobs that match your specific skills and salary expectations.

---

## 🎥 Demo Video

> 📹 *[Watch the 2-minute walkthrough](YOUR_VIDEO_LINK_HERE)*

---

## 🏗️ The "Avengers" Tech Stack

This project isn't just a script; it's a complete ecosystem built using 5 cutting-edge AI technologies.

| Technology | Role | The "Why" |
|------------|------|-----------|
| 🟣 **Cline** | The Architect | Built the entire CLI automation tool (`compass_cli.py`) and the frontend logic using autonomous coding agents. |
| 🟢 **Kestra** | The Manager | Orchestrates the daily data pipeline. It wakes up, fetches raw job data, and pipes it to the AI analysis layer. |
| 🔴 **Oumi** | The Judge | A custom Fine-Tuned Model (LLM) trained on my specific salary/culture preferences to "grade" job descriptions. |
| 🔵 **Vercel** | The Face | Hosts the "Apple-style" minimalist dashboard, ensuring the tool is accessible from any device. |
| 🟡 **CodeRabbit** | The Auditor | Automatically reviewed every Pull Request to ensure security best practices and clean code. |

---

## 🧠 How It Works (The Architecture)

```
[Resume Input] → [Together AI Extraction] → [Kestra Orchestrator] → [Oumi "Verdict" Model] → [Vercel Dashboard]
```

1. **Ingestion**: The user drags a `resume.txt` or `.pdf` into the web interface.
2. **Extraction**: An AI agent parses the unstructured text to extract key skills (e.g., "Python", "React").
3. **Orchestration**: Kestra triggers the workflow, simulating a fetch of live job data from external sources.
4. **Judgment**: The data is passed to a custom Oumi-trained model. This model doesn't just look for keywords; it looks for **fit**. (e.g., "Is this salary >$150k? Is it Remote?").
5. **Presentation**: The filtered, high-quality matches are displayed on the Vercel dashboard.
6. **Action**: Clicking "Apply" instantly generates a deep-link search for the specific application page.

---

## ⚡ Features

### 1. Resume-Aware Search
Drop your resume, and the system dynamically updates its search criteria. No more manual filter setting.

### 2. The "Oumi Verdict"
Most job sites give you "Matches." Career Compass gives you a **Verdict**. We trained a custom model to classify jobs as **GOOD** or **BAD** based on nuanced criteria like "unpaid overtime" or "vague salary ranges."

### 3. Command Center CLI
Includes a custom-built CLI tool (`compass_cli.py`) for managing the agent backend:
- **Option 1**: Verifies Oumi training artifacts.
- **Option 2**: Manually triggers Kestra workflows.
- **Option 3**: Checks system health status.

---

## 🛠️ Installation & Setup

Want to run the backend yourself? Follow these steps.

### Prerequisites
- Docker (for Kestra)
- Python 3.10+
- Node.js (for Vercel)

### 1. Start the Orchestrator (Kestra)

```bash
docker run --pull=always --rm -it -p 8080:8080 --user=root \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp:/tmp kestra/kestra:latest server local
```

Access the UI at `http://localhost:8080`

### 2. Verify the AI Brain (CLI)

```bash
# Activate env
conda activate hackathon

# Run the Command Center
python compass_cli.py
```

### 3. Deploy the Frontend

```bash
npx vercel --prod
```

---

## 🏆 Hackathon Tracks & Eligibility

This project was built specifically for **AI Agents Assemble 2024**.

- [x] **Infinity Build (Cline)**: Used Cline to generate the `compass_cli.py` tool and complex frontend logic.
- [x] **Wakanda Data (Kestra)**: Implemented `kestra_flow.yaml` to fetch and summarize job data using Llama-3 (via Groq).
- [x] **Iron Intelligence (Oumi)**: Trained a custom text-classification model (`output/salary_model`) to judge job quality.
- [x] **Stormbreaker (Vercel)**: Deployed a production-ready, responsive web app.
- [x] **Captain Code (CodeRabbit)**: Repository includes `.coderabbit.yaml` and active PR reviews.

---

## 📁 Project Structure

```
career-compass/
├── compass_cli.py          # CLI tool for managing backend
├── kestra_flow.yaml        # Kestra workflow definition
├── output/
│   └── salary_model/       # Custom Oumi fine-tuned model
├── frontend/               # Vercel-hosted web dashboard
├── .coderabbit.yaml        # CodeRabbit configuration
└── README.md               # You are here!
```

---

## 🚀 Usage

### Running the Full Pipeline

1. **Start Kestra** (see Installation step 1)
2. **Upload your resume** to the web interface
3. **Watch the magic happen** as jobs are fetched, analyzed, and filtered
4. **Review your matches** on the dashboard

### Using the CLI

```bash
python compass_cli.py
```

Follow the interactive prompts to:
- Verify model training status
- Trigger workflows manually
- Check system health

---

## 🤝 Contributing

This project is open-source. Code quality is enforced by **CodeRabbit**.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a PR (and watch CodeRabbit review it automatically!)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Cline** for autonomous code generation
- **Kestra** for workflow orchestration
- **Oumi** for custom model training
- **Vercel** for seamless deployment
- **CodeRabbit** for code quality assurance

---

## 📧 Contact

Built with ☕ and 🤖 by **[Your Name]**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

⭐ **If this project helped you, please give it a star!** ⭐
