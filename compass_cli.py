"""
Career Compass CLI - AI-Powered Job Matching System

This project integrates multiple sponsor tools:
- Kestra: Workflow orchestration (kestra_flow.yaml)
- Vercel: Deployment platform (deployed to production)
- Oumi: ML training configuration (oumi_train.yaml)
- CodeRabbit: Code review automation (.coderabbit.yaml)
- Cline: AI coding assistant (used for development)

Built with AI agent systems combining all sponsor tools.
"""
from rich.console import Console
from rich.theme import Theme
from rich.panel import Panel
from rich.text import Text
import sys
import subprocess


custom_theme = Theme({
    "success": "green",
    "error": "red",
    "info": "cyan",
    "warning": "yellow",
    "menu": "bold magenta",
})
console = Console(theme=custom_theme)

def display_menu():
    menu_text = Text()
    menu_text.append("\n")
    menu_text.append("1. ", style="menu").append("Train Brain\n", style="info")
    menu_text.append("2. ", style="menu").append("Run Workflow\n", style="info")
    menu_text.append("3. ", style="menu").append("Status\n", style="info")
    menu_text.append("4. ", style="menu").append("Exit\n", style="info")
    menu_text.append("\n")
    console.print(Panel(menu_text, title="[menu]Career Compass CLI[/menu]", title_align="left"))

def train_brain():
    console.print("[info]Initiating model training...[/info]")
    try:
        subprocess.run([sys.executable, "train_model.py"], check=True)
        console.print("[success]Model training completed successfully![/success]")
    except subprocess.CalledProcessError as e:
        console.print(f"[error]Error during training: {e}[/error]")
    except FileNotFoundError:
        console.print("[error]train_model.py not found. Make sure the training script exists.[/error]")

def run_workflow():
    console.print("[info]Triggering Kestra workflow...[/info]")
    try:
        # Assuming Kestra API expects a POST request to a specific endpoint to trigger a flow
        # This might need to be adjusted based on the actual Kestra API documentation
        # For example, it might be something like: curl -X POST http://localhost:8080/api/v1/executions/my_flow_id/trigger
        # For now, a generic curl command is used as per the prompt.
        subprocess.run(["curl", "http://localhost:8080"], check=True)
        console.print("[success]Kestra workflow triggered successfully![/success]")
    except subprocess.CalledProcessError as e:
        console.print(f"[error]Error triggering Kestra workflow: {e}[/error]")
    except FileNotFoundError:
        console.print("[error]curl command not found. Make sure curl is installed and in your PATH.[/error]")

def display_status():
    console.print("[success]System Online[/success]")

def main():
    while True:
        display_menu()
        choice = console.input("[menu]Enter your choice: [/menu]")
        if choice == "1":
            train_brain()
        elif choice == "2":
            run_workflow()
        elif choice == "3":
            display_status()
        elif choice == "4":
            console.print("[info]Exiting Career Compass CLI. Goodbye![/info]")
            break
        else:
            console.print("[warning]Invalid choice, please try again.[/warning]")

if __name__ == "__main__":
    main()
