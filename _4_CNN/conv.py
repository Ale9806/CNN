import numpy as np
from math import floor

def normal(A,fil):
    """ Implements the simplest form of Convolution """
    N=A.shape[0]
    F=fil.shape[0]
    P=0
    S=1
    # Calculates the expected dimenesions of Convolution output
    conv_size = int(floor((N + 2*P - F)/S +1))
    # Creates the Convolution object with zeros
    C=np.ones((conv_size ,conv_size ))

    # Convolution
    for n1 in range(conv_size):     # ROW ADVANCE
        for n2 in range(conv_size): # COLUMN ADVANCE
            C[n1,n2]=(A[n1:n1+F,n2:n2+F]*fil).sum()

    return C

def padding(A,P):
    A_w_p=np.zeros((A.shape[0]+P+P,A.shape[0]+P+P))
    A_w_p[P:-P,P:-P]=A
    return A_w_p
