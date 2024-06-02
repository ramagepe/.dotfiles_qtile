import os
from core.command_runner import CommandRunner
from core.package_installer import PackageInstaller
from core.terminal_printer import TerminalPrinter


class Dependencies:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._package_installer = PackageInstaller(command_runner)
        self._printer = TerminalPrinter()

    def _install_core_dependencies(self):
        self._printer.print_message("Installing Core Dependencies")
        self._package_installer.install_with_pacman("curl")
        self._package_installer.install_with_pacman("yq")
        self._package_installer.install_with_pacman("base-devel")

    def _install_paru(self):
        self._printer.print_message("Installing Paru")
        if not self._command_runner.run_command("command -v paru"):
            self._command_runner.run_command(
                "git clone https://aur.archlinux.org/paru.git $HOME/.local/share/paru"
            )
            self._command_runner.run_command(
                "cd $HOME/.local/share/paru && makepkg -si --noconfirm && cd -"
            )
        else:
            self._printer.print_message("paru is already installed", style="green")

    def _install_rustup(self):
        self._printer.print_message("Installing Rustup")
        if not self._command_runner.run_command("command -v rustup"):
            self._command_runner.run_command("sudo pacman -Rs --noconfirm rust")
            self._command_runner.run_command(
                "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
            )
            self._command_runner.run_command("source $HOME/.cargo/env")
        else:
            self._printer.print_message("rustup is already installed", style="green")

    def _install_nvm_node(self):
        self._printer.print_message("Installing NVM + Node")
        nvm_dir = os.path.expanduser("~/.config/nvm")
        if not os.path.exists(nvm_dir):
            self._command_runner.run_command(
                'export NVM_DIR="$HOME/.config/nvm" && curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash'
            )
            self._command_runner.run_command(
                'export NVM_DIR="$HOME/.config/nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"'
            )
        else:
            self._printer.print_message("nvm is already installed", style="green")

        # Source nvm in the current session
        self._command_runner.run_command(
            'export NVM_DIR="$HOME/.config/nvm" && [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && [ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"'
        )

        if not self._command_runner.run_command("command -v node"):
            self._command_runner.run_command("nvm install node")
        else:
            self._printer.print_message("node is already installed", style="green")

    def run_dependencies_installation(self):
        self._printer.clear_terminal()
        self._printer.print_title("Dependencies Installation")
        self._install_core_dependencies()
        self._install_paru()
        self._install_rustup()
        self._install_nvm_node()
