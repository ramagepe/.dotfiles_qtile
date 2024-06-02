from core.command_runner import CommandRunner
from core.terminal_printer import TerminalPrinter


class PostgreSQLSetup:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._printer = TerminalPrinter()
        self._data_dir = "/var/lib/postgres/data"

    def _disable_copy_on_write(self):
        self._printer.print_message(
            "Disabling Copy-on-Write on PostgreSQL data directory...", style="green"
        )
        self._command_runner.run_command(
            f"-u postgres chattr +C {self._data_dir}", sudo=True
        )

    def _initialize_database(self):
        self._printer.print_message(
            "Initializing PostgreSQL database...", style="green"
        )
        self._command_runner.run_command(
            f"-u postgres initdb -D {self._data_dir}", sudo=True
        )

    def run_postgresql_setup(self):
        self._printer.clear_terminal()
        self._printer.print_title("PostgreSQL Setup")
        self._initialize_database()
        self._disable_copy_on_write()
