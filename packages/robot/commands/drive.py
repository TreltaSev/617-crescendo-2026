from __future__ import annotations

from commands2 import Command
from commands2.button.commandxboxcontroller import CommandXboxController

# === Types ===
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from subsystems import DriveSubsystem


class Drive(Command):

    def __init__(self, drive_system: DriveSubsystem, driver_controller: CommandXboxController):

        # Declare the instance of drive_subsystem as a dependency
        self.addRequirements(drive_system)

        # Store passed in parameters
        self.drive_system: DriveSubsystem = drive_system
        self.driver_controller: CommandXboxController = driver_controller

    def initialize(self):
        """Called when the command is initially scheduled."""
        pass

    def execute(self):
        """
        Called every time the scheduler runs while the command is scheduled.
        The Y axis of the controller is inverted so that pushing the
        stick away from you (a negative value) drives the robot forwards (a positive
        value). The X axis is scaled down so the rotation is more easily
        controllable.
        """
        pass

    def end(self, interrupted: bool):
        """Called once the command ends or is interrupted."""
        # self.drive_system.drive_arcade(0, 0)
