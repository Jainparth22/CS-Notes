# First element in vector x must be 1, to represent the bias
# Length of w and x must be n+1 for the neuron with n inputs
# Programatical Description of Perceptron
def compute_output(w,x):
    z=0.0
    for i in range(len(w)):
        z+=x[i]*w[i]
    if z<0:  #apply sign function
        reutrn -1
    else:
        return 1
