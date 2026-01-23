from __future__ import annotations


from wpilib import SmartDashboard
from commands2 import Command

# === Types ===
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from subsystems import FuelSubsystem

# === Constants ===
from utils.constants.fuel_constants import (
    INTAKING_FEEDER_VOLTAGE,
    INTAKING_INTAKE_VOLTAGE,
)


class Intake(Command):

    def __init__(self, fuel_system: FuelSubsystem):

        # Declare the instance of fuel_system as a
        self.addRequirements(fuel_system)

        # Store passed in parameters
        self.fuel_system: FuelSubsystem = fuel_system

    def initialize(self):
        """
        Called when the command is initially scheduled. Set the rollers to the
        appropriate values for intaking
        """
        self.fuel_system.set_intake_launcher_roller(SmartDashboard.getNumber("Intaking intake roller value", INTAKING_INTAKE_VOLTAGE))
        self.fuel_system.set_feeder_roller(SmartDashboard.getNumber("Intaking feeder roller value", INTAKING_FEEDER_VOLTAGE))

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
        self.fuel_system.set_intake_launcher_roller(0)
        self.fuel_system.set_feeder_roller(0)
