from __future__ import annotations

# === Core ===
from wpilib import SmartDashboard
from commands2 import Command


# === Types ===

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from subsystems import FuelSubsystem

# === Constants ===
from utils.constants.fuel_constants import (
    LAUNCHING_LAUNCHER_VOLTAGE,
    LAUNCHING_FEEDER_VOLTAGE
)


class Launch(Command):

    def __init__(self, fuel_system: FuelSubsystem):

        # Declare the instance of fuel_subsystem as a dependency
        self.addRequirements(fuel_system)

        # Store passed in parameters
        self.fuel_system: FuelSubsystem = fuel_system

    def initialize(self):
        """
        Called when the command is initially scheduled. Set the rollers to the
        appropriate values for intaking
        """
        self.fuel_system.set_intake_launcher_roller(
            SmartDashboard.getNumber(
                "Launching launcher roller value", LAUNCHING_LAUNCHER_VOLTAGE
            )
        )

        self.fuel_system.set_feeder_roller(
            SmartDashboard.getNumber(
                "Launching feeder roller value",
                LAUNCHING_FEEDER_VOLTAGE
            )
        )

    def execute(self):
        """
        Called every time the scheduler runs while the command is scheduled. This
        command doesn't require updating any values while running
        """
        pass

    def end(self, interrupted: bool):
        """
        Called once the command ends or is interrupted. Stop the rollers
        """
        pass
