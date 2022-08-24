import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype = np.int32)
    '''
    以下と同じ
    y = x > 0
    return y.astype(np.int32)

    例
    print(x) -> [-1 1 2]
    print(y) -> [False True True]
    return -> [0 1 1]
    '''

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
