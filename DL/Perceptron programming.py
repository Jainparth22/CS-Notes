# Coding Perceptron in Python to implement NAND function
import random

def show_learning(w):
    print('w0={:.2f}, w1={:.2f}, w2={:.2f}'.format(w[0],w[1],w[2]))

#define variables needed for control training process
random.seed(7) # to make repeatable
LEARNING_RATE=0.1
index_list=[0,1,2] # to randomly select training data

#define training examples
x_train=[(1.0,-1.0,-1.0), # NAND(0,0)
         (1.0,-1.0,1.0),  # NAND(0,1)
         (1.0,1.0,-1.0),  # NAND(1,0)
         (1.0,1.0,1.0)]   # NAND(1,1)
y_train=[1.0,1.0,1.0,-1.0]  # expected output for NAND function(ground truth)

# Define perceptron weights, initialized to random values
w=[random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)]
# w=[0.2,-0.6,0.25]
print('Initial weights:')
show_learning(w)
 

#first element in vector x must be 1, to represent the bias
# Length of w and x must be n+1 for the neuron with n inputs
def compute_output(w,x):
    z=0.0
    for i in range(len(w)):
        z+=x[i]*w[i]
    if z<0:  #apply sign function
        return -1
    else:
        return 1


#perceptron Training loop
all_correct=False
while not all_correct:
    all_correct=True
    #randomly select training data
    random.shuffle(index_list)
    for i in index_list:
        x=x_train[i]
        y=y_train[i]
        p_out=compute_output(w,x)
        if p_out!=y: # if prediction is wrong, update weights
            
            for i in range(0,len(w)):
                # w[i]+=LEARNING_RATE*(y-p_out)*x[i] # wi​=wi​+η(y−pout​)xi ​#wi​=wi​+2ηyxi​
                
            # 2η when wrong
            # this is Error-correction / Delta-style update
            # Convergence -usually faster steps
            # When a mistake occurs:
            # y-pout=±2
            # So the update becomes:
            # # wi=wi+2ηyxi
            # which is twice as large as the perceptron update.
            # So the commented version moves the weight twice as far.
          

                w[i] += (y*LEARNING_RATE*x[i]) # wi​=wi​+ηyxi​

         
            # update size : η , Perceptron learning rule
            # where:
            # η = learning rate
            # y = target output (-1 or 1)
            # xi= input
            # This is the classic perceptron learning rule when outputs are encoded as -1 and +1.
            
            all_correct=False
            print('Final weights:')
            show_learning(w)

print('y0_truth=','%5.2f' %y_train[0],', y0_predict=','%5.2f' %compute_output(w,x_train[0]))
print('y1_truth=','%5.2f' %y_train[1],', y1_predict=','%5.2f' %compute_output(w,x_train[1]))
print('y2_truth=','%5.2f' %y_train[2],', y2_predict=','%5.2f' %compute_output(w,x_train[2]))
print('y3_truth=','%5.2f' %y_train[3],', y3_predict=','%5.2f' %compute_output(w,x_train[3]))
