# === Core ===
from rev import SparkMax, SparkMaxConfig
from rev import ResetMode, PersistMode

from commands2 import Subsystem

from wpilib import SmartDashboard


# === Constants ===
from utils.constants.fuel_constants import (
    INTAKE_LAUNCHER_MOTOR_ID,
    FEEDER_MOTOR_ID,
    FEEDER_MOTOR_CURRENT_LIMIT,
    LAUNCHER_MOTOR_CURRENT_LIMIT,
    INTAKING_FEEDER_VOLTAGE,
    INTAKING_INTAKE_VOLTAGE,
    LAUNCHING_FEEDER_VOLTAGE,
    LAUNCHING_LAUNCHER_VOLTAGE,
    SPIN_UP_FEEDER_VOLTAGE
)

from utils.constants.spark.motor_types import (
    BRUSHED_MOTOR,
    BRUSHLESS_MOTOR
)


class FuelSubsystem(Subsystem):

    def __init__(self) -> None:
        # create brushed motors for each of the motors on the launcher mechanism
        self.intake_launcher_roller = SparkMax(INTAKE_LAUNCHER_MOTOR_ID, BRUSHED_MOTOR)
        self.feeder_roller = SparkMax(FEEDER_MOTOR_ID, BRUSHED_MOTOR)

        # create the configuration for the feeder roller, set a current limit and apply
        # the config to the controller
        feeder_config = SparkMaxConfig()
        feeder_config.smartCurrentLimit(FEEDER_MOTOR_CURRENT_LIMIT)
        self.feeder_roller.configure(feeder_config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # create the configuration for the launcher roller, set a current limit, set
        # the motor to inverted so that positive values are used for both intaking and
        # launching, and apply the config to the controller
        launcherConfig = SparkMaxConfig()
        launcherConfig.inverted(True)
        launcherConfig.smartCurrentLimit(LAUNCHER_MOTOR_CURRENT_LIMIT)
        self.intake_launcher_roller.configure(launcherConfig, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # put default values for various fuel operations onto the dashboard
        # all commands using this subsystem pull values from the dashboard to allow
        # you to tune the values easily, and then replace the values in Constants.java
        # with your new values. For more information, see the Software Guide.
        SmartDashboard.putNumber("Intaking feeder roller value", INTAKING_FEEDER_VOLTAGE)
        SmartDashboard.putNumber("Intaking intake roller value", INTAKING_INTAKE_VOLTAGE)
        SmartDashboard.putNumber("Launching feeder roller value", LAUNCHING_FEEDER_VOLTAGE)
        SmartDashboard.putNumber("Launching launcher roller value", LAUNCHING_LAUNCHER_VOLTAGE)
        SmartDashboard.putNumber("Spin-up feeder roller value", SPIN_UP_FEEDER_VOLTAGE)

    def set_intake_launcher_roller(self, voltage: float):
        """A method to set the voltage of the intake roller"""
        self.intake_launcher_roller.setVoltage(voltage)

    def set_feeder_roller(self, voltage: float):
        """A method to set the voltage of the feeder roller"""
        self.feeder_roller.setVoltage(voltage)

    def stop(self):
        """A method to stop the rollers"""
        self.feeder_roller.set(0)
        self.intake_launcher_roller.set(0)

    def periodic(self) -> None:
        """This method will be called once per scheduler run"""
        pass
