#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vrc import *
from vexcode_vrc.events import get_Task_func
  
# constructors

drivetrain = Drivetrain()
brain = Brain()
bottom_distance = Distance("BottomDistance", 18)
roller_optical = Optical("RollerOptical", 2)
gps = GPS("GPS", 3)
intake_motor_group = Motor("IntakeMotorGroup", 10)
bottom_line_tracker = LineTracker("BottomLineTracker", 22)
middle_line_tracker = LineTracker("MiddleLineTracker", 23)
top_line_tracker = LineTracker("TopLineTracker", 24)
#endregion VEXcode Generated Robot Configuration

# --------------------------------------------------
# 
# 	Project:            Da Funny
#	Author:             Funny Phu
#	Created:            
#	Description:        Shoot Shoot Shoot
#   Starting Position:  
#   Preload:            
# 
# --------------------------------------------------

# Library imports
from vexcode_vrc import *
from math import sqrt
# Function go to Coordinates:


# Add project code in "main"
def main():
    #Set Speed
    intake_motor_group.set_velocity(100, PERCENT)
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT) 

    #Pick/Shoot 3 Dish
    goTo(-1200,1000,0)
    drivetrain.turn_to_heading(275, DEGREES)
    shoot(90, 140)

    # Spin First Roller
    drivetrain.turn_to_heading(0, DEGREES)
    goTo(-1450,1100,1)
    shoot(100, 30)

    # Pick/Shoot 3 Dish
    goTo(-1000,950,0)
    shoot(100, 100)
    drivetrain.drive_for(FORWARD, 25, MM)
    drivetrain.drive_for(REVERSE, 25, MM)
    shoot(100, 20)
    drivetrain.turn_to_heading(277.5, DEGREES)
    shoot(100, 140)

    # Spin Second Roller
    goTo(-900,1450,1)
    shoot(100, 30)

    # Pick/Shoot Leftover Dish
    goTo(-1300,1500,0)
    shoot(100, 20)
    goTo(-450,1000,0)
    shoot(100, 60)
    goTo(-550,750,0)
    shoot(100, 30)
    drivetrain.turn_to_heading(166, DEGREES)
    shoot(90, 140)
    
    goTo(-800,450,0)
    shoot(100, 100)
    drivetrain.drive_for(FORWARD, 25, MM)
    drivetrain.drive_for(REVERSE, 25, MM)
    shoot(100, 20)
    drivetrain.turn_to_heading(157, DEGREES)
    shoot(90, 140)
    goTo(-700,400,0)



    
    


    
    


    


    
    

    


    
    


#Define move to GPS coordinates funciton
def goTo(target_x, target_y, reverse):
    # Set initial position
    x1 = gps.x_position(MM)
    y1 = gps.y_position(MM)
    
    # Identify Delta(s):
    delta_x = target_x - x1
    delta_y = target_y - y1

    # Pythagorean theorem:
    distance = math.sqrt(delta_x**2 + delta_y**2)
    
    # Identify Turn Angle:
    if ( delta_x == 0 ):
        if ( delta_y < 0):
            direction = 90
        else:
            direction = 270
    else:
        direction = - math.atan(delta_y / delta_x) * 180 / math.pi
    
    # Identify Angle to Turn to:
    if ( delta_x < 0 ):
        direction = direction + 180
    if ( reverse != 0 ):
        direction = direction + 180
    if ( direction > 360 ):
        direction = direction - 360
    
    # Turn to Angle: 
    drivetrain.turn_to_heading(direction, DEGREES, wait=True)
    
    # Initiate Drive:
    if ( reverse != 0 ):
        drivetrain.drive_for(REVERSE, distance, MM, wait=True)
    else:
        drivetrain.drive_for(FORWARD, distance, MM, wait=True)

#Function Shoot:
def shoot(power, duration):
    intake_motor_group.set_velocity(power, PERCENT)
    intake_motor_group.spin_for(REVERSE, duration, DEGREES)

# VR threads — Do not delete
vr_thread(main)
