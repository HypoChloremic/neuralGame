import matrix
import math

class NeuralNetwork:
    def __init__(self, inp, hidden, output):
        print("running neuralNet")
        # constants
        self.input   = inp
        self.hidden = hidden
        self.output  = output
        arg = [self.input, self.hidden, self.output]
        self.weights = [self.genWeights(inp,hidden), self.genWeights(hidden, output)]


    def genWeights(self, fir, sec):
        weights = []
        for i in range(sec):
            weights.append([])
            for j in range(fir):
                weights[i].append(random(0,1)) 
        return weights
    

    def dotProduct(self, vector, matrix):
        #print(vector, matrix)
        temp = []
        for i in range(len(vector)):
            temp.append([])
            for j in range(len(matrix)):
              temp[-1].append(matrix[j][i]*vector[i])

        dotted = []
        for i in range(len(temp)):
          p = self.sigmoid(sum(temp[i]))
          dotted.append(p)
        return dotted


    def drive(self, fundInput):
        print("fund", fundInput)
        hidden = self.dotProduct(fundInput, self.weights[0])
        output = self.dotProduct(hidden, self.weights[1])
        print(output)
        return output

    def sigmoid(self, x):
        #return 1 / (1 + math.exp(-x))
        return 2 / (1 + x)
