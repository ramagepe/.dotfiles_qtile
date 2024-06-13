from core.command_runner import CommandRunner
from core.terminal_printer import TerminalPrinter


class MediaVolumeSetup:
    def __init__(self, command_runner: CommandRunner):
        self._command_runner = command_runner
        self._printer = TerminalPrinter()

    def _add_volume_to_fstab(self):
        self._printer.print_message("Adding volume to /etc/fstab...", style="green")
        fstab_entry = "\n# /dev/nvme1n0 (media)\nUUID=38c3d749-e70b-433f-a8ff-663e729dbd50  /home/ramage/media  btrfs  defaults  0 0\n"

        try:
            with open("/etc/fstab", "a") as fstab:
                fstab.write(fstab_entry)
            self._printer.print_message(
                "Volume added to /etc/fstab successfully!", style="green"
            )
        except Exception as e:
            self._printer.print_message(
                f"Failed to add volume to /etc/fstab: {e}", style="red"
            )

    def run_media_volume_setup(self):
        self._printer.clear_terminal()
        self._printer.print_title("Media Volume Setup")
        self._add_volume_to_fstab()
