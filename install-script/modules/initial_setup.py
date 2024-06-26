from core.command_runner import CommandRunner
from core.package_installer import PackageInstaller
from core.terminal_printer import TerminalPrinter


class InitialSetup:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._package_installer = PackageInstaller(command_runner)
        self._printer = TerminalPrinter()

    def _install_reflector_and_rsync(self):
        self._printer.print_message("Installing Reflector and Rsync")
        try:
            self._package_installer.install_with_pacman("reflector")
            self._package_installer.install_with_pacman("rsync")
        except Exception as e:
            self._printer.print_message(
                f"Failed to install Reflector and Rsync: {e}", style="red"
            )

    def _update_mirrors(self):
        self._printer.print_message("Updating Mirrors")
        self._command_runner.refresh_shell_environment()
        if not self._command_runner.run_command(
            "reflector --verbose --latest 10 --sort rate --save /etc/pacman.d/mirrorlist"
        ):
            self._printer.print_message(
                "Updating mirrors failed. Skipping.", style="red"
            )

    def _update_system(self):
        self._printer.print_message("Updating System")
        if not self._command_runner.run_command("pacman -Syu --noconfirm", sudo=True):
            self._printer.print_message(
                "System update failed. Skipping.", style="red"
            )

    def run_setup(self):
        self._printer.clear_terminal()
        self._printer.print_title("Setup")
        self._install_reflector_and_rsync()
        self._update_mirrors()
        self._update_system()
