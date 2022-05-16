import math

class Neuron:
    def __init__(self, w, b):
        self.w = w
        self.b = b

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def feedForward(self, data):

        result = self.sigmoid(self.weightedSumInput(data))
        return result

    def weightedSumInput(self, data):

        sumX = 0
        for i in range(len(data)):
            sumX += data[i] * self.w[i]
        sumX += self.b
        return sumX