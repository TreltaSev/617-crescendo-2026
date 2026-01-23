from __future__ import annotations


# === Core ===
import wpilib

from commands2 import Command
from commands2.button.commandxboxcontroller import CommandXboxController

# === Types ===
from typing import TYPE_CHECKING

from subsystems import DriveSubsystem, FuelSubsystem

# === Constants ===
from utils.constants.operator_constants import (
    DRIVER_CONTROLLER_PORT,
    OPERATOR_CONTROLLER_PORT
)

# === Commands ===
from commands.intake import Intake
from commands.example_auto import ExampleAuto
from commands.launch_sequence import LaunchSequence
from commands.eject import Eject
from commands.drive import Drive


class RobotContainer:

    # === Subsystems ===
    drive_system = DriveSubsystem()
    fuel_system = FuelSubsystem()

    # Driver Controller
    driver_controller = CommandXboxController(DRIVER_CONTROLLER_PORT)

    # Operator Controller
    operator_controller = CommandXboxController(OPERATOR_CONTROLLER_PORT)

    # The autonomous controller
    auto_chooser = wpilib.SendableChooser()

    def __init__(self) -> None:
        self.configure_bindings()

        # Set the options to show up in the Dashboard for selecting auto modes. If you
        # add additional auto modes you can add additional lines here with
        # self.auto_chooser.addOption
        self.auto_chooser.setDefaultOption("Autonomous", ExampleAuto(self.drive_system, self.fuel_system))

    @classmethod
    def configure_bindings(cls):
        """
        Use this method to define your trigger->command mappings.
        """

        # While the left bumper on operator controller is held, intake Fuel
        cls.operator_controller.leftBumper().whileTrue(Intake(cls.fuel_system))

        # While the right bumper on the operator controller is held, spin up for 1
        # second, then launch fuel. When the button is released, stop.
        cls.operator_controller.rightBumper().whileTrue(LaunchSequence(cls.fuel_system))

        # While the A button is held on the operator controller, eject fuel back out
        # the intake
        cls.operator_controller.a().whileTrue(Eject(cls.fuel_system))

        # Set the default command for the drive subsystem to the command provided by
        # factory with the values provided by the joystick axes on the driver
        # controller. The Y axis of the controller is inverted so that pushing the
        # stick away from you (a negative value) drives the robot forwards (a positive
        # value)
        cls.drive_system.setDefaultCommand(Drive(cls.drive_system, cls.driver_controller))

        # This is supposed to start the fuel subsystem and callback to stop it
        # cls.fuel_system.setDefaultCommand()

    @classmethod
    def get_autonomous_command(cls) -> Command:
        return cls.auto_chooser.getSelected()
