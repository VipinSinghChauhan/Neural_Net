import numpy as np

class Node:
    
    def __init__(self,input_shape):
##        np.random.seed(42)
        self.weight = np.random.rand(input_shape)
        self.bias = np.random.rand(1)

    def node_product(self,input):
        return (sum(input*self.weight) + self.bias)[0]


class NeuralNet:
    def __init__(self,inputs,outputs):
        self.inputs = inputs
        self.outputs = outputs
    def calculate_output(self):
        output_nodes = []
        for o in range(self.outputs):
            output_nodes.append(Node(len(self.inputs)).node_product(self.inputs))

        return output_nodes

inputs = [1,2,3]
n1 = NeuralNet(inputs,4).calculate_output()
n2 = NeuralNet(n1,5).calculate_output()
n3 = NeuralNet(n2,1).calculate_output()

print(inputs)
print(n1)
print(n2)
print(n3)



        
        
