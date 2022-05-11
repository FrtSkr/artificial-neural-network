import option
from Neuron import Neuron

class OutputLayer:
    def __init__(self):
        self.O1 = Neuron(option.Wo, option.B)