from core.command_runner import CommandRunner
from core.terminal_printer import TerminalPrinter
from core.file_manipulator import FileManipulator


class GrubSetup:
    def __init__(
        self, command_runner: CommandRunner, file_manipulator: FileManipulator
    ):
        self._command_runner = command_runner
        self._file_manipulator = file_manipulator
        self._printer = TerminalPrinter()

    def _install_grub_theme(self, theme: str, resolution: str):
        self._printer.print_message(
            f"Installing GRUB theme: {theme} with resolution: {resolution}",
            style="green",
        )
        try:
            self._command_runner.run_command(
                f"./install.sh -t {theme} -s {resolution}", sudo=True
            )
        except Exception as e:
            self._printer.print_message(
                f"Failed to install GRUB theme: {e}", style="red"
            )

    def _edit_grub_btrfsd_service(self):
        self._printer.print_message("Editing grub-btrfsd service...", style="green")
        service_file = "/usr/lib/systemd/system/grub-btrfsd.service"
        search_text = "ExecStart=/usr/bin/grub-btrfsd --syslog /.snapshots"
        replace_text = "ExecStart=/usr/bin/grub-btrfsd --syslog -t"

        try:
            self._file_manipulator.replace_line_in_file(
                service_file, search_text, replace_text
            )
            self._command_runner.run_command("systemctl daemon-reload", sudo=True)
            self._printer.print_message(
                "grub-btrfsd service edited successfully!", style="green"
            )
        except Exception as e:
            self._printer.print_message(
                f"Failed to edit grub-btrfsd service: {e}", style="red"
            )

    def run_grub_setup(self):
        self._printer.clear_terminal()
        self._printer.print_title("GRUB Setup")

        install_theme = (
            self._printer._console.input(
                "Do you want to install GRUB theme? [y/N] "
            ).lower()
            == "y"
        )
        if install_theme:
            theme = self._printer._console.input("Enter the GRUB theme: ")
            resolution = self._printer._console.input(
                "Enter the resolution (e.g., 1080p): "
            )
            self._install_grub_theme(theme, resolution)
        else:
            self._printer.print_message(
                "Skipping GRUB theme installation...", style="yellow"
            )

        edit_service = (
            self._printer._console.input(
                "Do you want to edit grub-btrfsd service? [y/N] "
            ).lower()
            == "y"
        )
        if edit_service:
            self._edit_grub_btrfsd_service()
        else:
            self._printer.print_message(
                "Skipping grub-btrfsd service editing...", style="yellow"
            )
