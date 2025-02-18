import numpy as np

INPUT_DIM = 4
OUT_DIM = 3
H_DIM = 10

x = np.array([7.9, 3.1, 7.5, 1.8])

W1 = np.array([[0.33462099, 0.10068401, 0.20557238, -0.19043767, 0.40249301, -0.00925352, 0.00628916, 0.74784975,
                0.25069956, -0.09290041],
               [0.41689589, 0.93211640, -0.32300143, -0.13845456, 0.58598293, -0.29140373, -0.28473491, 0.48021000,
                -0.32318306, -0.34146461],
               [-0.21927019, -0.76135162, -0.11721704, 0.92123373, 0.19501658, 0.00904006, 1.03040632, -0.66867859,
                -0.01571104, -0.08372566],
               [-0.67791724, 0.07044558, -0.40981071, 0.62098450, -0.33009159, -0.47352435, 0.09687051, -0.68724299,
                0.43823402, -0.26574543]])

b1 = np.array(
    [-0.34133575, -0.24401602, -0.06262318, -0.30410971, -0.37097632, 0.02670964, -0.51851308, 0.54665141, 0.20777536,
     -0.29905165])

W2 = np.array([[0.41186367, 0.15406952, -0.47391773],
               [0.79701137, -0.64672799, -0.06339983],
               [-0.20137522, -0.07088810, 0.00212071],
               [-0.58743081, -0.17363843, 0.93769169],
               [0.33262125, 0.18999841, -0.14977653],
               [0.04450406, 0.26168097, 0.10104333],
               [-0.74384144, 0.33092591, 0.65464737],
               [0.45764631, 0.48877246, -1.16928700],
               [-0.16020630, -0.12369116, 0.14171301],
               [0.26099978, 0.12834471, 0.20866959]])

b2 = np.array([-0.16286677, 0.06680119, -0.03563594])


def relu(t):
    return np.maximum(t, 0)


def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)


def predict(x):
    t1 = x @ W1 + b1
    h1 = relu(t1)
    t2 = h1 @ W2 + b2
    z = softmax(t2)
    return z


probs = predict(x)
pred_class = np.argmax(probs)
class_names = ['Setosa', 'Versicolor', 'Virginica']
print('Predicted class:', class_names[pred_class])
