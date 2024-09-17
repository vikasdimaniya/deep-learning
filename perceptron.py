import random
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, N):
        self.N = N
        self.weights = [0.0 for _ in range(N)]
        self.b = 0

    def predict(self, X):
        sum = self.b
        for i in range(self.N):
            sum += self.weights[i] * X[i]
        return self.activationFunction(sum)

    def activationFunction(self, sum):
        return 1 if sum > 0 else -1

    def train(self, X, expectedOutput):
        y = self.predict(X)
        error = expectedOutput - y
        if error != 0:
            for i in range(self.N):
                self.weights[i] += expectedOutput * X[i]
            self.b += expectedOutput

# return the expected output 1 if the point is above the line y=0, else -1
def predict_x_equal_zero():
    X = [random.randint(-100, 100) for _ in range(2)]
    expectedOutput = 1 if X[0] > 0 else -1
    return X, expectedOutput

def predict_y_equal_zero():
    X = [random.randint(-100, 100) for _ in range(2)]
    expectedOutput = 1 if X[1] > 0 else -1
    return X, expectedOutput

def predict_y_equal_x():
    X = [random.randint(-100, 100) for _ in range(2)]
    if X[0] > X[1]:
        expectedOutput = 1
    else:
        expectedOutput = -1
    return X, expectedOutput

if __name__ == "__main__":
    p = Perceptron(2)
    TOTAL_TRAINING = 1000
    plt.ion()
    
    for i in range(TOTAL_TRAINING):
        # function which we want to learn
        X, expectedOutput = predict_y_equal_zero()
        p.train(X, expectedOutput)

        if p.weights[1] != 0:  # Ensuring not dividing by zero
            slope = -p.weights[0] / p.weights[1]
            intercept = -p.b / p.weights[1]
            x_vals = [-100, 100]
            y_vals = [slope * x + intercept for x in x_vals]
        elif p.weights[0]!=0:
            # In case the second weight is zero, plot a vertical line
            x_vals = [-p.b / p.weights[0], -p.b / p.weights[0]]
            y_vals = [-100, 100]
        else:
            # In case both weights are zero, do nothing
            x_vals = [-100, 100]
            y_vals = [-100, 100]
        
        # Clearing
        plt.clf()
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)

        # Plotting new data
        plt.plot(x_vals, y_vals, 'r-', label='Decision Boundary')
        plt.scatter(X[0], X[1], color='b' if expectedOutput == 1 else 'g')
        plt.draw()
        plt.pause(0.01)
    
    print("Final Weights:", p.weights)
    print("Final Bias:", p.b)
