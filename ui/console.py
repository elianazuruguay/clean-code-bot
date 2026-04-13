from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.syntax import Syntax

console = Console()


def print_title(text: str) -> None:
    console.print(Panel.fit(text, style="bold cyan"))


def print_analysis(text: str) -> None:
    console.print(Markdown(text))


def print_plan(text: str):
    console.print(Panel(Markdown(text), title="🛠️ IMPROVEMENT PLAN", border_style="yellow"))


def print_success(message: str) -> None:
    console.print(f"[green]✅ {message}[/green]")


def print_error(title: str, message: str) -> None:
    console.print(
        Panel(
            f"[red]{message}[/red]",
            title=f"❌ {title}",
            border_style="red",
        )
    )

def print_warning(message: str) -> None:
    console.print(f"[yellow]⚠️ {message}[/yellow]")


def print_info(message: str) -> None:
    console.print(f"[blue]ℹ️ {message}[/blue]")

def print_code(code: str, language: str):
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)
    console.print(syntax)