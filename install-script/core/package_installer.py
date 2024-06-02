import logging
import shutil
from core.command_runner import CommandRunner


class PackageInstaller:
    def __init__(self, command_runner: CommandRunner):
        self.command_runner = command_runner
        self.logger = logging.getLogger(self.__class__.__name__)

    def _is_pacman_installed(self, package: str) -> bool:
        result = self.command_runner.run_command(f"pacman -Qs {package}")
        return bool(result.strip())

    def _is_paru_installed(self, package: str) -> bool:
        result = self.command_runner.run_command(f"paru -Qs {package}")
        return bool(result.strip())

    def _is_command_available(self, command: str) -> bool:
        return shutil.which(command) is not None

    def install_with_pacman(self, package: str):
        if self._is_pacman_installed(package):
            self.logger.info(f"{package} is already installed via pacman.")
        else:
            self.command_runner.run_command(f"sudo pacman -S --noconfirm {package}")
            self.logger.info(f"Installed {package} via pacman.")

    def install_with_paru(self, package: str):
        if self._is_paru_installed(package):
            self.logger.info(f"{package} is already installed via paru.")
        else:
            self.command_runner.run_command(f"paru -S --noconfirm {package}")
            self.logger.info(f"Installed {package} via paru.")

    def install_with_clone_and_build(self, repo_url: str, build_command: str):
        temp_dir = "/tmp/repo"
        package_name = repo_url.split("/")[-1].replace(".git", "")
        if self._is_command_available(package_name):
            self.logger.info(f"{package_name} is already installed.")
        else:
            self.command_runner.run_command(f"git clone {repo_url} {temp_dir}")
            self.command_runner.run_command(f"cd {temp_dir} && {build_command}")
            self.command_runner.run_command(f"rm -rf {temp_dir}")
            self.logger.info(f"Installed {package_name} from {repo_url}.")

    def install_with_curl(self, url: str, command: str, command_name: str):
        if self._is_command_available(command_name):
            self.logger.info(f"{command_name} is already installed.")
        else:
            self.command_runner.run_command(f"curl -sS {url} | {command}")
            self.logger.info(f"Installed {command_name} from {url}.")
