# Robot Forward Kinematics Python Module
## Overview
This project implement **forward kinematics (FK)** using the **Denavit-Hartenberg (DH) convention**
The user can dynamically enter joint parameters and compute the **end-effector transformation matrix**
_ _ _
## Project Structure
1.**dh_module.py**
-contains 'dh(theta,a,d,alpha)' function
-computes a single link's **DH transformation matrix** using Numpy
2.**fk_module.py**
-contains 'forward_kinematics(dh_params)' function
-computes the **full forward kinematics** for a series of links
-optional:helper functions if needed (e.g., 'get_dh_params()' for demo)
3.**test_fk.py**
-Main script to **run the FK computation**
-collects user input for number of joints and DH parameteres
-calls 'forward_kinematics()' and prints **end-effector matrix**
_ _ _
# Dependencies
-Python 3.X
-Numpy 
Install Numpy with: pip install numpy
_ _ _
## Notes
-'dh_module.py' and 'fk_module.py' are **reusable** for other robot FK projects
-'test_fk.py' is **interactive** for testing purposes
-you can extend the project to **GUI**
