class Constants:

    class DriveConstants:

        # Motor controller IDs for drivetrain motors
        LEFT_LEADER_ID: int = 1
        LEFT_FOLLOWER_ID: int = 2
        RIGHT_LEADER_ID: int = 3
        RIGHT_FOLLOWER_ID: int = 4

        # Current limit for drivetrain motors. 60A is a reasonable maximum to reduce
        # likelihood of tripping breakers or damaging CIM motors
        DRIVE_MOTOR_CURRENT_LIMIT: int = 60

    class FuelConstants:

        # Motor controller IDs for Fuel Mechanism Motors
        FEEDER_MOTOR_ID: int = 6
        INTAKE_LAUNCHER_MOTOR_ID: int = 5

        # Current limit and nominal voltage for fuel mechanism motors.
        FEEDER_MOTOR_CURRENT_LIMIT: int = 60
        LAUNCHER_MOTOR_CURRENT_LIMIT: int = 60

        # Voltage values for various fuel operations. These values may need to be tuned
        # based on exact robot construction.
        # See the Software Guide for tuning information
        INTAKING_FEEDER_VOLTAGE: int = -12
        INTAKING_INTAKE_VOLTAGE: int = 10
        LAUNCHING_FEEDER_VOLTAGE: int = 9
        LAUNCHING_LAUNCHER_VOLTAGE: float = 10.6
        SPIN_UP_FEEDER_VOLTAGE: int = -6
        SPIN_UP_SECONDS: int = 1

    class OperatorConstants:
        # Port constants for driver and operator controllers. These should match the
        # values in the Joystick tab of the Driver Station software
        DRIVER_CONTROLLER_PORT: int = 0
        OPERATOR_CONTROLLER_PORT: int = 1

        # This value is multiplied by the joystick value when rotating the robot to
        # help avoid turning too fast and beign difficult to control
        DRIVE_SCALING: float = .7
        ROTATION_SCALING: float = .8
