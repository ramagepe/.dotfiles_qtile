import os
from core.command_runner import CommandRunner
from core.package_installer import PackageInstaller
from core.terminal_printer import TerminalPrinter


class StowMigration:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._package_installer = PackageInstaller(command_runner)
        self._printer = TerminalPrinter()

    def _install_stow(self):
        self._printer.print_message("Installing stow...", style="green")
        self._package_installer.install_with_pacman("stow")

    def _run_stow(self):
        try:
            self._printer.print_message("Stowing...", style="green")

            # Remove conflicts
            bashrc_path = os.path.expanduser("~/.bashrc")
            qtile_config_path = os.path.expanduser("~/.config/qtile")
            if os.path.exists(bashrc_path):
                os.remove(bashrc_path)
            if os.path.exists(qtile_config_path):
                os.system(f"rm -r {qtile_config_path}")

            # Run stow on the .dotfiles directory, ignoring install-script
            dotfiles_path = os.path.expanduser("~/.dotfiles")
            if not self._command_runner.run_command(
                f"cd {dotfiles_path} && stow ."
            ):
                self._printer.print_message(
                    "[red]Stow failed due to conflicts. Skipping stow.[/red]",
                    style="red",
                )
        except Exception as e:
            self._printer.print_message(
                f"[red]An error occurred during stowing: {e}[/red]", style="red"
            )

    def run_migration(self):
        self._printer.clear_terminal()
        self._printer.print_title("Stow Migration")
        self._install_stow()
        self._run_stow()
