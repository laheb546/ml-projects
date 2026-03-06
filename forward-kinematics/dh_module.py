import numpy as np
def dh(alpha,a,theta,d):
    """ 
    compute standard DH transformation matrix 
    INPUTS:- theta,a,d,alpha:float(radians,meters)
    OUTPUT:- 4x4 numpy array 
    """
    T=np.array([
        [np.cos(theta),-np.sin(theta)*np.cos(alpha),np.sin(theta)*np.sin(alpha),a*np.cos(theta)],[np.sin(theta),np.cos(theta)*np.cos(alpha),-np.cos(theta)*np.sin(alpha),a*np.sin(alpha)],[0,          np.sin(alpha),          np.cos(alpha),          d],[0,          0,          0,          1]
                ])
    return T
