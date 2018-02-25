from sklearn.neural_network import MLPClassifier
import numpy as np


def main():
    x = np.array([[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [1, 0, 0, 0]])
    print(x)
    y = np.array([0, 1, 1, 1])
    ml = MLPClassifier()
    ml.fit(x, y)
    print(ml.predict([[0,0,1,0]]))


if __name__ == '__main__':
    main()
