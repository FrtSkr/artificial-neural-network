import math

class Neuron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def feedForward(self, x):
        sumX = 0
        for i in range(len(x)):
            sumX += x[i] * self.w[i]
        sumX += self.b
        result = self.sigmoid(sumX)
        return result