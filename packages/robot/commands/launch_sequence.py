from __future__ import annotations

# === Types ===
from commands2 import Command, SequentialCommandGroup

from commands.spinup import SpinUp
from commands.launch import Launch

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from subsystems import FuelSubsystem

# === Constants ===
from utils.constants.fuel_constants import (
    SPIN_UP_SECONDS
)


class LaunchSequence(SequentialCommandGroup):
    """
    Creates a new LaunchSequence
    """

    def __init__(self, fuel_system: FuelSubsystem, *commands: Command):
        self.addCommands(
            SpinUp(fuel_system).withTimeout(SPIN_UP_SECONDS),
            Launch(fuel_system),
            *commands
        )
