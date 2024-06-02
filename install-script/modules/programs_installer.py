import os
import yaml
from core.command_runner import CommandRunner
from core.package_installer import PackageInstaller
from core.terminal_printer import TerminalPrinter


class ProgramsInstaller:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._package_installer = PackageInstaller(command_runner)
        self._printer = TerminalPrinter()

    def _install_programs_from_list(self):
        self._printer.print_message("Installing Programs")
        programs_file = os.path.expanduser("~/.dotfiles/install-script/programs.yml")

        if not os.path.isfile(programs_file):
            self._printer.print_message(
                "[red]programs.yml not found![/red]", style="red"
            )
            return

        with open(programs_file, "r") as file:
            programs_list = yaml.safe_load(file).get("programs", [])

        for program in programs_list:
            if not self._command_runner.run_command(f"pacman -Qi {program}"):
                if self._command_runner.run_command(f"pacman -Sp {program}"):
                    self._package_installer.install_with_pacman(program)
                else:
                    paru_result = self._package_installer.install_with_paru(program)
                    if paru_result is None:
                        self._printer.print_message(
                            f"[red]{program} installation failed or does not exist[/red]",
                            style="red",
                        )
            else:
                self._printer.print_message(
                    f"{program} is already installed...", style="green"
                )

    def _install_starship(self):
        self._printer.print_message("Installing Starship")
        if not self._command_runner.run_command("command -v starship"):
            if not self._command_runner.run_command(
                "curl -sS https://starship.rs/install.sh | sh -s -- --yes"
            ):
                self._printer.print_message(
                    "[red]Starship installation failed.[/red]", style="red"
                )
        else:
            self._printer.print_message("Starship is already installed", style="green")

    def _install_lazyvim(self):
        self._printer.print_message("Installing LazyVim")
        if not os.path.isfile(os.path.expanduser("~/.config/nvim/init.lua")):
            self._command_runner.run_command(
                "rm -rf ~/.config/nvim ~/.local/share/nvim ~/.local/state/nvim"
            )
            self._command_runner.run_command(
                "git clone https://github.com/LazyVim/starter ~/.config/nvim"
            )
            self._command_runner.run_command("rm -rf ~/.config/nvim/.git")
        else:
            self._printer.print_message(
                "LazyVim is already installed...", style="green"
            )

    def _install_lazyvim_extensions(self):
        self._printer.print_message("Installing LazyVim Extensions")
        if not self._command_runner.run_command("pip show pynvim"):
            self._package_installer.install_with_pacman("python-pynvim")
        else:
            self._printer.print_message("pynvim is already installed...", style="green")

        self._printer.print_message("Installing Node Extension")
        if not self._command_runner.run_command("command -v npm"):
            self._printer.print_message("[red]node is not installed[/red]", style="red")
        else:
            if not self._command_runner.run_command("npm list -g neovim"):
                self._command_runner.run_command("npm install -g neovim")
            else:
                self._printer.print_message(
                    "neovim-node is already installed...", style="green"
                )

    def run_programs_installation(self):
        self._printer.clear_terminal()
        self._printer.print_title("Programs Installation")
        self._install_programs_from_list()
        self._install_starship()
        self._install_lazyvim()
        self._install_lazyvim_extensions()
