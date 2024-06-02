from core.command_runner import CommandRunner
from core.package_installer import PackageInstaller
from core.terminal_printer import TerminalPrinter


class DaemonsSetup:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._package_installer = PackageInstaller(command_runner)
        self._printer = TerminalPrinter()
        self._daemons = [
            {"package": "networkmanager", "service": "NetworkManager.service"},
            {"package": "bluez", "service": "bluetooth.service"},
            {"package": "cups", "service": "cups.service"},
            {"package": "avahi", "service": "avahi-daemon.service"},
            {"package": "util-linux", "service": "fstrim.service"},
            {"package": "util-linux", "service": "fstrim.timer"},
            {"package": "grub-btrfs", "service": "grub-btrfsd.service"},
            {"package": "docker", "service": "docker.service"},
            {"package": "postgresql", "service": "postgresql.service"},
        ]

    def _install_and_enable_service(self, package: str, service: str):
        try:
            self._printer.print_message(f"Installing {package}...", style="green")
            self._package_installer.install_with_pacman(package)

            self._printer.print_message(f"Enabling {service} service...", style="green")
            self._command_runner.run_command(f"sudo systemctl enable {service}")
            self._command_runner.run_command(f"sudo systemctl start {service}")
        except Exception as e:
            self._printer.print_message(
                f"[red]Failed to install or enable {service}: {e}[/red]", style="red"
            )

    def run_daemons_setup(self):
        self._printer.clear_terminal()
        self._printer.print_title("Daemons Setup")
        for daemon in self._daemons:
            self._install_and_enable_service(daemon["package"], daemon["service"])
