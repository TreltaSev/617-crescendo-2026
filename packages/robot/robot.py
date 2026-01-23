import wpilib

from commands2 import CommandScheduler
from robot_container import RobotContainer


class MainRobot(wpilib.TimedRobot):
    """
    This is just a replica of the sample code given in the documentation [here](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java-python.html#basic-drivetrain-example).

    """

    def __init__(self, period: float = 0.02) -> None:
        super().__init__(period)

        # Instantiate our RobotContainer. This will perform all our button bindings,
        # and put our
        # autonomous chooser on the dashboard.
        self.robot_container = RobotContainer()

    def robotPeriodic(self) -> None:
        """
        Runs the Scheduler. This is responsible for polling buttons, adding
        newly-scheduled
        commands, running already-scheduled commands, removing finished or
        interrupted commands,
        and running subsystem periodic() methods. This must be called from the
        robot's periodic
        block in order for anything in the Command-based framework to work.
        """
        CommandScheduler.getInstance().run()

    # ====== TELOPERATED OPERATIONS ======

    def teleopInit(self) -> None:
        """Called once each time the robot enteres "teloperated" mode"""
        if self.autonomous_command:
            self.autonomous_command.cancel()

    def teleopPeriodic(self) -> None:
        """Called periodically during teleoperated mode."""
        pass

    # ====================================

    # ====== AUTONOMOUS LOGIC ======

    def autonomousInit(self):
        """Ran once each time the robot enters autonomous mode."""
        self.autonomous_command = self.robot_container.get_autonomous_command()

        if not self.autonomous_command:
            CommandScheduler.getInstance().schedule(self.autonomous_command)

    def autonomousPeriodic(self) -> None:
        """Called periodically during autonomous"""
        pass

    # ==============================

    # ====== TESTING LOGIC BELOW ======

    def testInit(self) -> None:
        CommandScheduler.getInstance().cancelAll()

    def testPeriodic(self) -> None:
        """Periodic code for test mode should go here."""
        pass

    def testExit(self) -> None:
        """Exit code for test mode should go here."""
        pass

    # =================================
