# python/main.py
import logging
import typer
from rich.console import Console
from rich.prompt import Confirm

from core.command_runner import CommandRunner
from core.file_manipulator import FileManipulator
from modules.initial_setup import InitialSetup
from modules.stow_migration import StowMigration
from modules.dependencies import Dependencies
from modules.programs_installer import ProgramsInstaller
from modules.daemons_setup import DaemonsSetup
from modules.postgresql_setup import PostgreSQLSetup
from modules.media_volume_setup import MediaVolumeSetup
from modules.grub_setup import GrubSetup

app = typer.Typer()
console = Console()


# Function to set up logging
def setup_logging(verbose: bool):
    level = logging.INFO if verbose else logging.WARNING
    logging.basicConfig(
        level=level, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )


command_runner = CommandRunner()
file_manipulator = FileManipulator()
initial_setup = InitialSetup(command_runner)
stow_migration = StowMigration(command_runner)
dependencies = Dependencies(command_runner)
programs_installer = ProgramsInstaller(command_runner)
daemons_setup = DaemonsSetup(command_runner)
postgresql_setup = PostgreSQLSetup(command_runner)
media_volume_setup = MediaVolumeSetup(command_runner)
grub_setup = GrubSetup(command_runner, file_manipulator)


def select_steps():
    console.print("Select steps to run:")
    steps = {
        "Setup": Confirm.ask("[ ] Setup"),
        "Stow": Confirm.ask("[ ] Stow"),
        "Dependencies": Confirm.ask("[ ] Install Dependencies"),
        "Programs": Confirm.ask("[ ] Install Programs"),
        "PostgreSQL": Confirm.ask("[ ] Setup PostgreSQL"),
        "Media Volume": Confirm.ask("[ ] Setup Media Volume"),
        "GRUB": Confirm.ask("[ ] Setup GRUB"),
        "Daemons": Confirm.ask("[ ] Setup Daemons"),
    }
    return steps


@app.command()
def run_installation(
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose logging"
    ),
):
    setup_logging(verbose)
    complete_installation = Confirm.ask("Do you want to run the complete installation?")

    if complete_installation:
        initial_setup.run_setup()
        dependencies.run_dependencies_installation()
        stow_migration.run_migration()
        programs_installer.run_programs_installation()
        postgresql_setup.run_postgresql_setup()
        media_volume_setup.run_media_volume_setup()
        grub_setup.run_grub_setup()
        daemons_setup.run_daemons_setup()
    else:
        selected_steps = select_steps()
        if selected_steps["Setup"]:
            initial_setup.run_setup()
        if selected_steps["Stow"]:
            stow_migration.run_migration()
        if selected_steps["Dependencies"]:
            dependencies.run_dependencies_installation()
        if selected_steps["Programs"]:
            programs_installer.run_programs_installation()
        if selected_steps["PostgreSQL"]:
            postgresql_setup.run_postgresql_setup()
        if selected_steps["Media Volume"]:
            media_volume_setup.run_media_volume_setup()
        if selected_steps["GRUB"]:
            grub_setup.run_grub_setup()
        if selected_steps["Daemons"]:
            daemons_setup.run_daemons_setup()


if __name__ == "__main__":
    app()
