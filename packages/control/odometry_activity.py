from typing import Tuple

def delta_phi(ticks: int, prev_ticks: int, resolution: int) -> Tuple[float, float]:
    """
        Args:
            ticks: Current tick count from the encoders.
            prev_ticks: Previous tick count from the encoders.
            resolution: Number of ticks per full wheel rotation returned by the encoder.
        Return:
            dphi: Rotation of the wheel in radians.
            ticks: current number of ticks.
    """

    delta_ticks = ticks-prev_ticks

    # Assuming no wheel slipping
    dphi = 2*np.pi*delta_ticks/resolution


    return dphi, ticks

    def pose_estimation(
        R: float,
        baseline: float,
        x_prev: float,
        y_prev: float,
        theta_prev: float,
        delta_phi_left: float,
        delta_phi_right: float,
) -> Tuple[float, float, float]:
    
#        Calculate the current Duckiebot pose using the dead-reckoning approach.
        
#        Args:
#            R:                  radius of wheel (assumed identical) - this is fixed in simulation,
#                                and will be imported from your saved calibration for the real robot
#            baseline:           distance from wheel to wheel; 2L of the theory
#            x_prev:             previous x estimate - assume given
#            y_prev:             previous y estimate - assume given
#            theta_prev:         previous orientation estimate - assume given
#            delta_phi_left:     left wheel rotation (rad)
#            delta_phi_right:    right wheel rotation (rad)
#
#        Return:
#            x_curr:                  estimated x coordinate
#            y_curr:                  estimated y coordinate
#            theta_curr:              estimated heading
     

    # x_curr = x_prev + R*(delta_phi_left+delta_phi_right)*np.cos(theta_prev)/2
    # y_curr = y_prev + R*(delta_phi_left+delta_phi_right)*np.sin(theta_prev)/2
    # theta_curr = theta_prev + R*(delta_phi_right-delta_phi_left)/(baseline)

   
        w = [R, 2*R / baseline, 1]

        x = np.array(
            [
                [
                    (delta_phi_left + delta_phi_right) * np.cos(theta_prev) / 2,
                    (delta_phi_left + delta_phi_right) * np.sin(theta_prev) / 2,
                    0,
                ],
                [0, 0, (delta_phi_right - delta_phi_left) / 2],
                [x_prev, y_prev, theta_prev],
            ]
        )

        x_curr, y_curr, theta_curr = np.array(w).dot(x)

        return x_curr, y_curr, theta_curr

#%load_ext autoreload
#%autoreload 2

x0 = y0 = 0 # meters
theta0 = 0 # radians

import numpy as np 
 
N_tot = 135 # total number of ticks per revolution
alpha = 2 * np.pi / N_tot # wheel rotation per tick in radians

print(f"The angular resolution of our encoders is: {np.rad2deg(alpha)} degrees")
# Feel free to play with the numbers to get an idea of the expected outcome

ticks_left = 1
prev_tick_left = 0

ticks_right = 0
prev_tick_right = 0
# How much would the wheels rotate with the above tick measurements? 

delta_ticks_left = ticks_left-prev_tick_left # delta ticks of left wheel 
delta_ticks_right = ticks_right-prev_tick_right # delta ticks of right wheel 

rotation_wheel_left = alpha * delta_ticks_left # total rotation of left wheel 
rotation_wheel_right = alpha * delta_ticks_right # total rotation of right wheel 

print(f"The left wheel rotated: {np.rad2deg(rotation_wheel_left)} degrees")
print(f"The right wheel rotated: {np.rad2deg(rotation_wheel_right)} degrees")
# What is the radius of your wheels? 
R = 0.0318 # insert value measured by ruler, in *meters*
# What is the distance travelled by each wheel?

d_left = R * rotation_wheel_left 
d_right = R * rotation_wheel_right

print(f"The left wheel travelled: {d_left} meters")
print(f"The right wheel rotated: {d_right} meters")
# How much has the robot travelled? 

d_A = (d_left + d_right)/2

print(f"The robot has travelled: {d_A} meters")
# What is the baseline length of your robot? 

baseline_wheel2wheel = 0.1 #  Distance between the center of the two wheels, expressed in meters 
# How much has the robot rotated? 

Delta_Theta = (d_right-d_left)/baseline_wheel2wheel # expressed in radians

print(f"The robot has rotated: {np.rad2deg(Delta_Theta)} degrees")

