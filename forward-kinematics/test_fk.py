import numpy as np
from dh_module import dh
from fk_module import forward_kinematics
"""
INPUTS:- dh_params:list of tuples [(theta,a,d,alpha),...]
"""
def get_dh_params(n_joints):
   dh_params=[]
   for i in range(1,n_joints+1):
      theta=float(input(f"Enter theta{i} (deg): "))*np.pi/180
      a=float(input(f"Enter a{i}: "))
      d=float(input(f"Enter d{i}: "))
      alpha=float(input(f"Enter alpha{i} (deg): "))*np.pi/180
      dh_params.append((theta,a,d,alpha))
      return dh_params
n_joints=int(input("Number of joints:"))
dh_params=get_dh_params(n_joints)
T_end,chain=forward_kinematics(dh_params) 
print("\n Final End-Effector Transform: \n", T_end)