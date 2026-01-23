# === Core ===
import rev
from rev import SparkLowLevel
from rev import ResetMode, PersistMode

from commands2 import Subsystem

from wpilib.drive import DifferentialDrive

# === Constants ===
from utils.constants.drive_constants import (
    LEFT_LEADER_ID,
    LEFT_FOLLOWER_ID,
    RIGHT_LEADER_ID,
    RIGHT_FOLLOWER_ID,
    DRIVE_MOTOR_CURRENT_LIMIT
)

from utils.constants.spark.motor_types import (
    BRUSHED_MOTOR,
    BRUSHLESS_MOTOR
)


class DriveSubsystem(Subsystem):

    def __init__(self) -> None:

        # Initialize brushed motors for drives
        self.left_leader = rev.SparkMax(deviceID=LEFT_LEADER_ID, type=BRUSHLESS_MOTOR)
        self.left_follower = rev.SparkMax(deviceID=LEFT_FOLLOWER_ID, type=BRUSHLESS_MOTOR)
        self.right_leader = rev.SparkMax(deviceID=RIGHT_LEADER_ID, type=BRUSHLESS_MOTOR)
        self.right_follower = rev.SparkMax(deviceID=RIGHT_FOLLOWER_ID, type=BRUSHLESS_MOTOR)

        # Group up left and right lead drives
        __leads: list[rev.SparkMax] = [self.left_leader, self.right_leader]
        self.drive = DifferentialDrive(*__leads)

        # Create the configuration to apply to motors. Voltage compensation
        # helps the robot perform more similarly on different
        # battery voltages (at the cost of a little bit of top speed on a fully charged
        # battery). The current limit helps prevent tripping
        # breakers.
        config = rev.SparkMaxConfig()
        config.voltageCompensation(12)
        config.smartCurrentLimit(DRIVE_MOTOR_CURRENT_LIMIT)

        # Set configuration to follow each leader and then apply it to corresponding
        # follower. Resetting in case a new controller is swapped
        # in and persisting in case of a controller reset due to breaker trip
        config.follow(self.left_leader)
        self.left_follower.configure(config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        config.follow(self.right_leader)
        self.right_follower.configure(config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

        # Remove following, then apply config to right leader
        config.disableFollowerMode()
        self.right_leader.configure(config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)
        # Set config to inverted and then apply to left leader. Set Left side inverted
        # so that positive values drive both sides forward
        config.inverted(True)
        self.left_leader.configure(config, ResetMode.kResetSafeParameters, PersistMode.kPersistParameters)

    def periodic(self) -> None:
        """This method will be called once per scheduler run"""
        pass

    def drive_arcade(self, x_speed: float, z_rotation: float) -> None:
        """Arcade drive method for differential drive platform for this object"""
        self.drive.arcadeDrive(x_speed, z_rotation)
