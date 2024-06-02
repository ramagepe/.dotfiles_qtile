from rich.console import Console


class TerminalPrinter:
    def __init__(self):
        self._console = Console()

    def clear_terminal(self):
        self._console.clear()

    def print_title(self, title: str):
        ascii_art = f"""
        ========================================
        =   {title.center(35)}   =
        ========================================
        """
        self._console.print(ascii_art, style="bold green")

    def print_message(self, message: str, style: str = "green"):
        self._console.print(message, style=style)
