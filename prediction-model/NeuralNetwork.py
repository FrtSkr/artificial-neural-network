from HiddenLayer import HiddenLayer
from OutputLayer import OutputLayer

class NeuralNetwork:
    def __init__(self, dataX, dataY):
        self.HL = HiddenLayer()
        self.OL = OutputLayer()
        self.dataX = dataX
        self.dataY = dataY

    def feedForward(self, data):

        resultF1 = self.HL.F1.feedForward(data)
        resultF2 = self.HL.F2.feedForward(data)
        resultF3 = self.HL.F3.feedForward(data)

        resultO1 = self.OL.O1.feedForward([resultF1, resultF2, resultF3])
        return resultO1

    def sigmoid_derivative(self, data): # data değişkenine her nöronun net çıktı değeri gelecek
        return data * (1 - data)

    def MSE(self, data): # data değişkenine 1 epoch sonucunda oluşan hataların dizisi gelecek
        result = 0
        for i in data:
            result += data**2

        result = result / len(data)
        return result
