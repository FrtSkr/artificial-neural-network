import option
from Neuron import Neuron

class HiddenLayer:
    def __init__(self):
        self.F1 = Neuron(option.Wh, option.B)
        self.F2 = Neuron(option.Wh, option.B)
        self.F3 = Neuron(option.Wh, option.B)