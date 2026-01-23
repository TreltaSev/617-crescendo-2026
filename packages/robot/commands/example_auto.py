from __future__ import annotations

# === Types ===
from commands2 import Command, SequentialCommandGroup

from commands.autodrive import AutoDrive
from commands.launch import Launch

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from subsystems import DriveSubsystem, FuelSubsystem


class ExampleAuto(SequentialCommandGroup):
    """
    Example auto drive and launch command group
    """

    def __init__(self, drive_system: DriveSubsystem, fuel_system: FuelSubsystem, *commands: Command):
        super().__init__()
        self.addCommands(
            AutoDrive(drive_system, 0.5, 0.0).withTimeout(.25),
            Launch(fuel_system),
            *commands
        )
