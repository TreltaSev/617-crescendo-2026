# Team 617's Crescendo Code for 2026

## Important Resources
- [RobotPY Examples](https://github.com/robotpy/examples/blob/main/GameData/robot.py)
    - [Basic Example](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-4/creating-test-drivetrain-program-cpp-java-python.html)
- [RobotPY API](https://robotpy.readthedocs.io/projects/robotpy/en/stable/index.html)

## Project Setup

### Install Required Packages
- [python](https://www.python.org/downloads/)
- [rust-just](https://github.com/casey/just#installation)

### Run initialization command
```bash
just init
```

#### Or setup the project manually
```bash

# Move to robot package
cd ./packages/robot

# Create virtual environment
python -m venv venv

# on linux:
source ./venv/bin/activate

# on windows
./venv/bin/activate

# Install packages
pip install -r ./requirements.txt
```

## Project Commands
While you can manually run robotpy using python, there are some scripts that can be run so long as you have [just](#install-required-packages) installed. You can find out all the commands and what they do with
```bash
just -l
```
