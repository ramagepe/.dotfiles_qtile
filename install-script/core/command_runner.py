import subprocess
import logging


class CommandRunner:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def run_command(self, command: str, sudo: bool = False, log_error: bool = True) -> bool:
        if sudo:
            command = f"sudo {command}"
        try:
            self._log_command(command)
            process = subprocess.run(
                command, shell=True, check=True, capture_output=True, text=True
            )
            self._log_output(process.stdout.strip())
            return True
        except subprocess.CalledProcessError as e:
            if log_error:
                self._log_error(e.stderr.strip())
            return False
    
    def refresh_shell_environment(self):
        self.run_command("source /etc/profile")

    def clear_terminal(self):
        subprocess.run("clear", shell=True)

    def _print_title(self, title: str):
        self.clear_terminal()
        ascii_art = f"""
        ========================================
        =   {title.center(35)}   =
        ========================================
        """
        self._console.print(ascii_art, style="bold green")

    def _log_command(self, command: str):
        self.logger.info(f"Running command: {command}")

    def _log_output(self, output: str):
        self.logger.info(f"Command output: {output}")

    def _log_error(self, error: str):
        self.logger.error(f"Command failed: {error}")
