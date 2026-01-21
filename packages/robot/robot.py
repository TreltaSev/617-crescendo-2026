import wpilib
import wpilib.drive


class MainRobot(wpilib.TimedRobot):
    """
    This is just a replica of the sample code given in the documentation [here](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java-python.html#basic-drivetrain-example).

    """

    def __init__(self, period: float = 0.02) -> None:
        super().__init__(period)

        # Initialize left and right example drives
        self.leftDrive = wpilib.PWMSparkMax(channel=0)
        self.rightDrive = wpilib.PWMSparkMax(channel=1)
        self.__drives: list[wpilib.PWMSparkMax] = [
            self.leftDrive, self.rightDrive]

        # Group up the left and right drives
        self.robotDrive = wpilib.drive.DifferentialDrive(*self.__drives)

        # Setup example controller
        self.controller = wpilib.XboxController(port=0)

        # Initialize global timer, doesn't start it
        self.timer = wpilib.Timer()

        # === BELOW IS CTRL+C CTRL+V ===
        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        # ==============================
        self.rightDrive.setInverted(True)

    def autonomousInit(self):
        """Ran once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self) -> None:
        """Called periodically during autonomous"""
        pass

    # ====== TELOPERATED OPERATIONS ======

    def teleopInit(self) -> None:
        """Called once each time the robot enteres "teloperated" mode"""
        pass

    def teleopPeriodic(self) -> None:
        """Called periodically during teleoperated mode."""

        # This is an example arcade drive
        self.robotDrive.arcadeDrive(
            -self.controller.getLeftY(), -self.controller.getRightX()
        )

    # ====================================

    # ====== AUTONOMOUS LOGIC ======

    def autonomousInit(self) -> None:
        """
        Run once each time the robot enters "autonomous" mode
        """
        self.timer.restart()

    # ==============================

    # ====== TESTING LOGIC BELOW ======

    def testInit(self) -> None:
        return super().testInit()

    def testPeriodic(self) -> None:
        """Periodic code for test mode should go here."""
        pass

    def testExit(self) -> None:
        """Exit code for test mode should go here."""
        pass

    # =================================
