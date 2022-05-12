import option
from DataSet import DataSet
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