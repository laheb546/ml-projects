import numpy as np
from dh_module import dh

def forward_kinematics(dh_params):
    """
    compute forward kinematics for multiple links 
    OUTPUTS:- 
     T_total:final 4x4 numpy array
     chain:list of cumulative 4x4 matrices for each link
    """
    T_total=np.eye(4)
    chain=[]
    for theta,a,d,alpha in dh_params:
      T_link=dh(theta,a,d,alpha)
      T_total=T_total @ T_link
      chain.append(T_total)
    return T_total,chain