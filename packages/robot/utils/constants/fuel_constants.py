
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
