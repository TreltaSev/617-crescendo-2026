# Port constants for driver and operator controllers. These should match the
# values in the Joystick tab of the Driver Station software
DRIVER_CONTROLLER_PORT: int = 0
OPERATOR_CONTROLLER_PORT: int = 1

# This value is multiplied by the joystick value when rotating the robot to
# help avoid turning too fast and being difficult to control
DRIVE_SCALING: float = .7
ROTATION_SCALING: float = .8
