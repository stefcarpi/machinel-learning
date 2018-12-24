import nn as NN
import numpy as np
import matplotlib.pyplot as plt
import imp
import utils as u

# number of patterns for each class
p_class1 = 70
p_class2 = 30
# attributes/features
n = 10

X = np.vstack((np.random.normal(2., 1., (p_class1, n)),
               np.random.normal(6., 1., (p_class2, n))))

# y = np.vstack((np.hstack((np.ones(p_class1), np.zeros(p_class2))),
#                np.hstack((np.zeros(p_class1), np.ones(p_class2))))).T
y = np.hstack((np.ones(p_class1), np.zeros(p_class2))).reshape(-1, 1)

imp.reload(NN)
imp.reload(u)

nn = NN.NeuralNetwork(hidden_sizes=[10])

nn.train(X, y, eta=0.2, regularizer=[0.01, 'l2'], epochs=500, batch_size=10,
         alpha=0.1, w_par=6)

y_pred = nn.predict(X)
np.round(y_pred, 1)
y.T
np.abs((np.round(y_pred, 0)-y.T)).sum()


nn.error_per_epochs[-1]
# (np.einsum('kp->', (y_pred-y.T)**2) / X.shape[0])

plt.plot(range(len(nn.error_per_epochs)), nn.error_per_epochs)
plt.ylabel('MSE error by epoch')
plt.xlabel('Epochs')
plt.grid()
plt.savefig('../images/learning_curve.pdf')
plt.close()

plt.plot(range(len(nn.error_per_batch)), nn.error_per_batch)
plt.ylabel('SE error by batch')
plt.xlabel('Epochs*Batches')
plt.grid()
plt.savefig('../images/learning_curve_batch.pdf')
plt.close()


###########################################################
def lapply(l, f):
    '''
    Apply function f to each element of the list l
    (R style)
    '''
    return [f(el) for el in l]

# lapply(nn.a, len)
