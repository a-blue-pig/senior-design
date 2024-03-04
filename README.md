# senior-design (ME 266K)

This is a repositry for our senior design project (ME 266K).
The repository contains all the scripts used to calculate heat transfer, our
motor specs, and the software scripts to control the motor.

## Setup
Create a virtual environment with python 3.8.10

### Venv Instructions
In order for VirtualENV to create an environemnt with the correct python verison you need to install python 3.12 first.\
Then create an environment using that specific python version.

Create the environment:\
`cd senior-design`\
`python3.12 -m venv .venv`

Activate the environment:\
`. .venv/Scripts/activate      # Windows`\
`source .venv/bin/activate     # Mac/Linux`

Install the required packages: `pip install -r requirements.txt`

### Conda Instructions
Create the environment:\
`cd senior-design`\
`conda create -n senior-design python=3.12`

Activate the environment (Use this command if already env already created and
you want to use it)\
`conda activate senior-design`


Install the required packages: `pip install -r requirements.txt`


## TODO
1. Add HT scripts
2. Add Motor/System Configuration (parameters)
3. Add Software Instructions for the Synapticon
4. Add scripts to generate aggressive trajectories
5. Add instructions for replicating the project/setup on different machines.